import pandas as pd
from typing import Literal, Callable
from histcite.parse_reference import ParseReference
from histcite.recognize_reference import RecognizeReference


class ProcessGeneralFile:
    @staticmethod
    def concat_refs(cr_field_series: pd.Series, 
                        source_type: Literal['wos', 'cssci', 'scopus']) -> pd.DataFrame:
        total_ref_list: list[dict[str, str]] = []
        for idx, cell in cr_field_series.items():
            parse_result = ParseReference(idx, cell, source_type).parse_cr_cell()
            if parse_result is not None:
                total_ref_list.extend(parse_result)
        refs_df = pd.DataFrame(total_ref_list)
        return refs_df
    
    @staticmethod
    def extract_citing_relation(recognize_ref_func: Callable[[pd.DataFrame, pd.DataFrame, int], tuple[list[int], list[int]]], 
                                    docs_df: pd.DataFrame, 
                                    refs_df: pd.DataFrame) -> tuple[pd.Series, list[int]]:
        result = docs_df.apply(lambda row: recognize_ref_func(docs_df, refs_df, row.name), axis=1)
        cited_doc_index_field = result.apply(lambda x: x[0])
        local_ref_series = result.apply(lambda x: x[1])
        local_ref_list: list[int] = sum(local_ref_series, [])
        local_ref_list.sort()
        return cited_doc_index_field, local_ref_list
        

class ProcessFile:
    def __init__(self, docs_df: pd.DataFrame, source_type: Literal['wos', 'cssci', 'scopus']):
        self.docs_df = docs_df.copy()
        self.source_type = source_type
    
    def extract_reference(self):
        """extract total references and generate dataframe"""
        cr_field_series = self.docs_df['CR']
        if self.source_type == 'wos':
            refs_df = ProcessGeneralFile.concat_refs(cr_field_series, 'wos')
        elif self.source_type == 'cssci':
            refs_df = ProcessGeneralFile.concat_refs(cr_field_series, 'cssci')
        elif self.source_type == 'scopus':
            refs_df = ProcessGeneralFile.concat_refs(cr_field_series, 'scopus')
        else:
            raise ValueError('Invalid source type')
        
        # maybe duplicate reference in some docs' references
        refs_df.drop_duplicates(ignore_index=True, inplace=True)
        refs_df.insert(0, 'ref_index', refs_df.index)
        self.refs_df = refs_df

    @staticmethod
    def __reference2citation(reference_field: pd.Series) -> pd.Series:
        citation_field = pd.Series([[] for i in range(len(reference_field))])
        for doc_index, ref_list in reference_field.items():
            if ref_list:
                for ref_index in ref_list:
                    citation_field[ref_index].append(doc_index)
        return citation_field

    def process_citation(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        if self.source_type == 'wos':
            self.docs_df['DI'] = self.docs_df['DI'].str.lower()
            self.refs_df = self.refs_df.astype({'PY':'int64[pyarrow]'})
            cited_doc_index_field, local_ref_list = ProcessGeneralFile.extract_citing_relation(RecognizeReference.recognize_wos_reference, self.docs_df, self.refs_df)
        
        elif self.source_type == 'cssci':
            self.docs_df['TI'] = self.docs_df['TI'].str.lower()
            self.refs_df['TI'] = self.refs_df['TI'].str.lower()
            cited_doc_index_field, local_ref_list = ProcessGeneralFile.extract_citing_relation(RecognizeReference.recognize_cssci_reference, self.docs_df, self.refs_df)
        
        elif self.source_type == 'scopus':
            self.docs_df['TI'] = self.docs_df['TI'].str.lower()
            self.refs_df['TI'] = self.refs_df['TI'].str.lower()
            cited_doc_index_field, local_ref_list = ProcessGeneralFile.extract_citing_relation(RecognizeReference.recognize_scopus_reference, self.docs_df, self.refs_df)
        else:
            raise ValueError('Invalid source type')
        
        citing_doc_index_field = self.__reference2citation(cited_doc_index_field)
        lcr_field = cited_doc_index_field.apply(len)
        lcs_field = citing_doc_index_field.apply(len)
        citing_relation_df = pd.DataFrame({'doc_index': self.docs_df.doc_index})
        citing_relation_df['cited_doc_index'] = [';'.join([str(j) for j in i]) if i else None for i in cited_doc_index_field]
        citing_relation_df['citing_doc_index'] = [';'.join([str(j) for j in i]) if i else None for i in citing_doc_index_field]
        citing_relation_df['LCR'] = lcr_field
        citing_relation_df['LCS'] = lcs_field
        # citing_relation_df.dropna(how='all', subset=['cited_doc_index', 'citing_doc_index'], inplace=True)
        
        self.refs_df['local'] = False
        self.refs_df.loc[local_ref_list, 'local'] = True
        return citing_relation_df, self.refs_df