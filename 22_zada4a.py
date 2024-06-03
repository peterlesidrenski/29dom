input_text = input()
trimmed_text = input_text[:-2]
lower_text = trimmed_text.lower()
is_digit = lower_text.isdigit()
print(f"{lower_text}, {is_digit}")
