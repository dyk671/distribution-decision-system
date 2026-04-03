import streamlit as st

from services.graph_service import get_graph_data
from mock.mock_qa import EXAMPLE_QA

st.set_page_config(page_title="首页", page_icon="🏠", layout="wide")

st.title("首页｜系统总览")
st.subheader("配电线路缺陷识别与辅助决策系统")

st.markdown(
    "本系统用于硕士论文演示，集成**缺陷识别、辅助决策、人工问答、知识图谱可视化**四类能力，当前版本以 Mock 数据打通全流程。"
)

graph = get_graph_data(use_mock=True)
module_count = 5
mock_detection_count = 2
mock_graph_nodes = len(graph["nodes"])
mock_qa_count = len(EXAMPLE_QA)

c1, c2, c3, c4 = st.columns(4)
c1.metric("功能模块数", module_count)
c2.metric("Mock 识别结果条数", mock_detection_count)
c3.metric("Mock 图谱节点数", mock_graph_nodes)
c4.metric("示例问答条数", mock_qa_count)

st.markdown("### 模块导览")
st.info(
    """
    1. **巡检图像缺陷识别**：上传巡检图像，执行 Mock 检测并展示检测框与结果表格。
    2. **缺陷辅助决策**：查看缺陷事件、知识路径与辅助处置建议。
    3. **人工问答**：输入自然语言问题，获得知识增强回答并查看证据路径。
    4. **知识图谱可视化**：浏览设备-缺陷-原因-措施关系，支持节点检索与局部关系查看。
    """
)

st.markdown("### 使用建议")
st.write(
    "建议按“识别 → 决策 → 问答 → 图谱”的顺序体验，可获得完整业务流程截图，适合论文展示。"
)
