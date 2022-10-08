""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
 для всех значений предикат. """


print('программа для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предика')

print ('Введите значение для проверки в формате X + Enter, Y + Enter Z + Enter')
numbers = []
for i in range (3):
    numbers.append(int(input()))
a = not (numbers[0] or numbers [1] or numbers [2]) 
b = (not numbers[0] and not numbers[1] and not numbers [2])
c = a == b
print (c)
