text = input()
replace = text.replace("е", "и")
reverse = replace[::-1]
count = replace.count("и")
print(f"{reverse}, и = {count}")