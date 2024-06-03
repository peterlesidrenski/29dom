input_text = input()
replaced_text = input_text.replace('и', 'е')
reversed_text = replaced_text[::-1]
ends_with_a = reversed_text.endswith('а')
print(f"{reversed_text}, {ends_with_a}")
