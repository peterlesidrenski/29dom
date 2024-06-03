input_text = input()
reversed_text = input_text[::-1]
lower_text = reversed_text.lower()
count_a = lower_text.count('а')
print(f"{lower_text}, а = {count_a}")
