"""
print("PROBLEM1")
print (17925 >= 34**2)
print (17925 >= 26*3)
print (17925 >= 17*33)
print (17925 >= 4394*2)
"""

"""
print("PROBLEM2")
a = 11 
b = 15
c = 50
resab = a > b
resac = a < c 
print(resab, resac)
print((7 % 3) * 4.8)
a1 = 3
b1 = 3
c1 = a1 == b1
print(c1)
a2 = 3
b2 = 2
c2 = a2 == b2
print(c2)
"""

"""
print("PRIBLEM3")
a = 1
b = 2
c = (a + b) * 3
d = c ** 2
e = 193432 - d
print(e)
"""

"""
print("PROBLEM4")
print(17*3 > 12*5)
print(12**3 > 13*7)
print(4**5 > 512+512)
"""



































"IF ELIF ELSE"
'''
print('PROBLEM2')
a = 2**3
b = 3**2
if a > b:
  print("a")
else:
  print("b")
'''

'''
print('PROBLEM22')
a = 1
b = 2
c = 3
if a > b and a > c:
  print("a >")
elif b > a and b > c:
  print("b >")
elif c > a and c > b:
  print("c >")
else:
  print("error")

if a < b and a < c:
  print("a <")
elif b < a and b < c:
  print("b <")
elif c < a and c < b:
  print("c <")
else:
  print("error")
'''

'''
print('PRIBLEM15')
a = 17391 % 17
b = 546 % 17
c = 934 % 17
if a < b and a < c:
  print("a < ", + a)
elif b < a and b < c:
  print("b < ", + b)
else:
  print("c < ", + c)
'''


'''
print('PRIBLEM39')
x = 13 ** 2
y = 172
if x < y:
  print('**2')
  x = x ** 2
  print(x)
''' 


'''
print('PROBLEM5')
a = int(input('Введите число: '))
if a % 2 == 0:
  print('четное')
if a % 3 == 0:
  print('без остатка')
if a / 3 != 0:
  print('не делится без остатка')
if a ** 2 > 1000:
  print('> 1000')
if a ** 2 < 1000:
  print('< 1000')
'''


'''
print('PROBLEM7')
if True:
  print('kkkk')
'''


'''
print('PROBLEM9')
a = 3
if a > 1:
  print(a)
  if a > 2:
    print(a)
    if a == 3:
      print(a)
'''

'''
print('PROBLEM3')
a = 100
if a < 22 and a > -1:
  print('Разрешенный')
if a > 56 and a < 101:
  print('Разрешенный')
if a > 21 and a < 57:
  print('Запрешенный')
'''


'''
print('PROBLEM45')
a = 10//5
b = 10/5
if a == b:
  print(a + b)
else:
  print('Они не равны')
'''  


'''
print('PROBLEM33')
a = True
if a == True:
  print('-1')
'''

'''
print('PROBLEM11')
a = 10
b = 5 
if a and b > 0:
  print('Положительные')
''' 


'''
print('PROBLEM0')
a = 10
b = 5
if a > b:
  print(a+2)
else: 
  print(b+2)
'''




"ЦИКЛЫ WHILE FOR"

'''
print('№1')
lang1 = 'Rust'
languages = ['go','java','php','python','JS','ruby']
if lang1 in languages:
  print('this languages is in list')
else:
  print('Nothing')
'''

'''
print('#2')
languages = ['go','java','php','python','JS','ruby']
for x in languages:
  if x == 'php':
    break
  print(x)
'''

'''
print('#3')
a = 7
i = 0
while i <= 5:
  a = a * a
  i += 1
  print(a)
'''


'''
print('#4')
languages = ['go','java','php','python','JS','ruby']
for x, languages in enumerate(languages):
  print(x + 1, languages)
'''


'''
print('#5')
i = 1
while i < 10:
  i +=1
  print(i)
while i != 1:
  i -= 1
  print(i)
'''


'''
print('#6')
names = ('Max','Lya','Dan','Aib','At',
        'Sala','Adi','Joma','Alym','Erm',
        'Das','Beka','Asla')
print(names[::2])
'''

'''
print('#7')
names = ('Max','Lya','Dan','Aib','At',
        'Sala','Adi','Joma','Alym','Erm',
        'Das','Beka','Asla')
print(names[1::2])
'''

'''
print('#8')
num = int(input('Введите трехзначное число: '))
res1 = num // 1
res2 = num // 10
res3 = num // 100
if res1 > 100 or res2 > 10 or res3 > 1:
  print(res1, res2, res3)
if num > 0:
  print("Положительное")
if num / 2 == 0:
  print("Четное")
'''


"""
print('#9')
a = int(input('Какое-то число: '))
res = a % 13
if res == 0:
  	print('делится')
else:
	print('Не делится')
"""
'''
name = input("Your name: ")
last_name = input("Your last name: ")
full_name = f"{name} {last_name}"
print(f"Hello,{full_name.title()}!")
'''

'''
name = " kairat "
print(name)
print(name.rstrip())
print(name.lstrip())
'''
'''
names = ['Alina', 'Kairat', 'Urmat']
message = f"The name is {names[1].title()}"
print(message)
new_name = names.append('Beka')
print(names)
names.append('Hella')
print(names)
names.insert(1, 'Monika')
print(names)
del names[2]
print(names)
names.pop()
print(names)
output_last_pop_name = names.pop()
print(output_last_pop_name)
print(f"Последняя удаленная с помощью метода pop значение списка {output_last_pop_name.title()}.")
middle_pop = names.pop(2)
print(middle_pop)
print(f"Удалили с помощью метода pop {middle_pop.title()}")
print(names)
#Чтобы проста удалить и не юзать del
#Чтобы удалить но после юзать pop
name_remove = names.remove('Alina')
print(f'Удалили {name_remove}, не зная ее индекс')
print(names)
for i in range(1, 5 + 1):
	print(i)
'''
'''
m = "Hello Word"
l = [i * 2 for i in m]
print(l)
'''




