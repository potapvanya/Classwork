1.
a= ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']

a.remove(0.25)
a.remove(15)
a.remove('10')

print(a)


2.
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

del abc[1:-2]
print(abc)


3.

numbers = [1, 4]
for i in range(numbers[-1]-1, numbers[0], -1): 
    numbers.insert(1, i)  
print(numbers)

4.

mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass = [x for x in mass if x >= 0]
sorted_asc = sorted(mass)
sorted_desc = sorted(mass, reverse=True)
print(sorted_asc) 
print(sorted_desc)

5.

m1 = []
m2 = []
m3 = []
n = int(input("Введите количество чисел"))
for item in range(1, n+1):
    n1 = int(input("Введите число"))
    if n1 > 0:
        m1.append(n1)
    elif n1 == 0:
        n1 = '*'
        m2.append(n1)
    else:
        m3.append(n1)
sum_neg = sum(m3)
print(sum_neg)
arif_pol = sum(m1) / len(m1)
print(arif_pol)
print("Количество звезд:", len(m2), m2)
