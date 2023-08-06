import pytest
import pandas as pd
from typing import Literal
from histcite.network_graph import GraphViz

@pytest.mark.skip(reason='This is a function factory')
def test_graph(docs_df_path: str, citing_relation_df_path: str, source_type: Literal['wos','cssci','scopus']):
    def new_func():
        docs_df = pd.read_csv(docs_df_path, dtype_backend='pyarrow')
        citing_relation_df = pd.read_csv(citing_relation_df_path, dtype_backend='pyarrow')
        doc_indices = citing_relation_df.sort_values('LCS', ascending=False).index[:10]
        G = GraphViz(docs_df, citing_relation_df, source_type)
        graph_dot_file = G.generate_dot_file(doc_indices)
        return graph_dot_file
    return new_func

def test_wos_graph():
    docs_df_path = 'tests/wos_docs_df.csv'
    citing_relation_df_path = 'tests/wos_citing_relation_df.csv'
    graph_dot_file = test_graph(docs_df_path, citing_relation_df_path, 'wos')()
    assert graph_dot_file[:7] == 'digraph'

def test_cssci_graph():
    docs_df_path = 'tests/cssci_docs_df.csv'
    citing_relation_df_path = 'tests/cssci_citing_relation_df.csv'
    graph_dot_file = test_graph(docs_df_path, citing_relation_df_path, 'cssci')()
    assert graph_dot_file[:7] == 'digraph'

def test_scopus_graph():
    docs_df_path = 'tests/scopus_docs_df.csv'
    citing_relation_df_path = 'tests/scopus_citing_relation_df.csv'
    graph_dot_file = test_graph(docs_df_path, citing_relation_df_path, 'scopus')()
    assert graph_dot_file[:7] == 'digraph'