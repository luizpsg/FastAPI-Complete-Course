'''
User Input
'''

first_name = input("What is your first name? ")
print(f"Hello, {first_name}")

days = input("How many days until your birthday? ")
weeks = round(int(days) / 7, 2);

print(f"Your birthday is in {weeks} weeks");