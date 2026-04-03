import streamlit as st

st.set_page_config(page_title="首页", page_icon="🏠", layout="wide")

st.title("首页｜配电线路缺陷识别与辅助决策系统")
st.caption("面向硕士论文展示的原型系统总览页面（Mock-first）。")

st.markdown(
    "本系统集成巡检图像缺陷识别、缺陷辅助决策、人工问答和知识图谱可视化能力，用于展示完整业务流程与交互逻辑。"
)

st.markdown("### 功能概览")
card_cols = st.columns(4)
modules = [
    ("巡检图像缺陷识别", "上传图像并展示缺陷检测框及结果表格。"),
    ("缺陷辅助决策", "基于缺陷事件与知识路径生成处置建议。"),
    ("人工问答", "支持自然语言问题输入、证据路径与历史记录。"),
    ("知识图谱可视化", "展示实体关系网络并支持节点属性浏览。"),
]
for col, (title, desc) in zip(card_cols, modules):
    with col:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.write(desc)

left, right = st.columns([1, 1])
with left:
    st.markdown("### 系统业务流程")
    with st.container(border=True):
        st.markdown(
            """
            1. 上传巡检图像并执行缺陷识别  
            2. 查看缺陷事件及风险等级  
            3. 结合知识路径生成辅助决策  
            4. 在人工问答中进行知识增强问询  
            5. 在知识图谱页面追踪关联实体关系
            """
        )

with right:
    st.markdown("### 系统功能说明")
    with st.container(border=True):
        st.write("- 当前版本采用 Mock 数据，优先保证流程完整与界面可演示。")
        st.write("- 页面按论文截图场景优化，强调信息层次与可读性。")
        st.write("- 业务调用通过服务层统一封装，便于后续平滑替换真实模型。")

st.markdown("### 使用提示")
with st.container(border=True):
    st.write("建议按“缺陷识别 → 辅助决策 → 人工问答 → 图谱可视化”顺序体验。")
    st.write("当前版本说明：所有算法结果为 Mock 输出，用于系统结构与交互展示。")
