number = int(input('Введите число: '))
if number % 2 == 0 and number % 3 == 0:
    print('third')
if number % 3 == 0:
    print('first')
elif number % 2 == 0:
    print('second')
else:
    print('Число не подходит')