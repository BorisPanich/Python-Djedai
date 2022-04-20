# a = input('Ввод дела: ')
# b = input('количества раз: ')

# print(a * int(b))

# i = 3
# while i >= 0:
#     print(i)
#     i -= 1


# i = 0
# while i <= 10:
#     i += 1
#     if (i % 2) != 0:
#         continue;
#     print('Четное число ' + str(i))


# Итерация
# numbers = [1, 2, 3, 4, 5]
# i = 0

# for element in numbers:
#     print(element)

# length = len(numbers) - 1
# while i <= length:
#     print(numbers[i])
#     i += 1

# for test in range(4):
#     print('Hi')


# def min(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# x = float(input('Input x: '))
# y = float(input('Input y: '))
# print(min(x, y))
# print(min(5, 7))


''' Исключение '''
''' ImportError, IndexError, NameError, SyntaxError, TypeError, ValueError, ZeroDivisionError '''

# try:
#     print(7 / 0)
# except ZeroDivisionError:
#     pass
# print('Ошибка пропущена')

# try:
#     print(7 / 0)
# except:
#     raise
#     print('Test')
#     raise


''' Работа с файлами, assert(утверждение), len, with'''

# fileName = input('Укажите выбранный файл: ')
# file = open('test.txt')
# print('В выбранном вами файле ' + str(len(file.read())) + ' символов.')
# file.close()

# режимы чтения файлов:
# r - read
# w - write
# a - append
# b - binary

# w:
# fileName = input('Укажите выбранный файл: ')
# secondString = 'secondString: This is a test file for the theme 15.'
# # secondString = input('Введите новый текст для файла test.txt: ')
#
# file = open('test.txt', 'w')
# file.write(secondString)  # происходит перезапись содержимого текста
# file.close()


# a
# file = open('test.txt', 'a')
# file.write(' Test!')  # происходит добавления текста Test к содержимому
# file.close()

# b
# filename1 = input('Какой фойл хотите прочесть?: ')
# filename2 = 'backup_' + filename1
#
# file1 = open(filename1, 'rb')  # читается файл
# file2 = open(filename2, 'wb')
#
# file2.write(file1.read())  # перезаписывается в новый файл filename2 содержимое filename1
# file1.close()
# file2.close()
#
# print("Process accessed!")


# file = open('test.txt', 'r')
#
# strings = file.readlines() # построчное чтение
# for string in strings:
#     print(string)
# file.close()


# with
# with open('test.txt', 'r') as t:
#     print(t.read(10))  # читаются только первые 10 байт
#     print(t.read())  # выполняется оставшаяся часть файла


''' None, Dictionary '''

# def test():
#     print('Test')
#
# azaza = test()
# print(azaza)


# test = {
#     'key1': 'value1',
#     11: {
#         'short_value': 'eleven'
#     }
# }
#
# try:
#     print(test["test"])
#     # print(test["key1"])
# except KeyError:
#     print("not key")


# contacts = {
#     "Andry": "+25325413",
#     "Tony": "+253225558",
# }

# testing = input("Who is looking?: ")
#
# if testing in contacts:
#     print("Contact info: " + contacts[testing])
# else:
#     print("not finded contact")

# print(contacts["Andry T."])
# print(contacts.get("Andry T.", "not finded"))


''' Pass, Tuple (кортеж - списки, кот. нельзя изменять) '''

# def main():
#     pass
# print("проверка кода")

# #  это СПИСКИ
# numbers = [1, 2, 4, 32, 4, 5]
# numbers[0] = 0
# print(numbers[0])

#  это Кортеж
# numbers = (1, 2, 4, 32, 4, 5)
# numbers = 1, 2, 4, 32, 4, 5   # будет аналогично предедущей строке
# numbers[0] = 0                # не допустимо
# print(numbers[0])


''' Срез списков '''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# newNumbers = numbers[3:7]       # [4, 5, 6, 7]
# print(newNumbers)

# i = numbers[0:4]  # [:4]  =>  [1, 2, 3, 4]
# анологично:   for i in range(4):
# print(i)

# [: 5]  # с начала до 5 индекса (невключительно)
# [4:]  # с 4 до конца списка
#
# digit = range(2, 101)[::2]  # список с четными числами от 2 до 100
#
# [-3]              # 8
# [-3 - 2]          # 6
# [-3:]             # [8, 9, 10]

# реверсивный список:
# [::-1]
# [::-1][::-1]        # в реверс. и обратно
# [5:2:-2]            # -2 это шаг в обратном направлении
