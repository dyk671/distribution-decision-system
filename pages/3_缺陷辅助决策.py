import streamlit as st

from services.decision_service import get_decision_payload

st.set_page_config(page_title="缺陷辅助决策", page_icon="🧭", layout="wide")

st.markdown(
    """
    <style>
    .section-title {font-size: 1.1rem; font-weight: 600; color: #1f3b57; margin-top: 0.6rem;}
    .panel {background: #ffffff; border: 1px solid #d9e4ef; border-radius: 12px; padding: 12px 14px;}
    .risk-tag {display:inline-block; padding: 2px 10px; border-radius: 999px; background:#e8f0f8; color:#1f4e79; font-weight:600;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("缺陷辅助决策")
st.caption("单页连续展示：缺陷事件信息 → 缺陷知识路径 → 辅助决策结果")

payload = get_decision_payload(use_mock=True)
event = payload["event"]
paths = payload["paths"]
decision = payload["decision"]

st.markdown('<div class="section-title">一、缺陷事件信息</div>', unsafe_allow_html=True)
with st.container(border=True):
    m1, m2, m3 = st.columns(3)
    m1.metric("缺陷类别", event["缺陷类别"])
    m2.metric("关联部件", event["关联部件"])
    m3.markdown(f"<div style='margin-top:30px;'>风险等级：<span class='risk-tag'>{event['风险等级']}</span></div>", unsafe_allow_html=True)
    st.markdown("**视觉证据**")
    st.write(event["视觉证据"])

st.markdown('<div class="section-title">二、缺陷知识路径（决策依据）</div>', unsafe_allow_html=True)
path_cols = st.columns(3, gap="medium")
path_items = [
    ("现象路径", paths["现象路径"]),
    ("原因路径", paths["原因路径"]),
    ("措施路径", paths["措施路径"]),
]
for col, (title, content) in zip(path_cols, path_items):
    with col:
        st.markdown(f"""<div class='panel'><b>{title}</b><br><br>{content}</div>""", unsafe_allow_html=True)

st.markdown('<div class="section-title">三、辅助决策结果（结论输出）</div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("**风险提示**")
    st.warning(decision["风险提示"])
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

with st.expander("复制 / 导出结果", expanded=False):
    c1, c2 = st.columns([2, 1])
    with c1:
        st.code(export_text, language="text")
    with c2:
        st.download_button(
            "导出决策结果.txt",
            data=export_text,
            file_name="mock_缺陷辅助决策结果.txt",
            mime="text/plain",
            use_container_width=True,
        )
