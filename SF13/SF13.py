# Пример с поиском цифры 5 в числе
# print(list(str(123456789)))
# print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# list_digit = list(map(int, list(str(123456789))))
# print(5 in list_digit)
# print("5" in str(123456789))

# Задача на поиск чисел 3 и 7 в N c n-ым количеством чисел
# N = input("Введите число:")
# print("3"and "7" in str(N))

# Эквивалентность
# a = [1, 2, 3]
# print(id(a))  # id возвращает идентификатор объекта
# b = a
# print(id(b))
# print(a is b)  # а и b являются один и тем же объектом
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a)) # 2710536613568
# print(id(b)) # 2710536614464
# print(a == b)  # True
# print(a is b)  # False

# Условный оператор
# a = 16
# b = 14 + a
# print("b=", b)
#
# a = 7
# b = 9+a
# print("a=F(", b, ")")

# 13.3.3 Поиск ошибки
# Ворженный условный оператор
# rain = True
# heavy_rain = True
# if rain:
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

# 13.4 Исключения:
# try:
#     a = 5
#     b = 1
#     c = a / b
# except ZeroDivisionError:
#     print("Делить на 0 нельзя")
# else:
#     print (c)

# 13.4.8 задача с исключением
# try:
#     number = int(input("Введите число:"))
# except ValueError:
#     print("Вы ввели неправильное число")
# else:
#     print("Вы ввели", number)
# finally:
#     print("Выход из программы")
# Решение SF:
# try:
#     i = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')

# задание 13.5.1
# def are_both_odd(A, B):
#     return A % 2 == 1 and B % 2 == 1
# print(are_both_odd(3,5))

# задание 13.5.2 переделать код
# код задания
# x =  int(input("x ="))
# y =  int(input("y ="))
# if x > 0:
#     if y > 0:               # x > 0, y > 0
#          print("Первая четверть")
#     else:                   # x > 0, y < 0
#          print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#          print("Вторая четверть")
#     else:                   # x < 0, y < 0
#          print("Третья четверть")
# переделанный
# x =  int(input("x ="))
# y =  int(input("y ="))
# if x > 0 and y > 0:
#     print("Первая четверть")
# if x > 0 and y < 0:
#     print("Четвертая четверть")
# if x < 0 and y > 0:
#     print("Вторая четверть")
# if x < 0 and y < 0:
#     print("Третья четверть")

# Пример 3. Использование оператора if-elif-else.
# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")

# Задание 13.5.3
# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"
# В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
# def get_wind_class(speed):  # Объявление функции
#     if 1 <= speed <= 4:
#         return "weak"
#     elif 5 <= speed <= 10:
#         return "moderate"
#     elif 11 <= speed <= 18:
#         return "strong"
#     elif 18 <= speed:
#         return "hurricane"
# print(get_wind_class(14))  # Печатаем результат выполнения

# Задание 13.5.4
# Список login_list хранит имена пользователей, а словарь password_list хранит имена (ключи) и пароли (значения).
# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# login_list = list(user_database.keys())
# password_list = user_database
# username = input("Username:")
# password = input("Password:")
# def check_user(username, password):
#     if username in user_database:
#         if password == username[username]:
#             return True
#         else:
#             return False
#     else:
#         return False

# Задание 13.5.5 Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.

# A = int(input("Введите число A:"))
# B = int(input("Введите число B:"))
# C = int(input("Введите число C:"))
# if ((A < 45) and (B >= 45) and (C >= 45)) or ((B < 45) and (A >= 45) and (C >= 45)) or ((C < 45) and (A >= 45) and (B >= 45)):
#     print ("Есть одно число меньше 45")
# else:
#     print("Числа меньше 45 нет или их несколько")

# 13.6 Циклы

# time = 0
# while (true) do
#     {wait (1)
#      print(time)}

# words = {лягушка, собака, кошка, слон, попугай}
# word = 0
#     print(words[word]), word = word + 1
#     while (words[word] != слон):

# КОНСТРУКЦИЯ
# S = 0
# N = 5
# for i in range(1, N+1):
#     print("Значение суммы на предыдущем шаге:", S)
#     print("Текущее число:", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# конструкция произведения
# Мой вариант:
# P = 1
# N = 5
# for i in range(1, N+1):
#     print("Значение произведения на предыдущем шаге:", P)
#     print("Текущее число:", i)
#     P = P * i  # Умножает текущее число i и перезаписываем значение произведения
#     print("Значение суммы после произведения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: Произведение чисел до", N, "=", P)

