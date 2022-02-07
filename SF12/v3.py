per_cent = {'tkb': 5.6, 'skb': 5.9, 'vtb': 4.28, 'sber': 4.0}
money = int(input("Введите сумму, которую планируете положить под проценты:"))
deposit = []
for i in per_cent:
    deposit.append(int(money / 100 * per_cent[i]))
print("Накопленные средства за год вклада в банках составят {} рублей".format(deposit))
deposit.sort()
print("Максимальная сумма, которую вы можете заработать: {} рублей".format(deposit[-1]))