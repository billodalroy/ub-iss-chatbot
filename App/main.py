import streamlit as st
from llama_engine import get_together_query_engine

st.set_page_config(
    page_title="Ask UB-International Student Services (ISS)",
    page_icon="🔍",
    layout="wide",
)

st.header("🔍 Ask UB-International Student Services (ISS)", divider='grey')
st.markdown("#### Get answers to your all your queries as an international\
             student at UB")

col1, col2 = st.columns(2)
col1.markdown("### Ask your query")
col2.markdown("### What can you ask?")
col3, col4, col5 = col2.columns(3)


st.session_state["query_engine"] = get_together_query_engine()
st.session_state["input"] = ''

suggested_texts = [
    "What is OPT and CPT?",
    "How do I apply for OPT?",
    "How do I apply for CPT?",
    "How do I apply for F-1 Visa?",
    "How do I apply for F-2 Visa?",
    "How to file my taxes?",
]
if col3.button(suggested_texts[0]):
    st.session_state.input = suggested_texts[0]

if col4.button(suggested_texts[1]):
    st.session_state.input = suggested_texts[1]

if col5.button(suggested_texts[2]):
    st.session_state.input = suggested_texts[2]

if col3.button(suggested_texts[3]):
    st.session_state.input = suggested_texts[3]

if col4.button(suggested_texts[4]):
    st.session_state.input = suggested_texts[4]

if col5.button(suggested_texts[5]):
    st.session_state.input = suggested_texts[5]


if prompt := col1.text_input("Enter your query", key='input'):
    with st.spinner("Searching..."):
        response = st.session_state['query_engine'].query(prompt)
    col1.markdown(f"{response}")

else:
    st.text("Type your query above or Select a template prompt")

footer = """
<style>
.footer {
# position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a href="https://www.linkedin.com/in/billodalroy">\
    Billodal Roy</a></p>
<p>This is an independent project and is not affiliated with the State \
    University of New York at Buffalo</p>
<p>This chatbot does not provide legal advice. Please contact your school's \
    International Student Advisor for advice.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
