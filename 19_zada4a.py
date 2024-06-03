input_text = input()
upper_text = input_text.upper()
trimmed_text = upper_text[2:]
is_alpha = trimmed_text.isalpha()
print(f"{trimmed_text}, {is_alpha}")
