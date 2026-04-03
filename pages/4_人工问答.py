import streamlit as st

from services.qa_service import answer_question, get_example_questions

st.set_page_config(page_title="人工问答", page_icon="💬", layout="wide")
st.title("人工问答")
st.caption("当前为 Mock 问答流程，后续可接入知识增强检索与真实 LLM 推理。")

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

st.markdown("### 示例问题")
example_questions = get_example_questions()
cols = st.columns(len(example_questions))
for idx, q in enumerate(example_questions):
    with cols[idx]:
        if st.button(q, use_container_width=True):
            st.session_state["qa_input"] = q

question = st.text_input("请输入问题", key="qa_input", placeholder="例如：绝缘子污闪有哪些常见诱因？")

if st.button("提交问题", type="primary") and question.strip():
    result = answer_question(question, use_mock=True)
    st.session_state.qa_history.append(
        {
            "question": question.strip(),
            "answer": result["answer"],
            "evidence": result["evidence"],
        }
    )

if st.session_state.qa_history:
    st.markdown("### 问答结果与历史")
    for idx, item in enumerate(reversed(st.session_state.qa_history), 1):
        with st.container(border=True):
            st.write(f"**Q{idx}：**{item['question']}")
            st.write(f"**回答：**{item['answer']}")
            st.caption(f"证据来源：{item['evidence']}")
else:
    st.info("请先输入问题或点击示例问题开始问答。")
