input_text = input()
replaced_text = input_text.replace('т', 'д')
count_d = replaced_text.count('д')
is_lower = replaced_text.islower()
print(f"{replaced_text}, д = {count_d}, {is_lower}")
