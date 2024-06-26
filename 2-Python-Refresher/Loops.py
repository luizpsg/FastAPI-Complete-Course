#
# Loops
#

my_list = [1, 2, 3, 4, 5]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

sum_of_for_loop = 0

for number in my_list:
    sum_of_for_loop += number 
    print(number)

print(sum_of_for_loop)

print("-----------------")

for number in range(1, 6):
    print(number)


my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in my_list:
    print(f"Happy {day}!")

print("-----------------")

i = 0

while i < 5:
    i += 1
    print(i)

print("-----------------")

i = 0
while i < 5:
  i += 1
  if i == 3:
      continue
  print(i)
  if i == 4:
      break
else:
    print("Loop completed")

print("-----------------")

e = 0
while e < 3:
    for day in my_list:
        if day == "Monday":
            continue 
        print(f"Happy {day}!")
    e += 1