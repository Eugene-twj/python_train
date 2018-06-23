alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
     }

# 按字母顺序遍历字典键-值对
for name, language in sorted(favorite_languages.items()):
    print(name.title() + "'s favorite language is " + language)

# 按键值遍历字典
print("\nThe following language have been mentioned")
for language in favorite_languages.values():
    print(language.title())
vocabulary = {
    'sex': 'it means person',
    'github': 'it is a version control',
    'vs': 'it means two person competition',
    'python': 'it is a programme language',
    'eugene': 'it is a person',
    }
for voc, mean in vocabulary.items():
    print(voc + "\nit represent " + mean)

# 添加键-值对
vocabulary['ss'] = 'double s'
vocabulary['rr'] = 'double r'
vocabulary['tt'] = 'double t'
vocabulary['gg'] = 'double g'
vocabulary['yy'] = 'double y'

# 列表中嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', "point": 10}
alien_2 = {'color': 'red', 'point': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = [alien_1]
for _ in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
for alien in aliens[:5]:
    print(alien)
# 字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

# 字典中嵌套字典
users = {
    'eugene': {
        'name': 'tang',
        'location': 'hunan',
        'phone': 1228,
        },
    'fu': {
        'name': 'fuy',
        'location': 'xin',
        'phone': 110,
    },
    }
for user, info in users.items():
    print("\n" + user + "'s detail information")
    for info_1, info_2 in info.items():
        if info_1 == 'name':
            print('\tThat name is ' + info_2.title())
        elif info_1 == 'location':
            print("\t" + user + "'s location is in " + info_2)
        elif info_1 == 'phone':
            print("\tHis phone is " + str(info_2))

# 练习6-7
people_1 = {
    'first_name': 'tang',
    'last_name': 'eugene',
    'age': 23,
    'city': 'hy',
    }
people_2 = {
    'first_name': 'fu',
    'last_name': 'fuy',
    'age': 23,
    'city': 'xj',
    }
people_3 = {
    'first_name': 'zhou',
    'last_name': 'mao',
    'age': 22,
    'city': 'xj',
    }
peoples = [people_1, people_2, people_3]
for people in peoples:
    print(people)
