import random
num = str(random.randint(1000, 9999))
guess = ""
count = 0
while guess != num:
    guess = input("Enter a 4-digit number: ")
    count = count + 1
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == num[i]:
            cows = cows + 1
        elif guess[i] in num:
            bulls = bulls + 1
    print("Cows =", cows)
    print("Bulls =", bulls)
print("You guessed the number!")
print("Total guesses =", count)