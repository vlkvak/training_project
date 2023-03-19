tickets = int(input('Введите количество билетов:'))
age = list(map(int, input('Введите возраст посетителей через пробел:').split()))
while tickets != len(age):
    age(list(map(int, input('Количество посетителей не совпадает! \n'
                            'Введите возраст посетителей через пробел:').split())))
price = []
for i in age:
    if i in range (0, 18):
        price.append(0)
    if i in range(19, 25):
        price.append(990)
    else:
        price.append(1390)
if tickets > 3:
        print('Сумма к оплате со скидкой 10%: ', sum(price) - ((sum(price) / 100) * 10), 'рублей')
else:
        print('Сумма к оплате: ', sum(price), 'рублей')