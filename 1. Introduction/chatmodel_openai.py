from pyexpat import model
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("What is the capital of Ukraine?")
print(response.content)
