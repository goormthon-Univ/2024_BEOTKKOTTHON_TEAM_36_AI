import tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
print(f"Prompt 길이: {len(encoding.encode(instruction))}")