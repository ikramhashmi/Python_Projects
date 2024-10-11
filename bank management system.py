import string
import random
import pyfiglet as pg
text= "python bank"
new_text=pg.figlet_format(text)
print(new_text)


res = ''.join(random.choices(string.ascii_letters,k=7))

def depsoite(total_amount):
   
    amount=int(input("Enter amount to deposite:\n"))
    if amount>0:
        total_amount+=amount
        print(f"your amount despoited successfully")
        print(f"your accoount balance=${total_amount}")
    else:
       print("Amount must be greater than 0") 
    return total_amount

def withdrawal(total_amount):
    amount=int(input("Enter amount to withdraw:\n"))
    if amount<total_amount:
        total_amount-=amount
        print(f"your amount withdrawl successfully")
        print(f"your accoount balance=${total_amount}")
    else:
        print("insufficient Balance")
    return total_amount   

def sign_up(usernames,passwords):
    user_name= input("Enter your name\n")
    password = input("Enter your password\n")
    usernames.append(user_name)
    passwords.append(password)
    return user_name,password
  
def login(usernames,passwords):
     user_name= input("Enter your name\n")
     password = input("Enter your password\n")
     if user_name in usernames and password in passwords:
        print("----Account Details----")
        print(f"Account Holder Name:{user_name}")
        print(f"Account number:{str(res)}")
        total_amount=0
        while True:
            print("1:Deposite")
            print("2:Withdraw")
            print("3:Exit")
            choice =input("Choose an option")
            if choice == "1":
                total_amount=depsoite(total_amount) 
                continue

            elif choice=="2":
                total_amount=withdrawal(total_amount)
                continue
            elif choice=="3":
                break
            else:
                print("Wrong input")
     else:
        print("Name and password did'nt match Try again!")

def main():
    
    usernames=[]
    passwords=[]
    while True:
        print("1:Sign Up")
        print("2:Login")
        print("3:Exit")
        option = input("Choose an option=\n")
        if option == "1":
            sign_up(usernames,passwords)
            continue
        elif option =="2":
            login(usernames,passwords)
            print("Login sucessful")
            continue
        elif option=="3":
            break 
            print("Thanks for using python bank")
        else:
            print("Invalid input")

main()    