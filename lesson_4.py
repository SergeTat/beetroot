#Проверка на высокосный год
print("Введите год")
y = int(input())

if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("Обычный")
else:
    print("Високосный")

#Проверка возраста
print("Введите возраст")
a = float(input())

if 56 > a > 18:
    print("Молодой")
elif 0 < a <= 18 :
    print("Юный")
else:
    print("Старый")

#Проверка числа

print("Введите  число")
a = float(input())

if  a < 39:
    print("F")
elif a == 40:
    print("E")
elif 40 < a < 59 :
    print("D")
elif 60 < a < 73 :
    print("C")
elif 74 < a < 89 :
    print("B")
else:
    print("A")
