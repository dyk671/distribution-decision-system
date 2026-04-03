import streamlit as st

from services.qa_service import answer_question, get_example_questions

st.set_page_config(page_title="人工问答", page_icon="💬", layout="wide")

st.markdown(
    """
    <style>
    .section-title {font-size: 1.1rem; font-weight: 600; color: #1f3b57; margin-top: 0.6rem;}
    .panel {background: #ffffff; border: 1px solid #d9e4ef; border-radius: 12px; padding: 12px 14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("人工问答")
st.caption("问题输入—回答展示—证据来源—历史记录的知识增强问答展示页面")

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []
if "qa_current" not in st.session_state:
    st.session_state.qa_current = None

st.markdown('<div class="section-title">一、输入区</div>', unsafe_allow_html=True)
with st.container(border=True):
    question = st.text_input("请输入问题", key="qa_input", placeholder="例如：绝缘子污闪有哪些常见诱因？")
    submit = st.button("提交问题", type="primary")

    with st.expander("示例问题（点击填充）", expanded=True):
        for idx, q in enumerate(get_example_questions()):
            if st.button(q, key=f"example_{idx}"):
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

st.markdown('<div class="section-title">二、回答展示区</div>', unsafe_allow_html=True)
if st.session_state.qa_current:
    st.markdown(
        f"""<div class='panel'>
        <b>当前问题：</b>{st.session_state.qa_current['question']}<br><br>
        <b>回答内容：</b>{st.session_state.qa_current['answer']}
        </div>""",
        unsafe_allow_html=True,
    )
else:
    st.info("提交问题后将在此显示当前回答。")

st.markdown('<div class="section-title">三、证据来源区</div>', unsafe_allow_html=True)
if st.session_state.qa_current:
    st.markdown(f"<div class='panel'>{st.session_state.qa_current['evidence']}</div>", unsafe_allow_html=True)
else:
    st.info("提交问题后将在此显示证据路径。")

st.markdown('<div class="section-title">四、历史记录区</div>', unsafe_allow_html=True)
if st.session_state.qa_history:
    with st.expander("展开查看历史问答", expanded=False):
        for idx, item in enumerate(reversed(st.session_state.qa_history), 1):
            with st.container(border=True):
                st.write(f"**第 {idx} 条问题：** {item['question']}")
                st.write(item["answer"])
                st.caption(item["evidence"])
else:
    st.info("暂无历史记录。")
