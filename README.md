LangChain Basic Chatbot

A simple AI chatbot built using LangChain, Groq, and Streamlit.

Features

* LangChain LCEL Chains
* Groq LLM Integration
* Streamlit User Interface
* Prompt Templates
* Output Parsers
* Environment Variable Management

Tech Stack

* Python
* LangChain
* Groq
* Streamlit
* python-dotenv

Project Structure

Langchain_ChatBot/
│
├── app.py
├── streamlit_app.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore

Installation

git clone <repository-url>
cd Langchain_ChatBot
uv sync

Run the Application

streamlit run streamlit_app.py

## Screenshots

### Home Page

![Home Page](screenshots/home_page.png)

### Chatbot Response

![Chatbot Response](screenshots/chatbot_response.png)

Future Improvements

* Conversation Memory
* Chat History
* RAG Integration
* Multi-Agent Workflows