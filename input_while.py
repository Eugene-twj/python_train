# prompt = "Do you have girlfriend ?"
# print(prompt)
# active = True
# while active:
#     y_n = input("Please input y/Y or n/N:\n")
#     if y_n == 'y' or y_n == 'Y':
#         print("Congratulation! you isn't single dog\n")
#     elif y_n == 'n' or y_n == "N":
#         print("It is shame that you are still a single dog\n")
#     else:
#         active = False
#
# prompt = "Tell me something. and I will repeat it back to you:\n"
# prompt += "Enter 'quit' to end the program.\n"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# message_1 = ""
# prompt = "Please choose your topping:\n"
# while input(prompt) != 'quit':
#     print("Thanks for your order we will finish your pizza soon")


# # 使用while实现列表之间移动元素
# prompt = "Please choose confirmed user"
# prompt += "\nInput number 1 or 2 or 3"
# prompt += "\nEnter 'quit' to end the program"
# unconfirmed_users = ['eugene', 'xu', 'fu']
# confirmed_users = []
#
# # 存储输入
# message = ""
#
# # 判断未验证用户列表是否为空
# while unconfirmed_users:
#     print("Which user was confirmed in The flowing users ")
#     print(prompt)
#
#     # 遍历未验证用户列表
#     for unconfirmed_user in unconfirmed_users:
#         print("\t" + unconfirmed_user)
#
#     # 用户输入
#     message = input()
#     print("\n" + prompt)
#     if message == '1':
#
#         # 弹出未验证用户列表末尾元素
#         current_user = unconfirmed_users.pop()
#
#         # 将元素添加到验证用户列表末尾
#         confirmed_users.append(current_user)
#         for unconfirmed_user in unconfirmed_users:
#             print("\n" + unconfirmed_user + " was't confirmed")
#     elif message == '2':
#         current_user = unconfirmed_users.pop()
#         confirmed_users.append(current_user)
#         for unconfirmed_user in unconfirmed_users:
#             print("\n" + unconfirmed_user + " was't confirmed\n")
#     elif message == '3':
#         current_user = unconfirmed_users.pop()
#         confirmed_users.append(current_user)
#         for unconfirmed_user in unconfirmed_users:
#             print("\n" + unconfirmed_user + " was confirmed")
#     else:
#         print("Please input 1 or 2 or 3:\n")
# print("\n confirmed users are")
# print(confirmed_users)
# print(unconfirmed_users)

# 7-8练习
sandwich_orders = ['tuna', 'tune', 'tun']
finished_sandwiches = []
# while sandwich_orders:
#     for sandwich_order in sorted(sandwich_orders):
#         print("\nI made your " + sandwich_order + " sandwich")
#         current_order = sandwich_orders.pop()
#         finished_sandwiches.append(current_order)
#     print("\n" + str(finished_sandwiches))

# 7-9练习
# print("Sorry, Pastrami is all sell")
# for _ in range(1, 4):
#     sandwich_orders.append('pastrami')
# a = 'pastrami'
# active = True
# while active:
#     if a in sandwich_orders:
#         sandwich_orders.remove('pastrami')
#     else:
#         active = False
# print(sandwich_orders)

