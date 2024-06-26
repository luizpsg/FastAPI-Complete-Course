#
# Dictionary is a collection of key-value pairs.
#

# Create a dictionary
person = {
    'name': 'John',
    'age': 30,
    'is_married': False
}

# Access a value
print(person['name'])  # John
print(person['age'])  # 30
print(person['is_married'])  # False

person['bold'] = True
print(person)

person.pop('age')

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

person2 = person.copy()
print(person2)
person2.pop("name")

print(person)
print(person2)


person.clear()
print(person)

# del person
# print(person)


my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key, value in my_vehicle.items():
    print(key, value)

vehicle2 = my_vehicle.copy()

vehicle2['number_of_tires'] = 4
vehicle2.pop("mileage")

for key in vehicle2:
    print(key)