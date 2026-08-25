size = int(input("What size game board do you want? "))
for row in range(size):
    print("---- " * size)
    print("|    " * size + "|")
print("---- " * size)