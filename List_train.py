# 添加嘉宾练习
guests = ['Eugene', 'Maickle', 'nine']
print(guests)
guests.append('huang')
print(guests)

print("I will invite the following person that " + guests[0].title() + " to my party")
print(guests.pop(1) + " can not keep an appointment")

guests.append('fuy')
print("So I will invite " + guests[3].title() + "to my party")

print("Because I find a big table")
guests.insert(0, 'zi')
print("So I also want to invite" + guests[0].title() + " to my party")

# 永久性排序，按字母排序
guests.sort()
print(guests)
print(guests[-1])

# 遍历整个列表
for guest in guests:
    print(guest.title() + " is my guest")
    print("I wish I can together again with " + guest.title() + ".\n")

numbers = list(range(1, 19))
print(numbers)
min(numbers)

squares = []
for value in range(1, 10):
    square = value**2
    squares.append(square)
print(squares)

# 列表解析
squares = [value**2 for value in range(1, 10)]
print(squares)

# 4-3练习
for i in range(1, 21):
    print(i)
# 4-4练习
# list_number = list(range(1000000))
# print(list_number)

# 4-5练习
list_number = list(range(1, 1000000))
print(min(list_number))
print(max(list_number))
print(sum(list_number))

# 4-6练习，奇数显示方法1
odd_numbers = []
for value in range(1, 20):
    odd_number = value % 2
    if odd_number == 1:
        odd_numbers.append(value)
print(odd_numbers)

# 4-6练习，奇数显示方法1
odd_numbers = list(range(1, 20, 2))
for i in odd_numbers:
    print(i)
# 4-7练习,3的倍数显示方法1
multiple_3 = list(range(3, 31, 3))
for i in multiple_3:
    print(i)
# 4-7练习,3的倍数显示方法2
numbers = []
for value in range(3, 31):
    multiple_3 = value % 3
    if multiple_3 == 0:
        numbers.append(value)
print(numbers)

# 4-8练习，立方
cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print(cubes)

# 列表解析实现1-10的立方
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:2])
print(players[-2:])

# 4-12练习
my_foods = ['pizza', 'falafel', 'carrot', 'cake']
# 复制列表
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite are")
for favorite in friend_foods:
    print(favorite)
print("my friend's favorite are")
for favorite in friend_foods:
    print(favorite)
# 元组
dimensions = (200, 20)
for i in dimensions:
    print(i)

