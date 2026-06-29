import os
from dotenv import load_dotenv
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

# Load API Key

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit Config

st.set_page_config(
    page_title="Enterprise AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# CSS

st.markdown("""
<style>

.main{
    background:#f7f9fc;
}

h1{
    color:#0056b3;
}

.stChatMessage{
    border-radius:12px;
    padding:12px;
    margin-bottom:10px;
    box-shadow:0px 3px 8px rgba(0,0,0,.10);
}

.stButton>button{
    width:100%;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    session_id = st.text_input(
        "Session ID",
        value="session_1"
    )

    model_name = st.selectbox(
        "Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ]
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.3
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "French",
            "Spanish"
        ]
    )

    st.markdown("---")

    clear = st.button("🗑 Clear Chat")

# Title

st.title("🤖 Enterprise AI Conversation Chatbot")

st.caption("Powered by LangChain + Groq + Streamlit")


# Session State


if "messages" not in st.session_state:
    st.session_state.messages = []

if clear:
    st.session_state.messages = []

# Display Previous Messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Prompt Template

prompt = ChatPromptTemplate.from_messages(

[
(
"system",

"""
You are an intelligent AI assistant.

Rules:

1. Reply professionally.
2. Explain step-by-step.
3. Give examples whenever needed.
4. Reply in {language}.
5. Use tables whenever useful.
6. If code is requested, generate complete code with comments.
7. Format answers beautifully using Markdown.

"""
),

MessagesPlaceholder(variable_name="messages")

]
)

# LLM

llm = ChatGroq(

model=model_name,

temperature=temperature,

api_key=groq_api_key

)

chain = prompt | llm | StrOutputParser()

# Memory

store = {}

def get_session_history(session):

    if session not in store:

        store[session] = InMemoryChatMessageHistory()

    return store[session]

conversation = RunnableWithMessageHistory(

chain,

get_session_history,

input_messages_key="messages"

)

# User Input

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        response = conversation.invoke(

            {
                "messages":[
                    ("human",user_input)
                ],

                "language":language
            },

            config={

                "configurable":{

                    "session_id":session_id

                }

            }

        )

        placeholder.markdown(response)

    st.session_state.messages.append(

        {

            "role":"assistant",

            "content":response

        }

    )

# Download Chat

st.divider()

history = ""

for msg in st.session_state.messages:

    history += f"{msg['role'].upper()}:\n"

    history += msg["content"]

    history += "\n\n"

st.download_button(

label="📥 Download Conversation",

data=history,

file_name="conversation.txt",

mime="text/plain"

)