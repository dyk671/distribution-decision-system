import streamlit as st

st.set_page_config(
    page_title="配电线路缺陷识别与辅助决策系统",
    page_icon="⚡",
    layout="wide",
)

st.title("配电线路缺陷识别与辅助决策系统")
st.markdown(
    """
    本系统为硕士论文演示原型，采用 Streamlit 多页面结构，当前版本使用 Mock 数据贯通全流程。

    请从左侧导航栏进入以下功能页面：
    - 首页（系统总览）
    - 巡检图像缺陷识别
    - 缺陷辅助决策
    - 人工问答
    - 知识图谱可视化
    """
)

st.info("建议先查看“1_首页”，再按业务流程逐页体验。")
