def binary_search(list, int):
    low = 0
    high = len(list) - 1
    if list[high] < int:
        return -1
    if list[low] >= int:
        return -2
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < int and list[mid + 1] >= int:
            return mid
        if list[mid] >= int:
            high = mid - 1
        else:
            low = mid + 1
    return -3

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
def seq_check_clear(string):
    seq_list = string.split(' ')
    try:
        int_list = list(map(int, seq_list))
        return int_list
    except:
        return False

seq = input('Введите последовательность чисел через пробел:')
number = input('Введите любое число:')
seq_check = seq_check_clear(seq)
number_check = seq_check_clear(number)
if seq_check and number_check:
    sorted_seq = bubble_sort(seq_check)
    print('Список введенных чисел по возрастанию: {}'.format(sorted_seq))
    number_int = int(number)
    index = binary_search(sorted_seq, number_int)
    if index >= 0:
        print('Индекс элемента, который меньше введенного числа: {}'.format(index))
    else:
        print('Предоставить индекс числа, которое меньше введенного невозможно, т.к. введенное число за пределами последовательности')
else:
    print("Введенные данные не соответствуют требуемым условиям")