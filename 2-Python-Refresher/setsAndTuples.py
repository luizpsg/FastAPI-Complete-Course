#
# Sets are similar to lists but they are unordered and do not
#  have duplicates.
#

my_set = {1000, 1, 3, 2, 4, 5, 5}
print(my_set)
print(type(my_set))
print(len(my_set))

for x in my_set:
    print(x)

print(5 in my_set)
print(6 in my_set)

my_set.add(6)
print(my_set)

#lança exception se o elemento não existir
my_set.remove(6)
print(my_set)

#não lança exception se o elemento não existir
my_set.discard(1000)
print(my_set)

my_set.clear()
print(my_set)

my_set.add(1)
print(my_set)

my_set.update([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(my_set)

### Tuples ###
# Tuples are similar to lists but they are immutable.
# You cannot change the values of a tuple once it is set.
# Tuples are defined using parentheses.
# Tuples are faster than lists.
# Tuples are used when you want to protect the data from being changed.
# Tuples are used when you want to use the data as a key in a dictionary.

my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

for x in my_tuple:
    print(x)

print(5 in my_tuple)
print(6 in my_tuple)
