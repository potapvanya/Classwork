import math

def area_triangle(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    s = (a + b + c) / 2

    return math.sqrt(s * (s - a) * (s - b) * (s - c))

x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4

result = area_triangle(x1, y1, x2, y2, x3, y3)
print(f"Площадь треугольника равна: {result}")




array = [int(input("Введите число: ")) for _ in range(15)]

zero_indices = [i for i, num in enumerate(array) if num == 0]
last_positive_index = max((i for i, num in enumerate(array) if num > 0), default=-1)

print(f"Номера всех нулевых элементов массива: {zero_indices}")
print(f"Номер последнего положительного элемента: {last_positive_index}")




array = [int(input("Введите число: ")) for _ in range(17)]
sum_elements = sum(array[:array.index(next(num for num in array if num < 0))])

print("Сумма всех элементов до первого отрицательного:", sum_elements)





z = [int(input(f"Введите элемент {i+1} первого массива: ")) for i in range(10)]
v = [int(input(f"Введите элемент {i+1} второго массива: ")) for i in range(10)]
if z == v:
    print("Массивы равны.")
else:
    print("Массивы неравны.")
if z != v:
    print("Массивы неравны.")
else:
    print("Массивы равны.")


arr = []
for i in range(20):
    arr.append(int(input("Введите элемент {}: ".format(i + 1))))
cat = []
for i in range(len(arr)):
    if arr[i] == 0:
        cat.append(i)

print("Индексы нулевых элементов:", cat)


