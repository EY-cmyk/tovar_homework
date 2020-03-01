a = str('Notebook')
b = str('SmartPhone')
c = str('Apple')
print(a)
print(b)
print(c)


lis = str(" 'Notebook', 'SmartPhone', 'Apple'")
result = str(input('Введите имя товара = '))
result = bool(lis)
print(lis)
print(result)

Notebook = 12
SmartPhone = 13
Apple = 1

students = {
    str('Tolia') : 'Notebook',
    str('Igor') : 'SmartPhone',
    str('Vasya') : 'Apple'
}
result2 = str(input("Введите имя ученика ="))
result2 = bool(students)
print(result2)
print(students)

#при проверке постоянно выдаёт True.При проверке товара такая же ошибка.
first_name = "Tolia"
second_name = "Igor"
third_name = "Vasya"

print(f"Notebook is for {first_name}")
print(f"SmartPhone is for {second_name}")
print(f"Apple is for {third_name}")

Notebook_quantity = str(input("Введите количесвтво Notebook = "))
SmartPhone_quantity = str(input("Введите количество SmartPhone = "))
Apple_quantity = str(input("Введите количество Apple = "))
z = 140
# тут загуглить как сумировать количество товара и сделать через if elif else or bool проверку
g = Notebook_quantity
f = SmartPhone_quantity
d = Apple_quantity
h = (g+f+d)
print(h)


#Проверка здесь уже тоже не работает 


print(f'''{first_name} bring Notebook to {second_name} and {third_name} осталься ни с чем потому что уже давно сожрал Apple and с 
ним не выгодно меняться потому что у него ничего нету''')


    
