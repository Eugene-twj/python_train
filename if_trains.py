cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'Bmw':
        print(car.upper())
    else:
        print(car.title())
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("true")
else:
    print("false")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 游乐场收费1
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

# 游乐场收费2
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 外星人颜色#1
alien_color = 'green'
if alien_color == 'green':
    print("You achieve 5 point")
if alien_color == 'yellow':
    print("  ")
age = 23
if age < 2:
    print("He is a baby")
elif age < 4:
    print("He is learning walk")
elif age < 13:
    print("He is a children")
elif age < 20:
    print("He is a teenager")
elif age < 65:
    print("He is a adult")
else:
    print("He is a old person")


if cars:
    print("true")


# 5-8练习
users = ['admin', 'eugene', 'root', 'first', 'second']
for user in users:
    if user == 'admin':
        print("Hello admin,would you like to see a status report\n")
    else:
        print("\nHello " + user + ",thank you for logging in again")

# 5-9练习
users = []
if users:
    for user in users:
        if user == "admin":
            print("Hello admin,would you like to see a status report\n")
        else:
            print("\nHello " + user + ",thank you for logging in again")
else:
    print("\nWe need to find some users")

# 5-10
current_users = ['admin', 'eugene', 'root', 'first', 'second']
new_users = ['g', 's', 'ti', 'first', 'second']
for new_user in new_users:
    if new_user in current_users:
        print("\nThis user was occupied,please use other user ")
    else:
        print("\nThis user is't used")

# 9x9乘法表
for number_1 in range(1, 10):
    for number_2 in range(1, 10):
        number = number_1 * number_2
        print(str(number_1) + " x " + str(number_2) + " = " + str(number))

# 练习5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("The number is First\n")
    elif number == 2:
        print("The number is Second\n")
    elif number == 3:
        print("The number is Third\n")
    else:
        print("The number is " + str(number) + "th\n")









