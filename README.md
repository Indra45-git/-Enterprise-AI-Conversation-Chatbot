# 🤖 Enterprise AI Conversation Chatbot

An AI-powered conversational chatbot built using **Streamlit**, **LangChain**, and **Groq LLMs**. The application provides a modern chat interface with conversation memory, multiple language support, customizable AI models, downloadable chat history, and session-based conversations.

---

## 🚀 Features

* 💬 Interactive AI chat interface
* 🧠 Conversation memory using LangChain
* 🔄 Session-based chat history
* 🌍 Multi-language responses

  * English
  * Hindi
  * French
  * Spanish
* 🤖 Multiple Groq LLM selection
* 🎛 Adjustable temperature control
* 📥 Download complete conversation
* 🗑 Clear chat functionality
* 📱 Responsive Streamlit UI
* 🎨 Modern custom CSS styling

---

## 🛠 Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Programming Language            |
| Streamlit     | Web Interface                   |
| LangChain     | LLM Framework                   |
| Groq API      | Large Language Model            |
| python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```text
Enterprise-AI-Chatbot/
│
├── app.py                 # Main Streamlit application
├── .env                   # Groq API Key (Not uploaded to GitHub)
├── requirements.txt       # Project dependencies
├── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Indra45-git/Enterprise-AI-Chatbot.git

cd Enterprise-AI-Chatbot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from:

https://console.groq.com/keys

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will automatically open in your browser.

---

## 🧠 Supported Models

* llama-3.3-70b-versatile
* llama-3.1-8b-instant

---

## 🌍 Supported Languages

* English
* Hindi
* French
* Spanish

---

## 💡 How It Works

1. User enters a question.
2. LangChain formats the prompt.
3. Conversation history is stored using `InMemoryChatMessageHistory`.
4. Request is sent to Groq LLM.
5. AI generates a response.
6. Response is displayed in the Streamlit interface.
7. Entire conversation can be downloaded as a text file.

---
