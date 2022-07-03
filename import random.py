import random 

num = random.randint(1, 1000)
count = 0
a = -1

while num != a:
    a = int(input('Введите число: ' ))
    if a > num:
        count+= 1
        print('Введите число поменьше! ')
    elif a < num:
        count+= 1
        print('Введите число побольше!' )
    else:
        count+= 1
        print('Поздравляю! Вы угадали, это число: '+ str(num), 'Количество попыток: ' + str(count))
        break