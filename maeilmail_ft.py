import json
from collections import OrderedDict
from openai import OpenAI
client = OpenAI()


with open("train.jsonl", "w", encoding="utf-8") as f:
  for dat in data:
    json.dump(dat, f, ensure_ascii=False) # ensure_ascii로 한글이 깨지지 않게 저장
    f.write("\n")

client.files.create(
  file=open("train.jsonl", "rb"),
  purpose="fine-tune"
)