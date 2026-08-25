num=int(input("enter a number to check if it is a prime number: "))
if num==1:
	print(num,"not a prime number")
else:
	for x in range(2,num):
		if num%x==0:
			print("not a prime number")
			break
	else:
		print(num,"is a prime number")