import random
num = random.randint(1,100)
while True:
	guess= int(input("guess a number number between 1 to 100: "))
	if guess==num:
		print("guess is exactly right")
		break
	elif guess>num:
		print("guess is high")
	else:
		print("guess is low")