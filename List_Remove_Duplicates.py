def remove_duplicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(list))