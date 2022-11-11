import random
guess = int(input("Guess a number b/w 1-100 :-"))
print(guess)
a = random.randint(1, 100)
# print(a)
if guess > a:
    print(f"your guessed number is greater than random's number {a}")
elif guess < a:
    print(f"your guessed number is less than random's number {a}")
else:
    print("you guessed a correct number ")
