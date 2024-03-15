1
word="Программирование"
w1=word[7]+word[8]+word[9]
print(w1)
w2=word[3]+word[4]+word[5]+word[6]+word[7]
print(w2)
w3=word[1]+word[2]+word[3]
print(w3)
w4=word[0]+word[1]+word[2]+word[3]+word[4]+word[5]+word[6]+word[7]+word[12]
print(w4)
w5=word[0]+word[8]+word[9]
print(w5)

2
s=input("Введите строку:")
print (s[::2])

3
s=input("Введите строку:")
print (s[1:5])

4
s=input("Введите строку:")
if s[0]==s[1]:
    print("True")
else:
    print("False")