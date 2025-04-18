import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = input("Amount of password to generate: ")
number = int(number)

lenght = input("Password lenght: ")
lenght = int(lenght)

print("\nHere are your passwords: ")

for password in range(number):
  passwords = ""
  for nest in range(lenght):
    passwords += random.choice(chars)
  print(passwords)