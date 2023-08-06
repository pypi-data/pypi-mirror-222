import pytest
import pandas as pd
from typing import Literal
from histcite.compute_metrics import ComputeMetrics

@pytest.mark.skip(reason='This is a function factory')
def test_statistics(docs_df_path: str, refs_df_path: str, citing_relation_df_path: str, source_type: Literal['wos','cssci','scopus']):
    def new_func():
        docs_df = pd.read_csv(docs_df_path, dtype_backend='pyarrow')
        refs_df = pd.read_csv(refs_df_path, dtype_backend='pyarrow')
        citing_relation_df = pd.read_csv(citing_relation_df_path, dtype_backend='pyarrow')
        cm = ComputeMetrics(docs_df, citing_relation_df, refs_df, source_type)
        author_df = cm._generate_author_df()
        keywords_df = cm._generate_keywords_df()
        return author_df, keywords_df
    return new_func

def test_wos_statistics():
    docs_df_path = 'tests/wos_docs_df.csv'
    refs_df_path = 'tests/wos_refs_df.csv'
    citing_relation_df_path = 'tests/wos_citing_relation_df.csv'
    author_df, keywords_df = test_statistics(docs_df_path, refs_df_path, citing_relation_df_path, 'wos')()
    assert isinstance(author_df.index[0],str)
    assert isinstance(keywords_df.index[0],str)

def test_cssci_statistics():
    docs_df_path = 'tests/cssci_docs_df.csv'
    refs_df_path = 'tests/cssci_refs_df.csv'
    citing_relation_df_path = 'tests/cssci_citing_relation_df.csv'
    author_df, keywords_df = test_statistics(docs_df_path, refs_df_path, citing_relation_df_path, 'cssci')()
    assert isinstance(author_df.index[0],str)
    assert isinstance(keywords_df.index[0],str)

def test_scopus_statistics():
    docs_df_path = 'tests/scopus_docs_df.csv'
    refs_df_path = 'tests/scopus_refs_df.csv'
    citing_relation_df_path = 'tests/scopus_citing_relation_df.csv'
    author_df, keywords_df = test_statistics(docs_df_path, refs_df_path, citing_relation_df_path, 'scopus')()
    assert isinstance(author_df.index[0],str)
    assert isinstance(keywords_df.index[0],str)