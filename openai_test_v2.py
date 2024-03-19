import os
import openai
from openai import OpenAI

client = OpenAI()

openai.api_key = os.getenv("OPENAI_API_KEY")

instruction = ""
question = "교수님께 면담 요청하는 메일 작성해줘"
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    { "role": "system", "content": instruction },
    { "role": "user", "content": question}
  ]
)

print(response.choices[0].message.content.strip())