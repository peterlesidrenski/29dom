input_text = input()
trimmed_text = input_text[:-3]
reversed_text = trimmed_text[::-1]
is_digit = reversed_text.isdigit()
print(f"{reversed_text}, {is_digit}")
