from langchain_openai import chat_OpenAI
from dotenv import load_dotenv

load_dotenv()

model = chat_OpenAI(model="gpt-4", temperature=0, max_completions_tokens=100)

result = model.invoke("what is the capital of bangladesh?")

print(result.choice[0].message.content)