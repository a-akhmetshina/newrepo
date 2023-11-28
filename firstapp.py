import streamlit as st
pip install openai streamlit



st.sidebar.header("Chatbot Settings")
openai_api_key = st.sidebar.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value='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')

st.title("💬 Chatbot")

# if "messages" not in st.session_state:
st.session_state["text"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state["text"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