#Dictioners
'''
alien_0 = {'color':'green','helth':5,}
print(alien_0['color'])
print(alien_0['helth'])

new_helth = alien_0['helth']
print(f'Здоровье пришельца {new_helth}')
# add new atribute

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# alien update position

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
	print(x_increment)

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
'''
#del posotion
'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
'''
'''
program_lang = {
	'baha':'java',
	'kama':'python',
	'alya':'ruby'
}
user = program_lang['kama'].title()
print(f"{program_lang['kama'].title()}'s "f"Favorite lang is {user}")
'''

'''
'''
#get method peredaetsya key
'''
alien_0 = {'colors':'green','speed':'slow'}
point_value = alien_0.get('points', 'Net takogo')
print(point_value)
'''

#item() перебор пар
'''
'''
'''
program_lang = {
	'baha':'java',
	'kama':'python',
	'alya':'ruby'
}

for key, value in program_lang.items():
	print(f"\n\tKey: {key}")
	print(f"\nValue: {value}")

for name, lang in program_lang.items():
	print(f"{name.title()}'s favorite lang is {lang.title()}")
'''


'''
#keys()  перебор всех ключей в словаре
'''
'''
program_lang = {
	'baha':'java',
	'kama':'python',
	'alya':'ruby',
}
#keys() Работает по умолчанию
for name in program_lang.keys():
	print(name.title())

for name in program_lang:
	print(name.title())

for name in program_lang.keys():
	print(name.title())
	if name in program_lang:
		lang = program_lang[name].title()
		print(f"\t{name.title()}, i see you love {lang}")
if 'roma' not in program_lang.keys():
	print("roma is not in list")
'''
'''
#sorted() перебор ключей в определенном порядке
'''
'''
program_lang = {
	'baha':'java',
	'kama':'python',
	'alya':'ruby'
}

for name in sorted(program_lang.keys()):
	print(f"{name.title()}, thank you.")
'''
'''
#values() перебор всех значений в словаре
'''
'''
program_lang = {
	'baha':'java',
	'kama':'python',
	'alya':'ruby',
	'kama':'python'
}
print("....")

#for lang in program_lang.values():
#	print(lang.title())
#Для вывода уникальных значений юзай set()
for lang in set(program_lang.values()):
	print(lang.title())
'''


#Список словарей
'''
'''
'''
a_0 = {'color':'green', 'helth': 5}
a_1 = {'color':'red', 'helth': 10}
a_2 = {'color':'blue', 'helth': 20}

aliens = [a_0, a_1, a_2]
for alien in aliens:
	print(alien)

aliens = []
#создание первых 30 пришельцев
for alien_number in range(30):
	new_alien = {'color':'green', 'helth':50, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['helth'] = 10

	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['helth'] = 15
#вывод первых 5
for alien in aliens[:5]:
	print(alien)
print("....")

print(f"Total number of aliens:{len(aliens)}")
'''

'''
#Список в словаре
'''
'''
program_lang = {
	'kaha':['java','c'],
	'kama':['python','go'],
	'alya':['ruby','c++'],
	'kama':['python', 'haskel']
}
for name, langs in program_lang.items():
	print(f"\n{name.title()}'s favorite lang are:")
	for lang in langs:
		print(f"\t{lang.title()}") 
'''
'''
#Словарь в словаре
'''

# users = {
# 	'inshtein' : {
# 		'first_n':'albert',
# 		'last_n':'inshtein',
# 		'location':'german',
# 		},
# 	'putin' : {
# 		'first_n':'vlad',
# 		'last_n':'putin',
# 		'location':'russia',
# 		},
# 	}

# for username, user_info in users.items():
# 	print(f"\nUsername: {username}")
# 	full_name = f"{user_info['first_n']} {user_info['last_n']}"
# 	location = user_info['location']
# 	print(f"\tFull name: {full_name.title()}")
# 	print(f"\tLocation: {location.title()}")
'''
kuhnya = {
		"lagman":120,
		"borsh": 150}
kuhnya['beshbarmak'] = 130
kuhnya.update({'lagman':135})
kuhnya.pop('borsh')
print(kuhnya)
kuhnya.update({'drinks':["Cola","Fanta"]})
print(kuhnya)
'''


'''
a_set = {'add','clear','discard','pop',
	'difference', 'update','intersection',
	'intersection_update',}
a_dict = {'clear','get','items',
	'values','update','keys',}

res = a_set.intersection(a_set, a_dict)
print(res)
'''


'''
a = {}
x = len(a)
for i in range(3):
	keys = input("Введите Имя:")
	pas = input("Введите Пароль: ")
	#a.update({keys:pas})
	a[keys] = pas
	print(a)
'''

'''
names = {'Erjan':'python',
		'Myktybek':'java',
		'Adilet':'c++',
		'Sezim':'HUCKER',
		'Azamat':'Super Huker',}

for name, values in names.items():
	print(f"Здравствуйте {name.title()} Профоессия {values.title()}")
#	for value in values:
#		print(f"Профессия {value.title()}")
'''


a_set = set()
i = 0
while i <= 10:
	num = int(input("Введите число: "))
	a_set.add(num)
	i += 1
	a_typ = tuple(a_set)
	

print(a_typ)
