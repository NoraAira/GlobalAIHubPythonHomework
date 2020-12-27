import random as rnd
import sys

name = input("Please enter your name: ")
print(f"Welcome {name}, this is a secret number game. Please guess the secret number.")
secret = rnd.randint(1,100)

check = False

for x in range(5):
  guess = int(input("Please enter your number: "))
  if guess == secret:
    print("You WIN")
    check = True
    break
  elif guess < secret:
    print("Please enter a greater number!!")
  else:
    print("Please enter a smaller number!!")

if not check:
  sys.exit(f"You LOSE {secret}")