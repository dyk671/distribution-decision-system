import streamlit as st

from services.decision_service import get_decision_payload

st.set_page_config(page_title="缺陷辅助决策", page_icon="🧭", layout="wide")
st.title("缺陷辅助决策")
st.caption("当前为 Mock 决策流程，后续可接入 GraphRAG 与微调模型。")

payload = get_decision_payload(use_mock=True)
event = payload["event"]
paths = payload["paths"]
decision = payload["decision"]

st.markdown("### 缺陷事件信息")
c1, c2, c3 = st.columns(3)
c1.metric("缺陷类别", event["缺陷类别"])
c2.metric("关联部件", event["关联部件"])
c3.metric("风险等级", event["风险等级"])
st.write(f"**视觉证据：**{event['视觉证据']}")

st.markdown("### 知识路径")
st.write(f"- 现象路径：{paths['现象路径']}")
st.write(f"- 原因路径：{paths['原因路径']}")
st.write(f"- 措施路径：{paths['措施路径']}")

st.markdown("### 辅助决策结果")
st.warning(f"风险提示：{decision['风险提示']}")
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
st.code(export_text, language="text")
st.download_button(
    "导出决策结果.txt",
    data=export_text,
    file_name="mock_缺陷辅助决策结果.txt",
    mime="text/plain",
)
