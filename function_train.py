# 函数
active = True


# def display_message():
#     print("We will learning function in this unit")
#
#
# display_message()


# def favorite_books(title):
#     print("\nOne of my favorite books is " + title)
#
#
# while active:
#     title_1 = input("Please enter your favorite books\n")
#     favorite_books(title_1)
#     if title_1 == 'no':
#         active = False
#     print("other?")

# 给函数形参设置默认值
# def describe_pet(pet_name, animal_type='dog'):
#     print("\nI have a " + animal_type + ".")
#     print("My" + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(pet_name='willie', animal_type='cat')
#
#
# # 8-3练习
#     def make_shirt(size, model):
#         print("This shirt's size is " + size + " and maker is " + model)
#
#
#     make_shirt(size='XL', model='class')
#
#
# # 8-4练习
# def make_shirt(size='L', model='I love python'):
#     print("a " + model + "'s " + size + " shirt")
#
#
# make_shirt()
# make_shirt(size='M')
# make_shirt(model='I love Deep learning')

# 形参指定默认空字符串使实参变成可选
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix',)
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# # 返回字典
# def build_person(first_name, last_name, age=''):
#     person = {'first_name': first_name, 'last_name': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=23)
# print(musician)

# 问候用户，用函数和while实现
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# while True:
#     print("\nTell mo your name")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First_name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last_name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello " + formatted_name)

# def city_country(city_name, country_name):
#     city = city_name + ', ' + country_name
#     return city
#
#
# musician = city_country('hengyang', 'China')
# print(musician.title())

import numpy as np
# x = np.array([[1, 2, 3], [4, 5, 6]])
# print("x:\n{}".format(x))
#
from scipy import sparse
#
# # 创建一个二维Numpy数组，对角线为1，其余为0
# eye = np.eye(4)
# print("Numpy arraty:\n{}".format(eye))
#
# import pandas as pd
# from IPython.display import display
#
# data = {
#     'name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Location': ['New York', 'Paris', 'Berlin', 'London'],
#     'age': [24, 13, 53, 33],
#     }
#
# data_pandas = pd.DataFrame(data)
# display(data_pandas)


# def make_album(singer_name, music_name, music_count = ''):
#     special = {
#         's_name': singer_name,
#         'm_name': music_name,
#         }
#     if music_count:
#         special['music_count'] = music_count
#     return special
#
#
# message = make_album('chengl', 'country', 19)
# message_1 = make_album('jielun', 'cai')
# print(message)
# print(message_1)

# def greet_users(names):
#     for name in names:
#         message = 'Hello, ' + name.title() + '!'
#         print(message)
#
#
# user_names = ['hannah', 'ty', 'margot']
# greet_users(user_names)

# 传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)


make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
