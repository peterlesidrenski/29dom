input_text = input()
trimmed_text = input_text[3:]
lower_text = trimmed_text.lower()
count_i = lower_text.count('и')
print(f"{lower_text}, и = {count_i}")
