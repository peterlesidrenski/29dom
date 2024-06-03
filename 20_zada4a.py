input_text = input()
count_i = input_text.count('и')
reversed_text = input_text[::-1]
starts_with_a = reversed_text.startswith('а')
print(f"{reversed_text}, и = {count_i}, {starts_with_a}")
