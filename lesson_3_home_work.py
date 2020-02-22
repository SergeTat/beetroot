
# Task - 1

s = 'helloworld'
s1 = 'my'
s2 = 'x'

print(s[0:3] + s[-1])
print(s1+s1)
print(s2[1:1])

# Task - 2

n = input("Номер? ")
n = str(n)
if len(n) == 10 and n.isdigit ():
    print ("Правильный номер")
else:
    print ("Номер неправильный")

# Task - 3

n1 = input("Сколько будет 2 + 2? ")
n1 = float(n1)

if n1 == 4:
    print ("Правильно")
else:
    print ("Неправильно")

# Task - 4

n2 = input("Как меня зовут?")
n2 = str(n2)

if n2 == 'Сергей' or n2.islower():
    print ("Правильно")
else:
    print ("Неправильно")