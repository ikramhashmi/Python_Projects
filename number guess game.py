# [x]Random Number Generate ==> number variable
# [x] User inut number ==>user number variable 
# [] if user_input == number ==> You won 


import random 

number = random.randint(0, 9)
print(number)

while True:
    user_number = int(input('Enter Number: '))

    if user_number == number:
        print('You Won')
        break
    else:
        print('Try Again')
        continue