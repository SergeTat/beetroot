# Task - 1

from random import randrange
x1 = randrange(10)
print (x1)
y = input("Угадайте число от 1 до 10:")
y = int(y)

if y == x1:
    print("Угадал")
else: print("Не угадал")


# Task - 2

n = input("What is your name? ")

r = input("How old are you? ")
r = int(r)
s = r + 1

print("Hello, %s in your next birthday you'll be %s years" %(n,s))

# Task - 3

from itertools import permutations

word = input ("Введите слово ")
word = str(word)

perms = [''.join(p) for p in permutations(word)]

print(perms)