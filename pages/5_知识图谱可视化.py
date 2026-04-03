import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph

from services.graph_service import get_graph_data

st.set_page_config(page_title="知识图谱可视化", page_icon="🕸️", layout="wide")

st.title("知识图谱可视化")
st.caption("用于演示设备、部件、缺陷、原因、措施等实体关系的可视化浏览。")

graph = get_graph_data(use_mock=True)
nodes_data = graph["nodes"]
edges_data = graph["edges"]

left, right = st.columns([2.2, 1])

with right:
    st.markdown("### 信息侧栏")
    keyword = st.text_input("节点搜索", placeholder="输入关键字，如：绝缘子、污闪")

if keyword.strip():
    filtered_nodes = [n for n in nodes_data if keyword.strip() in n["id"] or keyword.strip() in n["desc"]]
else:
    filtered_nodes = nodes_data

node_ids = {n["id"] for n in filtered_nodes}
filtered_edges = [e for e in edges_data if e[0] in node_ids or e[1] in node_ids]

color_map = {
    "设备": "#4F81BD",
    "部件": "#9BBB59",
    "缺陷": "#C0504D",
    "现象": "#F79646",
    "原因": "#8064A2",
    "措施": "#4BACC6",
}

nodes = [
    Node(id=n["id"], label=n["id"], size=18, color=color_map.get(n["type"], "#999999"))
    for n in filtered_nodes
]
edges = [Edge(source=s, target=t, label=l) for s, t, l in filtered_edges]

with left:
    st.markdown("### 图谱主展示区")
    config = Config(width="100%", height=560, directed=True, physics=True, hierarchical=False)
    selected = agraph(nodes=nodes, edges=edges, config=config)

with right:
    st.markdown("### 节点属性")
    if selected:
        node_info = next((n for n in nodes_data if n["id"] == selected), None)
        if node_info:
            st.json(node_info)
    else:
        st.info("点击左侧节点后显示属性。")

    st.markdown("### 局部关系说明")
    if selected:
        related = [e for e in edges_data if e[0] == selected or e[1] == selected]
        if related:
            with st.container(border=True):
                for s, t, l in related:
                    st.write(f"- {s} --[{l}]--> {t}")
        else:
            st.write("当前节点无局部关系。")
    else:
        st.info("点击左侧节点后显示局部关系路径。")
