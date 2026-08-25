birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
}
 
print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)
 
lookup_name = input("Who's birthday do you want to look up? ")
 
if lookup_name in birthdays:
    print(f"{lookup_name}'s birthday is {birthdays[lookup_name]}.")
else:
    print(f"Sorry, we don't have {lookup_name}'s birthday.")