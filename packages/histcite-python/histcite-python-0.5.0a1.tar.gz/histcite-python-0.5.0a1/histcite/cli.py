import os
import argparse
from histcite.read_file import ReadFile
from histcite.process_file import ProcessFile
from histcite.compute_metrics import ComputeMetrics
from histcite.network_graph import GraphViz


def main():
    parser = argparse.ArgumentParser(description='A Python interface for histcite.')
    parser.add_argument('-f','--folder_path', type=str, required=True, help='Folder path of literature metadata.')
    parser.add_argument('-t','--source_type', type=str, required=True, choices=['wos','cssci','scopus'], help='Source type of literature metadata.')
    parser.add_argument('-n','--node_num', type=int, default=50, help='N nodes with the highest LCS.')
    # parser.add_argument('-g','--graph', action="store_true", help='generate graph file only')
    args = parser.parse_args()

    # 将结果存放在用户指定的folder_path下的result文件夹中
    output_path = os.path.join(args.folder_path, 'result')
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    docs_df = ReadFile(args.folder_path, args.source_type).read_all()
    process = ProcessFile(docs_df, args.source_type)
    process.extract_reference()
    citing_relation_df, refs_df = process.process_citation()

    cm = ComputeMetrics(docs_df, citing_relation_df, refs_df, args.source_type)
    cm_output_path = os.path.join(output_path, 'descriptive_statistics.xlsx')
    cm.write2excel(cm_output_path)
    
    doc_indices = citing_relation_df[citing_relation_df['LCS']>0].sort_values('LCS', ascending=False).index[:args.node_num]
    graph = GraphViz(docs_df, citing_relation_df, args.source_type)

    # 生成图文件
    graph_dot_file = graph.generate_dot_file(doc_indices)
    graph_dot_path = os.path.join(output_path, 'graph.dot')
    with open(graph_dot_path, 'w') as f:
        f.write(graph_dot_file)

    # 生成图节点文件
    graph._export_graph_node_file(os.path.join(output_path, 'graph_node_info.xlsx'))