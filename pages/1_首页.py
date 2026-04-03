import streamlit as st

st.set_page_config(page_title="首页", page_icon="🏠", layout="wide")

st.markdown(
    """
    <style>
    .section-title {font-size: 1.15rem; font-weight: 600; color: #1f3b57; margin-top: 0.5rem;}
    .module-card {background: #ffffff; border: 1px solid #d9e4ef; border-radius: 12px; padding: 14px 16px; min-height: 118px;}
    .soft-panel {background: #ffffff; border: 1px solid #d9e4ef; border-radius: 12px; padding: 14px 16px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("配电线路缺陷识别与辅助决策系统")
st.caption("硕士论文展示原型｜缺陷识别、辅助决策、人工问答、知识图谱可视化一体化展示")
st.write("本页面作为系统总览，聚焦核心模块、业务流程与使用说明，便于论文截图与功能讲解。")

st.markdown('<div class="section-title">功能概览</div>', unsafe_allow_html=True)
modules = [
    ("巡检图像缺陷识别", "上传巡检图像，执行缺陷识别并展示检测框与结果表。"),
    ("缺陷辅助决策", "围绕缺陷事件与知识路径生成风险提示和处置建议。"),
    ("人工问答", "支持自然语言提问，展示回答结果与证据路径。"),
    ("知识图谱可视化", "展示设备-部件-缺陷-原因-措施关系网络。"),
]
cols = st.columns(4)
for col, (name, desc) in zip(cols, modules):
    with col:
        st.markdown(f'<div class="module-card"><b>{name}</b><br><br>{desc}</div>', unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="large")
with left:
    st.markdown('<div class="section-title">系统业务流程</div>', unsafe_allow_html=True)
    st.markdown(
        '''<div class="soft-panel">
        1. 巡检图像上传与缺陷识别<br>
        2. 缺陷事件抽取与风险等级展示<br>
        3. 知识路径支撑下的辅助决策生成<br>
        4. 人工问答核验知识依据<br>
        5. 图谱可视化追踪关联关系
        </div>''',
        unsafe_allow_html=True,
    )

with right:
    st.markdown('<div class="section-title">系统功能说明</div>', unsafe_allow_html=True)
    st.markdown(
        '''<div class="soft-panel">
        • 当前版本采用 Mock-first 方案，保证交互流程完整、页面稳定可演示。<br>
        • 页面与服务层分离，便于后续替换为 RT-DETR、GraphRAG、LLM、Neo4j 实际能力。<br>
        • 界面风格以简洁、规整、学术化为目标，适合论文截图。
        </div>''',
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title">使用提示与版本说明</div>', unsafe_allow_html=True)
st.markdown(
    '''<div class="soft-panel">
    使用提示：建议按“缺陷识别 → 辅助决策 → 人工问答 → 图谱可视化”顺序体验。<br>
    当前版本说明：页面数据均为 Mock 输出，用于演示系统结构与交互链路。
    </div>''',
    unsafe_allow_html=True,
)
