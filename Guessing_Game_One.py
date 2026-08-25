import random
num = random.randint(1,9)
while True:
	guess= int(input("guess a number number between 1 to 9: "))
	if guess==num:
		print("guess is exactly right")
	elif guess>num:
		print("guess is high")
	else:
		print("guess is low")