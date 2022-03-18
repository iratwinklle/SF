# 14.1.1 Напишите функцию print_2_add_2, которая будет складывать 2 и 2, а затем печатать этот результат
# мое решение:
# def print_2_add_2(x):
#     return x * x
# print(print_2_add_2(2))
# решение SF:
# def print_2_add_2():
#    result = 2 + 2
#    print(result)
# print_2_add_2()

# 14.1.2 hello_world
# def hello_world():
#     print("Hello world")
# hello_world()

# Задание 14.1.3 Напишите функцию, которая проверяет, является ли число n делителем числа a.
# И выводит на экран соответствующее сообщение, является ли число делителем или нет.

# def devisor_n(a, n):
#     if a % n == 0:
#         print("{} является делителем числа {}".format(n, a))
#     else:
#         print("{} не является делителем числа {}".format(n, a))
# devisor_n(5, 2)

# Задание 14.1.4 Напишите функцию, которая печатает «обратную лесенку» следующего типа:

# def ladder(n):
#     for i in range(n, 0, -1):
#         print("*" * i)
# ladder(7)
# print(ladder(4))

#Задание 14.1.5 Напишите функцию, которая будет возвращать количество делителей числа а.
# def number_of_devisor(a):
#     count = 0
#     for n in range(1, a+1):
#         if a % n == 0:
#             count += 1
#     return count
# print(number_of_devisor(5))

#Задание 14.1.6 проверка палиндром ли
# def palindrom(s):
#     new_s = s.replace(" ", "").lower()
#     if new_s == new_s[::-1]:
#         print("Фраза \"{}\" является палиндромом".format(s))
#     else:
#         print("Фраза \"{}\" не является палиндромом".format(s))
# palindrom("Кит на море не романтик")


# def pow_func(base, n=2):
#    inside_result = base ** n
#    return inside_result
#
# print(inside_result)

# x = 3
# def func():
#    global x
#    print(x)
#    x = 5
#    x += 5
#    return x
# print(func())

#Задание 14.2.2 Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
# def multipl(*nums):
#    p = 1
#    for n in nums:
#       p *= n
#    return p
# print(multipl(1, 2, 3, 4))

#Рекурсия. Числа Фибоначи
# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(10))

#14.2.3 С помощью рекурсивной функции найдите сумму чисел от 1 до n.
# def sum_all(n):
#    if n == 1:
#       return 1
#    else:
#       return n + sum_all(n-1)
# print(sum_all(6))

#14.2.5 сумма чисел числа N
# def sum_N(N):
#    if N < 10:
#       return N
#    else:
#       return N % 10 + sum_N(N // 10)
# print(sum_N(1421))

#Итератор
# для примера возьмём строку
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))

# def make_adder(x):
#    def adder(n):
#        return x + n # захват переменной "x" из nonlocal области
#    return adder
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105
#
# #Расчет врмемени на выполнение операции вычисления
# import time
# N = 100
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
# def pow_2():
#    return 10000000 ** 2
# def in_build_pow():
#    return pow(10000000, 2)
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
# in_build_pow()
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")

#14.5.1
# def linear_solve(a, b):
#    if a:
#       return b / a
#    elif not a and not b:  # снова используем числа в логических выражениях
#       return "Бесконечное количество корней"
#    else:
#       return "Нет корней"

#14.5.3 Функция D(a,b,c) возвращающая дискриминант квадратного уравнения. D = b**2 - 4*a*c - дискриминант
def quadratic_solve(a, b, c):
   if D(a, b, c) < 0:
      return "Нет вещественных корней"
   elif D(a, b, c) == 0:
      return -b / (2 * a)
   else:
      return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

#14.5.7
# разбили строку из input и преобразовали к float
# Ввод строки 1 0 -1
# L = list(map(float, input().split()))
# # Вывод [1.0, 0.0, -1.0]
# # [1, 0, -1] - например
# print(quadratic_solve(L[0], L[1], L[2]))
# # (-1.0, 1.0)
# print(quadratic_solve(*L))


# #14.6.1 помощью метода строки str.lower переведите все элементы списка в нижний регистр.
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))

# def positive(x):
#    return x % 2 == 0  # функция возвращает только True или False
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))  # [1, 2]

#14.6.5 посчитать длину каждого элемента в списке:
# a = ["asd", "bbd", "ddfa", "mcsa"]
# print(list(map(len, a)))

#14.6.6 перевести элементы в списке в верхний регистр
a = ["это", "маленький", "текст", "обидно"]
print(list(map(str.upper, a)))


