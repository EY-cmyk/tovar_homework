import math
print('')
a = str('Notebook')
b = str('SmartPhone')
c = str('Apple')
print(a)
print(b)
print(c)
print(a,b,c)



print('')
print('●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●')
print('')


lis = str("'Notebook', 'SmartPhone', 'Apple'")
result = str(input('Введите название товара = '))
print(lis)
if bool(result) == lis:  
    print("Есть такой товар!")
else:
    print("Нету такого товара!")


print('')
print('●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●●▬▬▬▬๑۩۩๑▬▬▬▬▬●')
print('')

students = ('Vasya, Tolia, Igor')
print('Клиенты:',students)


print('')
print('║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║')
print('')



Notebook = 12
SmartPhone= 2
Apple = 10
all_value = (Notebook+SmartPhone+Apple)
print('Общее количество товара :',all_value)


print('')
print('║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║')
print('')

stditems = {
    str('Tolia') : 'Notebook',
    str('Igor') : 'SmartPhone',
    str('Vasya') : 'Apple'
}

print(stditems)

print('')
print('║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║')
print('')


first_name = "Tolia"
second_name = "Igor"
third_name = "Vasya"

print(f"Notebook is for {first_name}")
print(f"SmartPhone is for {second_name}")
print(f"Apple is for {third_name}")


print('')
print('║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║')
print('')


Notebook = 1400
SmartPhone= 250
Apple = 2.5
all_sum = (Notebook+SmartPhone+Apple)
print('Общая цена товара :',all_sum)
print('Цена Notebook:',Notebook)
print('Цена SmartPhone:',SmartPhone)
print('Цена Apple:',Apple)


print('')
print('║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║')
print('')


nb = 1400
sf = 250
ap = 2.5

money_vasya= 12000
money_igor = 9000
money_tolia = 15000

k = int(input('Введите предпочитаемое  количество Notebook:'))
l = int(input('Введите предпочитаемое  количество SmartPhone:'))
t = int(input('Введите предпочитаемое  количество Apple:'))
all_count = k,l,t
print('')
if str(all_count) != str(all_value) :
    print('Not enought stuff')
    
else:
    print("We have stuff in shop")


z = k * nb
z2 = l * sf
z3 = t * ap
z4 = z+z2+z3
print('')

print('')
if money_vasya <= z4:
    print("Vasya can't buy this stuff")
else:
    print('Vasya buy all dat stuff')
print('')
if money_igor <= z4:
    print("Igor cant't buy dat stuff")
else:
    print("Igor buy all dat stuff")

print('')

if money_tolia <= z4:
    print("Tolia can't buy dat stuff")
else  :
    print("Tolia  buy dat stuff")

print('')

print("Цена Notebook на выходе будет:",z)
print("Цена SmartPhone на выходе будет:",z2)
print("Цена Apple на выходе будет:",z3)



print('')
print('║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║║▌│█║▌│█║▌│█│║▌║█│▌║█│▌║')
print('')



first_name = "Tolia"
second_name = "Igor"
third_name = "Vasya"

print(f'''{first_name} bring Notebook to {second_name} and {third_name} осталься ни с чем потому что уже давно сожрал Apple and с 
ним не выгодно меняться потому что у него ничего нету''')
