1. 
todo_list = ["Приготовить завтрак", "Сходить в магазин", "Выполнить домашнее задание"]
for item in todo_list:
    print(item)
todo_list.append("Погулять с собакой")
print(todo_list)
for item in todo_list:
    print(item)
2.
shopping_list = ["Яблоки", "Молоко", "Хлеб", "Мясо", "Яйца"]
for item in shopping_list:
    if item == "Молоко" or item == "Яйца":
        print(f"Купить {item} в количестве 2 шт.")
    else:
        print(f"Купить {item} в количестве 1 шт.)
3.
n = int(input("Введите число"))
x = ""
for i in range(1, n+1):
    x = x + str(i)
    print(x)
Доп. Задание
password_list = ["qwerty123", "qwerty", "qwe"]
password = input("Введите пароль")
for item in password_list:
    if item == password and item == "qwerty123":
        print("Пароль верный, доступ 3")
    elif item == password and item == "qwerty":
        print("Пароль верный, доступ 2")
    elif item == password and item == "qwe":
        print("Пароль верный, доступ 1")

1.
string = input("Введите строку:")
print("Используется цикл while:0")
i = 0
while i < len(string):
    print(f"{string[i]} : {ord(string[i])}")
    i += 1
print("\nИспользование цикла for:")
for char in string:
    print(f"{char} : {ord(char)}")
2.
n = int(input("Введите число больше нуля"))
while n <= 0:
    print("Число меньше нуля")
    n = int(input("Введите число больше нуля"))
sum_of_squares = 0
for i in range(1, n+1):
    sum_of_squares += i**2
print("Сумма квадратов числа от 0 до", n, "это", sum_of_squares)
3.
word = "бензин"
i = 3
while i > 0:
    w1 = input("Введите слово")
    if w1 == word:
        print("Вы угадали слово, количество попыток:", (3 - i) + 1)
        break
    else:
        print("Неверное слово, 1 буква - б")
        i -= 1
        print("Осталось попыток:", i)
    if i == 0:
        print("Попытки закончились, слово - бензин")
1.
all_keys = ['red key', 'blue key', 'golden key', 'red key', 'blue key', 'white key', 'golden key']
i = 0
for item in all_keys:
    if item == "golden key":
        i += 1
        print("True,", "встречается раз:", i)
2.
message = '6_185+_7*/#4i/*(@n'
m = ""
for i in message:
    if i == "7":
        m += "п"
    elif i == "1":
        m += "т"
    elif i == "n":
        m += "!"
    elif i == "+":
        m += "я"
    elif i == "i":
        m += "и"
    elif i == "/":
        m += "л"
    elif i == "(":
        m += "с"
    elif i == "5":
        m += "б"
    elif i == "6":
        m += "у"
    elif i == "_":
        m += " "
    elif i == "*":
        m += "о"
    elif i == "8":
        m += "е"
    elif i == "#":
        m += "у"
    elif i == "4":
        m += "ч"
    elif i == "@":
        m += "ь"
print(m)
3.
count = 0
while count < 4:
    p1 = int(input("Введите 1 сторону 1 прямоугольника"))
    p12 = int(input("Введите 2 сторону 1 прямоугольника"))
    p2 = int(input("Введите 1 сторону 2 прямоугольника"))
    p21 = int(input("Введите 2 сторону 2 прямоугольника"))
    if p1 <= 0:
        print("Какая-то из сторон меньше или равна нулю. Повторите ввод!")
    else:
        count += 1
    if p12 <= 0:
        print("Какая-то из сторон меньше или равна нулю. Повторите ввод!")
    else:
        count += 1
    if p2 <= 0:
        print("Какая-то из сторон меньше или равна нулю. Повторите ввод!")
    else:
        count += 1
    if p21 <= 0:
        print("Какая-то из сторон меньше или равна нулю. Повторите ввод!")
    else:
        count += 1
p3 = (p1 * p12)
p4 = (p2 * p21)
if p3 == p4:
    print("Они одинаковы")
elif p3 < p4:
    print("2 прямоугольник больше")
else:
    print("1 прямоугольник больше")
1.
random_string = 'f1ix_ER8ROR_in_l1ine_&_an7d_B8UG._in_C61o0de!'
correct_string = ""
i = 0

for item in random_string:
    if item not in ("01234567890&."):
        correct_string = correct_string + item
correct_string1 = correct_string.replace("_", " ")
correct_string2 = correct_string1.replace("  ", "")
print(correct_string2)
2.
word = input("Введите слово")
a = (ёуеаоэяию)
count = 0
for item in word:
    if item in a:
        count += 1
print(count)
3.
random_elements = [3, 6, -9, '-5', 'str', list, 'elem', None, -1, 10, str]
count = 0
b = ""
for a in random_elements:
    if isinstance(a, int):
        count += 1
        if a < 0:
            count -= 1
print(count, -9-5-1)
4.
n = int(input("Введите число"))
for i in range (1, 11):
    print(i * (n-1))
    print(i * n)
    print(i * (n+1))
5.
i = 0
while i < 50:
    a = int(input("Введите число"))
    if i < 50:
        i += a
