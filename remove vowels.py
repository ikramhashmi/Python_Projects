user_input = input("Enter your statement=")
vowels='aeiouAEIOU'
new_string = ""
for i in user_input:
    if i not in vowels:
        new_string +=i


print(new_string)