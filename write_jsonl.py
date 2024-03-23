import json
from collections import OrderedDict
from openai import OpenAI
client = OpenAI()

instruction = """
You are Korean Mail text generator AI for college students based on input information ‘sender, sender_info, receiver, receiver_info, purpose’
- You should divide it into (title), (greeting), (body), and (closing). You NEVER missing out any of these
- Your text should always be very polite.
- NEVER put in the fact of a user YOU DON'T KNOW. If you need to include specific information other than the input information, you have to write it in the form of [  additional information  ].

Each part(title, greeting, body, closing) has the main contents to deliver and should not be duplicated for each part.
- title: The title must be concise and clear and include the purpose of the email 
The title begins with [email purpose]. It is "purpose" of the input.
- greeting: greeting must include the sender's self-introduction, including student number and name.
- body: You create the text according to the purpose of the email. Yopu should write as politely as possible and put the reciever's intention first. You Don't need self introduction 
- closing:  You should include a thank you at the end. And You must match the format of the sender's name 드림 or sender's name 올림.
"""


data = [
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """sender: 김지수
sender_info: 환경공학과 20220341
receiver: 이다민 
receiver_info: 교수님 
purpose: 증원 요청 
"""}, 
              {"role": "assistant", "content": """(title)
[  과목명  ] 증원 관련 문의 드립니다. 시각디자인과 20220341 이유리

(greeting)
안녕하세요, 이다민 교수님.
저는 환경공학과에 재학중인 20220341 김지수입니다.

(body)
다름이 아니라, [  과목명  ] 수업과 관련하여 수강인원 증원이 가능할지 여쭙고 싶어 이렇게 메일 드립니다. 

교수님의 강의계획서를 보고 [  수업에서 다루는 것  ]에 대한 관심이 생겨 이번 학기 해당 과목을 수강함으로써 관련 분야에 대한 식견을 넓히고 싶습니다.

이를 위해 학년별 수강신청, 전체 수강신청 등 수강신청 기간 내내 교수님의 수업을 신청하기 위해 노력했지만 경쟁률이 너무 높아 수강신청에 모두 실패하였고, 이렇게 증원 예정이 있으신지 여쭙게 되었습니다. 

이미 많은 증원 요청 메일을 받으셨을 것이라고 생각하지만 수업이 절실한 학생들에게 기회를 주시면 정말 감사드리겠습니다. 

(closing)
바쁘신 와중에 메일 읽어주셔서 감사합니다. 

김지수 올림
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """sender: 김철수
sender_info: 휴먼바이오기계공학과 19학번 
receiver: 김민성 
receiver_info: 교수님 
purpose: 증원 요청 
"""}, 
              {"role": "assistant", "content": """(title)
[증원 요청] 휴먼바이오기계공학과 19학번 김철수입니다.
               
(greeting)
김민성 교수님, 안녕하세요.
저는 휴먼바이오기계공학과 19학번 신짱구입니다. 기온 변화가 심한 요즈음, 몸 건강히 잘 지내고 계신지요? 늘 건강하시기를 기원합니다. 
               
(body)
다름이 아니라, 이렇게 메일을 보내게 된 이유는 [  과목명  ] 수업 증원을 부탁드리기 위해서 입니다.  저는 [  과목명  ] 수업에 관심이 많아 이전부터 이번 학기에 꼭 수강하고 싶었습니다. 
수강 신청 내내 노력하였지만 모든 수업에 정원이 가득 차 실례인 줄 앎에도 불구하고 증원 요청을 드리고자 합니다. 

저는 [  과목명  ] 수업의 강의 내용 중  [  수업에서 다루는 것  ] 에 특히 관심이 많습니다. 교수님께서 기회를 주신다면 성실하고 열정적으로 수업에 참여할 준비가 되어있습니다. 이번 수업은 저의 진로에도 큰 도움이 될 것입니다. 또한, 교수님과 수업내용에 관하여 개인적으로 찾아뵙고 질문을 드려도 될 지 문의드립니다.
이번 학기 수강 인원 증원을 고려해 주실 수 있으실까요? 조심스럽지만 추후 수강인원을 늘릴 계획이 있으시다면 알려주시면 감사하겠습니다.
정중히 부탁드립니다.


(closing)
바쁘신데도 불구하고 메일을 읽어주셔서 감사합니다.
학교에서 늘 귀한 강의 들려 주시는 교수님께 감사드리며 더 많은 학생이 교수님의 수업을 들을 수 있기를 바랍니다. 건강하시기를 늘 소망합니다. 

감사합니다.

김철수 드림
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """sender: 박기호
sender_info: 경제학과 17학번
receiver: 정찬지
receiver_info: 교수님 
purpose: 미분적분학 증원 요청
"""}, 
              {"role": "assistant", "content": """(title
[미분적분학] 증원 가능 여부에 대해 메일드립니다. (경제학과 17학번 박기호)

(greeting)
안녕하세요, 정은지 교수님.
저는 경제학과에 재학 중인 17학번 박기호라고 합니다.

(body)
다름이 아니라 제가 연락을 드린 이유는 미분적분학에 대하여 교수님께 실례가 되지 않는다면 수강 정원을 조금만 더 증원해주실 수 있는지 문의를 드리기 위해서입니다.

저는 현재 [  관심 분야  ]에 많은 관심을 가지고 있고, 부족한 저의 안목을 더 키우기 위해 미분적분학 수업을 꼭 수강하여 심층적인 이해와 경험을 쌓아 저의 부족한 부분을 꼭 채우고 싶다는 마음이 있습니다. 

수강 신청에 실패한건 온전한 저의 잘못임을 인정하오나, 교수님께서 넓은 아량을 베푸셔서 증원을 해주실 수 있는지 양해를 구하고 싶습니다.

(closing)
미분적분학을 수강할 기회를 주신다면 최선을 다해 수강하겠습니다. 
바쁘신 와중에 긴 글 읽어주셔서 감사합니다.

박기호 올림
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """sender: 강은지
sender_info: 인공지능학과 20209342
receiver: 최윤서 
receiver_info: 교수님 
purpose: 대학원 진학 문의
"""}, 
              {"role": "assistant", "content": """(title)
[대학원] 교수님의 대학원 진학과 관련하여 면담 요청 드립니다. 

(greeting)
안녕하십니까 최윤서 교수님, 저는 인공지능학과에 재학 중인 20209342 강은지라고 합니다. 
개인적으로 [  과목명  ]과 관련하여 관심있는 분야가 생겼는데 이에 대한 대학원을 알아보던 중 교수님께 조언을 구하고자 연락드렸습니다

(body)
저는 현재 [  분야  ]에 흥미를 느껴 교수님의 [  과목명  ]을 수강하고 있습니다. 
특히 [  수업내용  ] 에 있어 관련 내용을 좀 더 공부해보고자 대학원에 진학을 할지 말지 선택을 해야하는 상황에 놓여져 있습니다. 
따라서 교수님과의 면담을 통해 이러한 저의 상황에 대해 조언을 구하고 방향성을 확고히 하고자 합니다.  
               
(closing)
결론적으로 대학원 진학에 있어 교수님과의 면담을 통해 확실하게 정하고 싶다는 말 전해드립니다. 
환절기에 감기 조심하시고 항상 건강하시길 기원합니다. 
바쁘신 와중에도 시간 내주셔서 감사합니다.
               
최윤서 올림
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """
"""}, 
              {"role": "assistant", "content": """
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """
"""}, 
              {"role": "assistant", "content": """
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """
"""}, 
              {"role": "assistant", "content": """
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """
"""}, 
              {"role": "assistant", "content": """
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """
"""}, 
              {"role": "assistant", "content": """
"""}]},
 {"messages": [{"role": "system", "content": instruction },
              {"role": "user", "content": """
"""}, 
              {"role": "assistant", "content": """
"""}]}
]

with open("train-v3.jsonl", "w", encoding="utf-8") as f:
  for dat in data:
    json.dump(dat, f, ensure_ascii=False) # ensure_ascii로 한글이 깨지지 않게 저장
    f.write("\n")

file = client.files.create(
  file=open("train-v2.jsonl", "rb"),
  purpose="fine-tune"
)

print(file)