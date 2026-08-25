def reverse_string(s):
    words = s.split()
    print(" ".join(words[::-1]))


text = input("Enter a sentence: ")
reverse_string(text)

