import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in .env")

llm = ChatGroq(
    model= "llama-3.3-70b-versatile",
    temperature= 0.7
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "{question}")
    ]
)
parser = StrOutputParser()


chain = prompt | llm | parser

print("The Chatbot has started, and to exit conversation type 'exit' or 'quit'. " )

def get_response(question: str) -> str:
    try:
        response = chain.invoke({
            "question": question
        })

        return f"Bot: {response}\n"

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":

    print(
        "The Chatbot has started, and to exit conversation type 'exit' or 'quit'."
    )

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("GoodBye")
            break

        print(
            f"Bot: {get_response(question)}\n"
        )