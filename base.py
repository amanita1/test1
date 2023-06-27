print("Hello World!")



# переменные и типы данных
# int - integer - числа: 124, 1623, 1243265, 1, 4, 1246
# float - числа с плавающей запятой - 3.1415, 3.1337, 228.1
# bool - boolean - логическое значение - True, False 
# str - string - строка: "слово" "ыыыы"
# другие виды рассмотрим позже
a = 123412 #int
b = 3.141592 #float
c = True #bool
d = "Александр" #str






#################################################################
#                            операторы
# Арифметические
#   Сложение (+)
#   Вычитание (-)
#   Умножение (*)
#   Деление (/)
#   Возведение в степень (**)
#   Деление без остатка (//)
#   Деление по модулю (остаток от деления) (%)
# Операторы сравнения
#   Меньше (<)
#   Больше (>)
#   Меньше или равно (<=)
#   Больше или равно (>=)
#   Равно (==)
#   Не равно (!=)
# Операторы присваивания
#   Присваивание (=)
#   Сложение и присваивание (+=)
#   Вычитание и присваивание (-=)
#   Деление и присваивание (/=)
#   Умножение и присваивание (*=)
#   Деление по модулю и присваивание (%=)
#   Возведение в степень и присваивание (**=)
#   Деление с остатком и присваивание (//=)
# Логические операторы Python
#   И (and)
#   Или (or)
#   Не (not)
# Операторы тождественности
# Это (is)
# Это не (is not)
#################################################################
#                            ветвления
# if - если
# elif - также если
# else - во всех остальных случаях
# if a > b:
#     print("больше")
# elif a < b:
#     print("меньше")
# else:
#     print("равны")
#################################################################
#                            циклы
# while, for
# while - пока условие не будет выполненно (пока условие не вернёт True)
# пример:
# while a != 100:
#   a+=1
# пока а не равно 100 добавляем а по одному
# 
# for - повторяется столько раз (итераций), сколько скажут
# пример:
# for i in range (100):
# print(i)
# 
# 100 раз повторяем код: вывести i
# 
# 
# подробнее про range:
# 
# 
# range(количество итераций)
# range(начало отсчёта, конец, шаг)
# таким образом, если 
# range(0, 100, 5)
# начиная с нуля, добавляя по 5 идём до 100
#################################################################
#                            функции
# Функция — это многократно используемый блок кода
# ключевое слово для создания функции: def
# 
# синтаксис:
# def название функции(принимаемые параметры):
#   тело функции(код выполняемой функции)
#   return значение
# 
#################################################################
#                            list
# 
# list - тип данных, позволяющий хранить сразу несколько значений (не обязательно одного типа)
# 
# myList = [значение1, значение2, значение3 и так далее]
# 
# добавить элемент в список:
# myList + [значение]
# 
# удалить элемент:
# myList.remove(значение)
# del myList[индекс]
# myList.clear() - очистить список
# 
# что такое индекс?
# порядковый номер элемента (отсчёт начинается с нуля)
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myList[0] - выводит 1
# myList[9] - выводит 10
 