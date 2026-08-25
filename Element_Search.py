def search(numbers, n):
    if n in numbers:
        return True
    else:
        return False
list1 = [1, 3, 5, 7, 9, 11, 13]
num = int(input("Enter a number you want to search: "))
print(search(list1, num))