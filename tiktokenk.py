import tiktoken  # import the tokenizer library used by OpenAI model encodings

enc = tiktoken.encoding_for_model("gpt-4o")  # select the token encoding that matches the gpt-4o model
text = "Create a member named Chidi from Nigeria"  # the text we want to tokenize

tokens = enc.encode(text)  # convert the text into a list of token IDs

print(tokens)  # show the raw token IDs produced by the tokenizer
print(len(tokens))  # print how many tokens were produced
# The token count is 8 because the tokenizer splits the text into 8 encoded pieces.
# Tokenization is not the same as word count; some words or spaces can become separate tokens.


# "Nigeria" can have one ID.
# " Nigeria" (with a space) can have another ID.
# "nigeria" can become two tokens with two IDs.
# "Nigerian" might split differently again.
