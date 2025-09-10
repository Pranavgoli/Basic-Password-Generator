import random as r

print("Welcome to the Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+~=-{}|[]:;?><,./"

number = int(input("Enter number of passwords u want to generate: "))

length = int(input("Enter the length of password you want: "))

print("\nHere are your passwords:")

for pwd in range(number):
    passwords = ''
    for ch in range(length):
        passwords = passwords + r.choice(chars)
    print(passwords)
    
    if length < 6:
        print("Password is weak")
    elif 6 <= length < 10:
        print("Password is medium")
    else:
        print("Password is strong")

if number > 10:
    print("You should not generate more than 10 passwords at a time for security reasons.")
else:
    print("Generate more passwords if needed.")
