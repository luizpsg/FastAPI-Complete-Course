#
# Lists are a collection of data
#

myList = [80, 96, 72, 100, 8]

print(myList)

people_list = ['John', 'Paul', 'George', 'Ringo']
print(people_list)

# Accessing elements in a list
print(myList[0])
print(people_list[0:2])

myList.append(99)
print(myList)

myList.insert(2, 1000)
print(myList)

myList.remove(8)
print(myList)

myList.pop(0)
print(myList)

myList.sort()
print(myList)

myList.reverse()
print(myList)

#
#- Create a list of 5 animals called zoo

# - Delete the animal at the 3rd index.

# - Append a new animal at the end of the list

# - Delete the animal at the beginning of the list.

# - Print all the animals

# - Print only the first 3 animals
#

zoo = ['lion', 'tiger', 'bear', 'elephant', 'giraffe']

#Não retorna o elemento removido
del zoo[3]

#Retorna o elemento removido
zoo.pop(3)

print(zoo)

zoo.append('zebra')

print(zoo)

del zoo[0]

print(zoo)

for animal in range (0, 3):
    print(zoo[animal])

print (zoo[0:3])