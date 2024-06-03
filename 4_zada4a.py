# Входен текст
input_text = input()
words = input_text.split()
joined_text = "_".join(words)
is_lower = joined_text.islower()
print(f"{joined_text}, {is_lower}")
