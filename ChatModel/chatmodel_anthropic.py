from langchain_anthropic import chat_Anthropic
from dotenv import load_dotenv

load_dotenv()

model = chat_Anthropic(model="claude-2", temperature=0, max_completions_tokens=10)
result = model.invoke("what is the capital of bangladesh?")

print(result.choice[0].message.content)
