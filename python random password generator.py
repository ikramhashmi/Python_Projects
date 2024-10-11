import random
import string
print("Welcome to password generator")
def main():
    length = int(input("Enter the length to generate password:"))
    upper = string.ascii_uppercase
    lower=string.ascii_lowercase
    charaters=string.punctuation
    digits=string.digits
    combine=length+upper+lower+charaters+digits
    a=random.sample(combine,length)
    print(a)
