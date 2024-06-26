#
# Functions
#

def my_function():
    print("Hello from my function!")

my_function()

def print_my_name(f_name, l_name):
    print(f"Hello, {f_name} {l_name}!")

print_my_name("Luiz", "Gonçalves")

def print_color_red():
    color = "red"
    print(f"The color is {color}")

color = "blue"
print(f"The color is {color}")

print_color_red()


def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

print_numbers(10, 5)
print_numbers(lowest_number=5, highest_number=10)

def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(5, 3)
print(result)

def print_list(list):
    for item in list:
        print(item)

num_list = [1, 2, 3, 4, 5]
print_list(num_list)

def buy_item(price):
    return price + add_tax(price)

def add_tax(price):
    return price * 0.07

total_price = buy_item(100)
print(total_price)

def person_info(f_name, l_name, age):
    return {
        'first_name': f_name,
        'last_name': l_name,
        'age': age
    }

person = person_info("Luiz", "Gonçalves", 30)
print(person)
print(type(person))