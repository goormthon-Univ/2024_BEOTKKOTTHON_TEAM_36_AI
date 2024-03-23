from openai import OpenAI
client = OpenAI()


fine_tuning = client.fine_tuning.jobs.create(
  training_file="file-BHP45WDvx9vkZhkxeO6jxuYl", 
  model="gpt-3.5-turbo-1106"
)

print(fine_tuning)