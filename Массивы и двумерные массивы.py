data=['folder','coursework.doc','folder','pict.png','data.accdb'], ['icon.ico', 'script.js', 'index.html','style.css','prog.py'],['my_song.mp3','anapa-2003.jpg','cs_1.6.exe','folder','cheat.txt'],['notes.txt','main.py','work.pdf','cartoon.mp4','array.py'],['project.psd','cycle.py','folder','cycle.js','turtle.py']

for row in data:
    print(row)

for row in data:
    for i in range(len(row)):
        if row[i]=="folder":
            row[i]=""
        elif row[i]=="data.accdb":
            row[i]="data.sql"
print("Без папок и с заменой data:")
for row in data:
    print(row)
    
extension_py=[]
for row in data:
    for item in row:
        if isinstance(item, str) and item.endswith(".py"):
            extension_py.append(item)
print("Все файлы.py")
print(extension_py)

for i in data:
    for item in i:
        if '.js' in item:
            print("все файлы.js:","new_"+item)


word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

n = int(input("Введите число от 0 до 9: "))

if 0 <= n <= 9:
    for i in range(n + 1):
        print(word_numb[i])
else:
    print("Введите число <= 9")


bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
decimal_list = []
for binary_num in bin_sy:
    decimal_num = int(binary_num, 2) 
    decimal_list.append(decimal_num)
    print(decimal_num) 
max_decimal = max(decimal_list)  
min_decimal = min(decimal_list) 
print("Максимальное число:", max_decimal)
print("Минимальное число:", min_decimal)



A = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, 'error', 8]
]

for i, row in enumerate(A):
    for j, element in enumerate(row):
        if isinstance(element, str):  
            A[i][j] = len(element) 

print("Исправленная матрица:")
for row in A:
    print(row)

total_sum = sum(sum(row) for row in A)

print("Сумма всех элементов матрицы:", total_sum)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total_sum = sum(matrix[i][2 - i] for i in range(3))
print("Сумма чисел по диагонали справа налево:", total_sum)
