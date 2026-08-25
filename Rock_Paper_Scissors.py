player1=input("player1 - Enter rock, paper ,scissor: ")
player2=input("player2 - Enter rock, paper ,scissor: ")

if player1==player2:
	print("match tie")

elif (player1 == "rock" and player2 == "paper"):
	print("player2 won")
elif(player1== "rock" and player2 == "scissor"):
	print("player1 won")
elif(player1== "paper" and player2== "rock"):
	print("player1 won")
elif(player1== "paper" and player2== "scissor"):
	print("player2 won")
elif(player1== "scissor" and player2== "rock"):
	print("player2 won")
elif(player1== "scissor" and player2== "paper"):
	print("player1 won")
		
else:
	print("invalid in input")