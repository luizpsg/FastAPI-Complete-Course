##Variables

cost = 10

print (cost)

print (10 + (10 * .25))

tax_percent = .25
tax = cost * tax_percent
price = cost + tax

print (price)

username = "Coding With Luiz"
first_name = "Luiz"

print (username + " " + first_name)

first_num = 10
second_num = 2
print(first_num)
print(second_num)

# Write a Python program that can do the following:

# - You have $50

# - You buy an item that is $15, that has a 3% tax

# - Using the print()  Print how much money you have left, after purchasing the item.


myMoney = 50
item = 15
tax = .03
taxedItem = item * tax + item
leftOver = myMoney - taxedItem
print (leftOver)


#String Formatting
first_name = "Luiz"
last_name =  "Gonçalves"

print (f"Hello, my name is {first_name} {last_name}")

sentence = "Hello, my name is {} {}"
print (sentence.format(first_name, last_name))

print(f"Hello, my name is {first_name} {last_name.upper()} I hope you are doing well")