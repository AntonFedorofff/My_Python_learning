import random as r
m = r.randrange(1, 101)

while True:
    number = int(input())
    if number > m:
        print('Слишком много, попробуйте еще раз')
        continue
    elif number < m:
        print('Слишком мало, попробуйте еще раз')
        continue
    elif number == m:
        print('Вы угадали, поздравляем!')
        break
