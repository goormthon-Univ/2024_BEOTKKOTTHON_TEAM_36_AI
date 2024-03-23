from openai import OpenAI
client = OpenAI()


instruction = """
Objective:
When users provide information about a specific part of an Korean email (such as the title, greeting, body, or closing), generate three different forms of Korean content appropriate for that part based on the provided information. If there is information that the user has not provided, use the placeholder "[  additional content  ]".

Data Structure:
email_part: Specifies the part of the email (e.g., title, greeting, body, closing)
sender: Name of the sender
sender_info: Additional information about the sender (e.g., department, student ID)
receiver: Name of the receiver
receiver_info: Additional information about the receiver (e.g., position, department)
purpose: Purpose of writing the email

Working Guidelines:
The email part is one of below four(title, greeting, body, closing)
Each part has the main contents to deliver and should not be duplicated for each part.
- title: The title must be concise and clear and include the purpose of the email 
- greeting: greeting must include the sender's self-introduction, including student number and name.
- body: You create the text according to the purpose of the email. Yopu should write as politely as possible and put the reciever's intention first. You Don't need self introduction 
- closing:  You should include a thank you at the end. And You must match the format of the sender's name 드림 or sender's name 올림.

Output must be in the format of (version1), (version2), (version3).
For each part, create content in three different styles or expressions. 
YOU NEVER write the infomation that you don't provided.  if you need it, use the placeholder "[  추가 정보  ]".
"""


response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:mongkey::95fR8eq5",
  messages=[
    { "role": "system", "content": instruction },
    { "role": "user", "content": """
     email_part: body 
sender: 강은지
sender_info: 인공지능학과 20209342
receiver: 최윤서 
receiver_info: 교수님 
purpose: 대학원 진학 관련 문의

    """ }]
)

print(response.choices[0].message.content.strip())