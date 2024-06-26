#
# If Else Elif
#

x = 2

if x == 1:
    print("x is 1")
else:
    print("x is not 1")

print("This is outside the if block")

hour = 13 

if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good evening")

print("This is outside the if block")

grade = 69

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")