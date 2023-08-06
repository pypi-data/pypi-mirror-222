import pandas as pd


class RecognizeCommonReference:
    def __init__(self, compare_cols: list[str]):
        self.compare_cols = compare_cols

    def select_df(self, docs_df: pd.DataFrame, refs_df: pd.DataFrame, row_index: int) -> tuple[pd.DataFrame, pd.DataFrame]:
        row_data_year = docs_df.loc[row_index, 'PY']
        child_refs_df = refs_df[refs_df['doc_index'] == row_index].dropna(subset=self.compare_cols)
        child_docs_df = docs_df[(docs_df['PY'] <= row_data_year) & (docs_df['doc_index'] != row_index)].dropna(subset=self.compare_cols)
        return child_docs_df, child_refs_df

    def recognize_refs(self, child_docs_df: pd.DataFrame, 
                      child_refs_df: pd.DataFrame) -> tuple[list[int], list[int]]:
        cited_ref_list: list[int] = []
        local_ref_list: list[int] = []
        shared_df = child_docs_df[['doc_index']+self.compare_cols].merge(child_refs_df[['ref_index']+self.compare_cols], on=self.compare_cols)
        if shared_df.shape[0] > 0:
            cited_ref_list = sorted(set(shared_df['doc_index']))
            local_ref_list = sorted(set(shared_df['ref_index']))
        return cited_ref_list, local_ref_list

class RecognizeReference():
    @staticmethod
    def recognize_wos_reference(docs_df: pd.DataFrame,
                                refs_df: pd.DataFrame,
                                row_index: int) -> tuple[list[int], list[int]]:
        cited_ref_list:list[int] = []
        local_ref_list:list[int] = []
        child_refs_df = refs_df[refs_df['doc_index'] == row_index]

        # DOI exists
        child_refs_df_doi = child_refs_df['DI'].dropna()
        child_docs_df_doi = docs_df[(docs_df['DI'].notna()) & (docs_df['doc_index'] != row_index)]['DI']
        cited_ref_list.extend(child_docs_df_doi[child_docs_df_doi.isin(child_refs_df_doi)].index)
        local_ref_list.extend(child_refs_df_doi[child_refs_df_doi.isin(child_docs_df_doi)].index)

        # DOI not exists
        compare_cols = ['First_AU', 'PY', 'J9', 'BP']
        child_refs_df_left = child_refs_df[child_refs_df['DI'].isna()].dropna(subset=compare_cols)
        child_docs_df_left = docs_df[(~docs_df['doc_index'].isin(cited_ref_list+[row_index]))
                                     & (docs_df['PY'].isin(child_refs_df_left['PY'])) 
                                     & (docs_df['BP'].isin(child_refs_df_left['BP']))].dropna(subset=compare_cols)
        recognize_instance = RecognizeCommonReference(compare_cols)
        result = recognize_instance.recognize_refs(child_docs_df_left, child_refs_df_left)
        cited_ref_list.extend(result[0])
        local_ref_list.extend(result[1])
        return cited_ref_list, local_ref_list

    @staticmethod
    def recognize_cssci_reference(docs_df: pd.DataFrame,
                                  refs_df: pd.DataFrame,
                                  row_index: int) -> tuple[list[int], list[int]]:
        compare_cols = ['First_AU', 'TI']
        recognize_instance = RecognizeCommonReference(compare_cols)
        child_docs_df, child_refs_df = recognize_instance.select_df(docs_df, refs_df, row_index)
        return recognize_instance.recognize_refs(child_docs_df, child_refs_df)

    @staticmethod
    def recognize_scopus_reference(docs_df: pd.DataFrame,
                                   refs_df: pd.DataFrame,
                                   row_index: int) -> tuple[list[int], list[int]]:
        compare_cols = ['First_AU', 'TI']
        recognize_instance = RecognizeCommonReference(compare_cols)
        child_docs_df, child_refs_df = recognize_instance.select_df(docs_df, refs_df, row_index)
        return recognize_instance.recognize_refs(child_docs_df, child_refs_df)