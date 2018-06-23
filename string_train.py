message = 'just try "hello world"'
print(message)

message = "try again "
print(message)
name = "asDw"
print(name.title())
print(name.upper())
print(name.capitalize())
print(name.casefold())

old = 23
print('hi my name is %s,I am %d' % (message, old))
print('%2d-%02d' % (333, 1))
print('%.3f' % 3.1415926)
r = 17.125
print('%.1f' % r)
print('Hello,{0},成绩提升了,{1}'.format("小明", 17.125))
full_name = message + " " + name
print(full_name)

print("Hello " + full_name.title() + "！")

name = """              I
         LOVE    YOU
       """
print(name)
print(message.rstrip())  # 删除字符串末端空白


name1 = "eugene"
print(name1[43:])