input_text = input()
lower_text = input_text.lower()
count_o = lower_text.count('о')
starts_with_n = lower_text.startswith('н')
print(f"{lower_text}, о = {count_o}, {starts_with_n}")
