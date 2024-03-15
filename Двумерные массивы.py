1.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matrix:")
for row in matrix:
print(row)

odd_numbers = []
count_even = 0

for row in matrix:
for num in row:
if num % 2 != 0:
odd_numbers.append(num)
else:
count_even += 1

print("нечётные числа matrix")
print(" ".join(str(num) for num in odd_numbers))
print("кол-во чётных:", count_even)

2.
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
answer_matrix = [[0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(len(matrix_1)):
for j in range(len(matrix_1[0])):
answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]

print(answer_matrix)

for row in answer_matrix:
print(f'{row} сумма строки: {sum(row)}')

3.
fruits = [['Banana', 'apple'],
['apricot', 'Avocado'],
['lime', 'lemon'],
['Mango', 'grapes']]

for sublist in fruits:
for item in sublist:
if item[0].isupper():
print(item)

4.
random_elements = [['toy', 'bee', 'cheese', 'ear'],
                   [False, 'word', '0110110', 10],
                   ['happiness', '(」°ロ°)」', 'luck', None],
                   ['car', '<- code ->', 4.7, True]]

for row in random_elements:
    for index, element in enumerate(row):
        if index % 2 == 1:
            print(element)

5.
rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Введите значение элемента [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)
print("Ваш двумерный массив:")
for row in matrix:
    print(row)

