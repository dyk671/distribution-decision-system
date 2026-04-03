import streamlit as st

from services.decision_service import get_decision_payload

st.set_page_config(page_title="缺陷辅助决策", page_icon="🧭", layout="wide")

st.title("缺陷辅助决策")
st.caption("用于演示缺陷事件、知识路径与辅助决策结果的分区展示。")

payload = get_decision_payload(use_mock=True)
event = payload["event"]
paths = payload["paths"]
decision = payload["decision"]

tab1, tab2, tab3 = st.tabs(["缺陷事件", "知识路径", "辅助决策结果"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("缺陷类别", event["缺陷类别"])
    c2.metric("关联部件", event["关联部件"])
    c3.metric("风险等级", event["风险等级"])
    with st.container(border=True):
        st.markdown("**视觉证据**")
        st.write(event["视觉证据"])

with tab2:
    col_l, col_r = st.columns(2)
    with col_l:
        with st.container(border=True):
            st.markdown("**现象路径**")
            st.write(paths["现象路径"])
        with st.container(border=True):
            st.markdown("**原因路径**")
            st.write(paths["原因路径"])
    with col_r:
        with st.container(border=True):
            st.markdown("**措施路径**")
            st.write(paths["措施路径"])

with tab3:
    with st.container(border=True):
        st.markdown("**风险提示**")
        st.warning(decision["风险提示"])

    with st.container(border=True):
        st.markdown("**处置建议**")
        for idx, suggestion in enumerate(decision["处置建议"], 1):
            st.write(f"{idx}. {suggestion}")

    st.caption(decision["说明信息"])

export_text = (
    "[缺陷辅助决策导出]\n"
    f"缺陷类别：{event['缺陷类别']}\n"
    f"关联部件：{event['关联部件']}\n"
    f"风险等级：{event['风险等级']}\n"
    f"视觉证据：{event['视觉证据']}\n\n"
    f"现象路径：{paths['现象路径']}\n"
    f"原因路径：{paths['原因路径']}\n"
    f"措施路径：{paths['措施路径']}\n\n"
    f"风险提示：{decision['风险提示']}\n"
    "处置建议：\n"
    + "\n".join([f"- {item}" for item in decision["处置建议"]])
)

st.markdown("### 复制 / 导出")
copy_col, download_col = st.columns([2, 1])
with copy_col:
    st.code(export_text, language="text")
with download_col:
    st.download_button(
        "导出决策结果.txt",
        data=export_text,
        file_name="mock_缺陷辅助决策结果.txt",
        mime="text/plain",
        use_container_width=True,
    )
