seq = '45 30 55 20 80 65 11' #input('Введите последовательность чисел через пробел:')
number = 34 #int(input('Введите любое число:'))
seq_clear = list(map(int, seq.split()))
for i in range(len(seq_clear)):
    for j in range(len(seq_clear) - i - 1):
        if seq_clear[j] > seq_clear[j + 1]:
            seq_clear[j], seq_clear[j + 1] = seq_clear[j + 1], seq_clear[j]
print(seq_clear)
for i in seq_clear




