import random

num = random.randint(1, 6)
guess = None

while guess != num:
  guess = input("guess a number between 1 and 6: ")
  guess = int(guess)

  if guess == num:
    print("congratulations! you won!")
    break
  else:
        print("bruh, the number was", num)