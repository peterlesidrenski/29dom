input_text = input()
lower_text = input_text.lower()
count_o = lower_text.count('о')
is_alpha = lower_text.isalpha()
print(f"{lower_text}, о = {count_o}, {is_alpha}")
