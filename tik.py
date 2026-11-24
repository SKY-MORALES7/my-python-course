import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = [13225]

tokens = enc.decode(text)

print(tokens)