# 2 version
# P = 1
# N = 5
# for i in range(1, N):
#     P *= i
#
# print(P)

# задание 13.6.3
# A = int(input("Число:"))
# for i in range(1, A+1):
#     print(" *"*i)

# Цикл WHILE
# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# Задание 13.6.4 возведение в степень пока не наступит 1000
# S = int(input("введи число больше 2:"))
# while S ** 2 < 1000:
#     S += 1
#     print("еще нет 1000")
# print("результат:привысил 1000")
# print("количество возведений в степень:", S)

# решение SF
# n = 1
# while n ** 2 < 1000:
#     n += 1
#     print(n)


# n = 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#    print("Hello World")
#    n += 1
#    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
#        break

# Задание Напишите цикл с использованием бесконечного цикла whilе с постусловием,
# который возводит натуральные числа в квадрат, пока результат меньше 1000.
# my dicision
# n = int(input("число:"))
# while True:
#     n = n ** 2
#     print("ok")
#     n += 1
#     if n > 1000:
#         break
# SF diicision
# n = 1
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1

# МАТРИЦЫ
# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#
#
# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")


# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)

# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# a = '' # пустая строка
# # b = a or 1
# # print(b)

# a = ""
# b = "bar"
#
# print(1 and a or b)

# Задание 13.8.6
# пусть a и b - переменные, которые мы хотим проверить
# a = "n"
# b = "bar"
# if a and b: # проверка истинности обеих переменных
#     print("Обе переменные истинные")
#     print(a,b)

# Задание 13.8.7
# пусть a и b - переменные, которые мы хотим проверить
# a = ""
# b = "bar"
# if a and b :
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b) # печать значения одной переменной, которая является истинной

# задание 13.8.8 проверить, является ли оно целым, находится ли в определенном промежутке
# (например от 100 до 999 включительно), да еще и делится ли на 2 и 3 одновременно.
# A = int(input())
# if type(A) == int:
#     if 100 <= A <= 999:
#         if A % 2 == 0:
#             if A % 3 == 0:
#                 print("Число удовлетворяет условиям")
#             else:
#                 print("false")

# задание 13.8.10
# A = int(input())
# if type(A) == int and 100 <= A <= 999 and A % 2 == 0 and A % 3 == 0:
#     print("Число удовлетворяет условиям")
# else:
#     print("Число не удовлетворяет условиям")

# A = int(input())
# if all([type(A) == int, 100 <= A <= 999, A % 2 == 0, A % 3 == 0]):
#     print("Число удовлетворяет условиям")
# else:
#     print("Число не удовлетворяет условиям")

# Задание 13.8.11 Напишите программу, которая на вход принимает последовательность целых чисел, и возвращает
# True, если все числа ненулевые, и False, если хотя бы одно число равно 0.
# решение SF:
# L = list(map(int, input().split()))
# print(all(L))

# Задание 13.8.12:
# Напишите программу, которая на вход принимает последовательность целых чисел и возвращает True, если все числа
# равны нулю, и False, если найдется хотя бы одно ненулевое число. Разрешается использование только логических
# операторов и функций all([ ]) и any([ ]).

# L = int(input())
# if all ([list(map(L)) != 0]):
#     if any([list(map(L)) == 0]):
#             print("ok")


# N = input("Напиши своё имя:")
# if N == "Никитка":
#     if input("Напиши сколько лет ты знаком со своей второй половинкой:") == "16":
#          print(N, ", с Днем Святого Валентина! Я люблю тебя!")
#     else:
#         print(N, ", не верно, попробуй еще раз")
# else:
#     print(N, "эта валентинка не для тебя!")

# print ("Это валентинка для особенного человека!")
# N = input("Напиши своё имя:")
# list_N = ["Nikitka", "Nikita", "Никитка", "Никита", "nikitka", "nikita", "никитка", "никита"]
# if N == any([list_N()]):
#     while \
#             input("Напиши сколько лет ты знаком со своей второй половинкой:") != "16":
#         print(N, ", не верно, попробуй еще раз")
#         if "16":
#             print(N, ", с Днем Святого Валентина! Я люблю тебя!")
#             break
# else:
#     print(N, "эта валентинка не для тебя!")

#Задание 13.8.13
#Задание на самопроверку.
#При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.

# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)

#задание 13.8.14
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)

L = [int(input()) % 2 == 0 for i in range(5)]
print(any(L))