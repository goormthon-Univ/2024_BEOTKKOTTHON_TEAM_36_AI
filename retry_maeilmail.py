from openai import OpenAI
client = OpenAI()


instruction = """
Objective:
When users provide information about a specific part of an Korean email (such as the title, greeting, body, or closing), generate three different forms of Korean content appropriate for that part based on the provided information. 
If there is information that the user has not provided, use the placeholder "[  additional content  ]".

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

Example:
Input:
email_part: body
email_part: closing
sender: 윤도윤
sender_info: 로봇공학과 20210423
receiver: 장하윤 
receiver_info: 교수님 
purpose: 대학원 진학 면담 요청


Output:
(version1)
환절기에 감기 조심하시고 항상 건강하시길 기원합니다. 바쁘신 와중에도 시간 내주셔서 감사합니다. 

윤도윤 올림

(version2)
교수님께서 가능하신 날짜에 꼭 대학원 진학과 관련하여 면담을 하고 싶습니다. 소중한 시간 내어 제 메일을 읽어주셔서 감사합니다. 

윤도윤 올림

(version3)
끝으로 항상 훌륭한 강의 제공해주셔서 감사합니다.
좋은 하루 보내시길 바라겠습니다.

20210423 윤도윤 드림
"""


response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:mongkey::95egk0CO",
  messages=[
    { "role": "system", "content": instruction },
    { "role": "user", "content": """email_part: closing 
sender: 강은지
sender_info: 인공지능학과 20209342
receiver: 최윤서 
receiver_info: 교수님 
purpose: 시험 일정 문의
    """ }]
)

print(response.choices[0].message.content.strip())