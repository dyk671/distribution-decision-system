import streamlit as st

from services.qa_service import answer_question, get_example_questions

st.set_page_config(page_title="人工问答", page_icon="💬", layout="wide")

st.title("人工问答")
st.caption("用于演示自然语言问答、证据路径展示与会话历史记录。")

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []
if "qa_current" not in st.session_state:
    st.session_state.qa_current = None

st.markdown("### 输入区")
input_col, btn_col = st.columns([4, 1])
with input_col:
    question = st.text_input("请输入问题", key="qa_input", placeholder="例如：绝缘子污闪有哪些常见诱因？")
with btn_col:
    submit = st.button("提交问题", type="primary", use_container_width=True)

st.markdown("#### 示例问题")
example_cols = st.columns(3)
for idx, q in enumerate(get_example_questions()):
    with example_cols[idx % 3]:
        if st.button(q, key=f"example_{idx}", use_container_width=True):
            st.session_state["qa_input"] = q
            question = q
            submit = True

if submit and question.strip():
    result = answer_question(question, use_mock=True)
    current_item = {
        "question": question.strip(),
        "answer": result["answer"],
        "evidence": result["evidence"],
    }
    st.session_state.qa_current = current_item
    st.session_state.qa_history.append(current_item)

st.markdown("### 回答展示区")
if st.session_state.qa_current:
    with st.container(border=True):
        st.write(f"**当前问题：**{st.session_state.qa_current['question']}")
        st.write(f"**回答内容：**{st.session_state.qa_current['answer']}")
else:
    st.info("提交问题后将在此显示当前回答。")

st.markdown("### 证据来源区")
if st.session_state.qa_current:
    with st.container(border=True):
        st.caption(st.session_state.qa_current["evidence"])
else:
    st.info("提交问题后将在此显示对应证据路径。")

st.markdown("### 历史记录区")
if st.session_state.qa_history:
    with st.expander("展开查看历史问答", expanded=True):
        for idx, item in enumerate(reversed(st.session_state.qa_history), 1):
            with st.container(border=True):
                st.write(f"**第 {idx} 条**｜{item['question']}")
                st.write(item["answer"])
                st.caption(item["evidence"])
else:
    st.info("暂无历史记录。")
