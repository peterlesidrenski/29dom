input_text = input()
reversed_text = input_text[::-1]
replaced_text = reversed_text.replace('а', 'у')
starts_with_u = replaced_text.startswith('у')
print(f"{replaced_text}, {starts_with_u}")
