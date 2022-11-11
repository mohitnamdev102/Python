import random


# a = random.random()
# print(a)

# a = random.randint(1,100)
# print(a)

# a = random.randrange(5, 100, 10)
# print(a)

# a = "!@#$%%^wqetriuposadkjdfnmbxzcvmu"
# b = "".join(random.sample(a, 12))
# print(b)


num = random.randrange(1,100)
guess = 0

while True:
    a = int(input("Please enter a number: "))
    guess += 1

    if a == num:
        print("Correct")
        print("You took {} turns to get it right".format(guess))
        break

    elif a < num:
        print("You guessed low")

    else:
        print("You guessed high")
