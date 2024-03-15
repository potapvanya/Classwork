a =int(input("Номер элемента ряда Фибоначчи: "))
kek1 = 0
lol2 = 1
print(kek1)
print(lol2)
i = 2
while i < a:
    s = kek1 + lol2
    print(s)
    kek1 = lol2
    lol2 = s
    i = i + 1
print("Значение этого элемента:", lol2)