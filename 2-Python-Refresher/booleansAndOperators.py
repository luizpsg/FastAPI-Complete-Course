#
# Booleans and Operators
#

like_coffee = True
like_tea = False

favorite_food = "pizza"
favorite_number = 32

print(like_coffee)
print(type(like_coffee))
print(type(favorite_food))
print(type(favorite_number))

print (1 == 2)
print (1 != 2)
print (1 > 2)
print (1 < 2)
print (1 >= 2)
print (1 <= 2)

print (1 == 1 and 2 == 2)
print (1 == 1 and 2 == 3)
print (1 == 1 or 2 == 3)
print (1 == 2 or 2 == 3)

print (not 1 == 1)
print (not 1 == 2)

print (1 == 1 and (not 2 == 3))
print (1 == 1 and (not 2 == 2))
print (1 == 1 or (not 2 == 2))
print (1 == 2 or (not 2 == 2))

print (1 == 1 and (2 == 2 or 3 == 3))
print (1 == 1 and (2 == 3 or 3 == 3))
print (1 == 2 or (2 == 2 and 3 == 3))
print (1 == 2 or (2 == 3 and 3 == 3))

print (1 == 1 and (2 == 2 or 3 == 6) and 4 == 4)
