#1
dora1 = float(input("Введите первое вещественное число:"))
dora2 = float(input("Введите второе вещественное число:"))

if dora1 > dora2:
    max_dora = dora1
    min_dora = dora2
else:
    max_dora = dora2
    min_dora = dora1
print(f"Максимальное значение:{max_dora}")
print(f"Минимальное значение:{min_dora}")
#2
k = float(input("Введите сторону квадрата:"))
r = float(input("Введите радиус круга:"))
d = 2 * r 
if d <= k:
    print("круг вписывается в квадрат")
else:
    print("круг не вписыввается в квадрат")
№3
x=float(input("Ввод знач x:"))
y=x**2
if y<0:
    print("Значение функции y меньше 0")
else:
    print("Значение функции y не меньше 0")
№4
gomer = float(input("Введите длину квадрата:"))
bart = float(input("Введите радиус круга:"))
if gomer <= 2 * bart:
    print("Квадрат впишется")
else:
    print("квадрат не впишется")
№5
j = float(input("Введите первое число:"))
w = float(input("Введите второе число:"))
max_num = max(j,w)
print(max_num)
    
    