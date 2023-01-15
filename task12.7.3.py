per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(per_cent.values())
money = int(input('введите сумму:'))
for i in range(len(deposit)):
    deposit[i] *= money / 100
deposit = list(map(int, deposit))
print('Максимальная сумма, которую вы можете заработать -', max(deposit))