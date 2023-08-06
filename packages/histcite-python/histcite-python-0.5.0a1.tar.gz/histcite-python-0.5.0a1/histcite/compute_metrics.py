import os
import pandas as pd
from typing import Literal, Optional


class ComputeMetrics:
    def __init__(self, docs_df: pd.DataFrame, 
                 citing_relation_df: pd.DataFrame,
                 refs_df: pd.DataFrame, 
                 source_type: Literal['wos', 'cssci', 'scopus']):
        self.merged_docs_df = docs_df.merge(citing_relation_df[['doc_index', 'LCR', 'LCS']], on='doc_index')
        self.refs_df = refs_df
        self.source_type = source_type

    def __generate_df(self, use_cols: list[str], 
                      col: str, 
                      split_char: Optional[str] = None, 
                      str_lower: bool = False, 
                      sort_field: Optional[str] = None) -> pd.DataFrame:
        df = self.merged_docs_df[use_cols]
        # 如果字段包含多个值，则进行拆分
        if split_char:
            df = df.dropna(subset=[col])
            df = df.astype({col: 'str'})
            if str_lower:
                df[col] = df[col].str.lower()
            df[col] = df[col].str.split(split_char)
            df = df.explode(col)
            df = df.reset_index(drop=True)

        if 'LCS' in use_cols and 'TC' in use_cols:
            grouped_df = df.groupby(col).agg({col: 'count', 'LCS': 'sum', 'TC': 'sum'})
            grouped_df.rename(columns={col: 'Recs', 'LCS': 'TLCS', 'TC': 'TGCS'}, inplace=True)
        elif 'LCS' in use_cols and 'TC' not in use_cols:
            grouped_df = df.groupby(col).agg({col: 'count', 'LCS': 'sum'})
            grouped_df.rename(columns={col: 'Recs', 'LCS': 'TLCS'}, inplace=True)
        elif 'LCS' not in use_cols and 'TC' not in use_cols:
            grouped_df = df.groupby(col).agg({col: 'count'}).rename(columns={col: 'Recs'})
        else:
            raise ValueError('Invalid columns list')

        if col == 'Author full names':
            grouped_df.index = grouped_df.index.str.replace(r'\(\d+\)', '', regex=True)
        
        if not sort_field:
            sort_field = 'Recs'
        return grouped_df.sort_values(sort_field, ascending=False)

    def _generate_author_df(self):
        if self.source_type == 'wos':
            use_cols = ['AU', 'LCS', 'TC']
        elif self.source_type == 'cssci':
            use_cols = ['AU', 'LCS']
        elif self.source_type == 'scopus':
            use_cols = ['Author full names', 'LCS', 'TC']
        else:
            raise ValueError('Invalid source type')
        return self.__generate_df(use_cols, use_cols[0], '; ')

    def _generate_keywords_df(self):
        if self.source_type in ['wos', 'scopus']:
            use_cols = ['DE', 'LCS', 'TC']
        elif self.source_type == 'cssci':
            use_cols = ['DE', 'LCS']
        else:
            raise ValueError('Invalid source type')
        return self.__generate_df(use_cols, 'DE', '; ', True)

    def _generate_institution_df(self):
        if self.source_type in ['wos', 'scopus']:
            use_cols = ['C3', 'LCS', 'TC']
        elif self.source_type == 'cssci':
            use_cols = ['C3', 'LCS']
        else:
            raise ValueError('Invalid source type')
        return self.__generate_df(use_cols, 'C3', '; ')

    def _generate_records_df(self):
        if self.source_type in ['wos', 'scopus']:
            use_cols = ['AU', 'TI', 'SO', 'PY', 'TI', 'LCS', 'TC', 'LCR', 'NR', 'source file']
        elif self.source_type == 'cssci':
            use_cols = ['AU', 'TI', 'SO', 'PY', 'LCS', 'LCR', 'NR', 'source file']
        else:
            raise ValueError('Invalid source type')
        records_df = self.merged_docs_df[use_cols]
        if 'TC' in use_cols:
            records_df = records_df.rename(columns={'TC': 'GCS'})
        if 'NR' in use_cols:
            records_df = records_df.rename(columns={'NR':'GCR'})
        return records_df

    def _generate_journal_df(self):
        if self.source_type in ['wos', 'scopus']:
            use_cols = ['SO', 'LCS', 'TC']
        elif self.source_type == 'cssci':
            use_cols = ['SO', 'LCS']
        else:
            raise ValueError('Invalid source type')
        return self.__generate_df(use_cols, 'SO')

    def _generate_year_df(self):
        use_cols = ['PY']
        return self.__generate_df(use_cols, 'PY').sort_values(by='PY')

    def _generate_document_type_df(self):
        use_cols = ['DT']
        return self.__generate_df(use_cols, 'DT')

    def _generate_reference_df(self):
        """生成参考文献表，按照引用次数降序排列，同时标记是否为本地文献"""
        if self.source_type == 'wos':
            keys = ['First_AU', 'PY', 'J9', 'VL', 'BP', 'DI', 'local']
        elif self.source_type == 'cssci':
            keys = ['First_AU', 'TI', 'SO', 'PY', 'VL', 'local']
        elif self.source_type == 'scopus':
            keys = ['First_AU', 'TI', 'SO', 'VL', 'BP', 'EP', 'PY', 'local']
        else:
            raise ValueError('Invalid source type')
        refs_df = self.refs_df.groupby(by=keys, dropna=False).size().reset_index(name='Recs')
        refs_df.insert(len(refs_df.columns)-1, 'local', refs_df.pop('local'))
        return refs_df.sort_values(by='Recs', ascending=False)

    def write2excel(self, save_path: str):
        """将统计结果写入excel"""
        save_folder_path = os.path.dirname(save_path)
        if not os.path.exists(save_folder_path):
            os.makedirs(save_folder_path)
        with pd.ExcelWriter(save_path) as writer:
            self._generate_records_df().to_excel(writer, sheet_name='Records', index=False)
            self._generate_author_df().to_excel(writer, sheet_name='Authors')
            self._generate_journal_df().to_excel(writer, sheet_name='Journals')
            self._generate_reference_df().to_excel(writer, sheet_name='Cited References', index=False)
            self._generate_keywords_df().to_excel(writer, sheet_name='Keywords')
            self._generate_year_df().to_excel(writer, sheet_name='Years')
            
            if self.source_type in ['wos', 'cssci']:
                self._generate_institution_df().to_excel(writer, sheet_name='Institutions')
            if self.source_type in ['wos', 'scopus']:
                self._generate_document_type_df().to_excel(writer, sheet_name='Document Type')