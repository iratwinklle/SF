def binary_search(list, item):
  low = 0
  high = len(list) - 1
  i = 0
  while low <= high:
    mid = (low + high) // 2
    if list[mid] < item and list[mid +1] >= item:
      return mid
    if list[mid] > item:
      high = mid - 1
    else:
      low = mid + 1
    i=i+1
    return None
seq = input('Введите последовательность чисел через пробел:')
number = int(input('Введите любое число:'))
seq_clear = list(map(int, seq.split()))
for i in range(len(seq_clear)):
    for j in range(len(seq_clear) - i - 1):
        if seq_clear[j] > seq_clear[j + 1]:
            seq_clear[j], seq_clear[j + 1] = seq_clear[j + 1], seq_clear[j]
print(seq_clear)
print(binary_search(seq_clear, number))






