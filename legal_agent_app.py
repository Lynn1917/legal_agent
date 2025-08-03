import streamlit as st
from scripts.query import ask

st.set_page_config(page_title="劳动法智能问答", page_icon="⚖️")
st.title("⚖️ 劳动法智能问答助手")
st.markdown("请输入你的劳动法问题，比如：**试用期最长可以多久？**")

question = st.text_input("🗣️ 问题", "")

if question:
    with st.spinner("思考中..."):
        answer = ask(question)
    st.success("✅ 回答如下：")
    st.write(answer)
