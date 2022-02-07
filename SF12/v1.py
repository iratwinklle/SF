per_cent = {'tkb': 5.6, 'skb': 5.9, 'vtb': 4.28, 'sber': 4.0}
percent_list = list(per_cent.values())
bank = list(per_cent.keys())
money = int(input("Введите сумму, которую планируете положить под проценты:"))
deposit = []
deposit.append(int(money/100 * percent_list[0]))
deposit.append(int(money/100 * percent_list[1]))
deposit.append(int(money/100 * percent_list[2]))
deposit.append(int(money/100 * percent_list[3]))
print("Накопленные средства за год вклада в банках {} составят {} рублей".format(bank, deposit))
deposit.sort()
print("Максимальная сумма, которую вы можете заработать: {} рублей".format(deposit[-1]))