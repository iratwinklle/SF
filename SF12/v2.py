per_cent = {'tkb': 5.6, 'skb': 5.9, 'vtb': 4.28, 'sber': 4.0}
money = int(input("Введите сумму, которую планируете положить под проценты:"))
deposit = []
deposit.append(int(money/100 * per_cent["tkb"]))
deposit.append(int(money/100 * per_cent["skb"]))
deposit.append(int(money/100 * per_cent["vtb"]))
deposit.append(int(money/100 * per_cent["sber"]))
print("Накопленные средства за год вклада в банках составят {} рублей".format( deposit))
deposit.sort()
print("Максимальная сумма, которую вы можете заработать: {} рублей".format(deposit[-1]))