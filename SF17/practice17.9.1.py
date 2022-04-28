def binary_search(list, item):
  low = 0
  high = len(list) - 1
  i = 0
  if list[high] < item:
      return False
  if list[low] >= item:
      return False
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
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
def seq_check_clear(string):
    seq_list = string.split(' ')
    try:
        int_list = list(map(int,seq_list))
        return int_list
    except:
        return False

seq = input('Введите последовательность чисел через пробел:')
number = input('Введите любое число:')
seq_clear = seq_check_clear(seq)
number_check = seq_check_clear(number)
if seq_clear and number_check:
    sorted_seq = bubble_sort(seq_clear)
    print('Список введенных чисел по возрастанию: {}'.format(sorted_seq))
    index = binary_search(sorted_seq, number_check)
    if index:
        print('Номер позиции элемента, который меньше введенного пользователем числа, '
              'а следующий за ним больше или равен этому числу: {}'.format(index))
    else:
        print('Введенное число находится за пределами последовательности')
else:
    print("Введенные данные не соответствуют требуемым условиям")

