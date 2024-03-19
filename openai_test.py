import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
    model = "gpt-3.5-turbo-instruct", 
    prompt = "내 이름은 철수야? \n\n Q: 내 이름이 뭘까?",
    temperature = 0,
    max_tokens=100,
    top_p=1,
    frequency_penalty = 0.0,
    presence_penalty = 0.0,
    stop=["\n"]

)

print(response)


print(response.choices[0].text.strip())