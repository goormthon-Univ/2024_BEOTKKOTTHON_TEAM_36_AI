from openai import OpenAI
client = OpenAI()


instruction = """
SYSTEM:
You are Korean Mail text generator AI for college students based on input information ‘sender, sender_info, receiver, receiver_info, purpose’
- You definitely divide it into (title), (greeting), (body), and (closing).
- Your text should always be polite.
- If you need to include specific information other than the input information, you have to write it in the form of [  additional information  ].
"""


response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:mongkey::94UsemHJ",
  messages=[
    { "role": "system", "content": instruction },
    { "role": "user", "content": """      
      sender: 강연수
      sender_info: 컴퓨터공학과 2071003 
      receiver: 이민수 
      receiver_info: 교수님 
      purpose: 면담 요청
    """ }]
)

print(response.choices[0].message.content.strip())