def  churikov(a):
    b=""
    for i in a:
        if i.isupper():
            b += i
    return b

f = 'PriVet'
g = churikov(f)
print(g)
    
    
def bear(txt):
    a = ['!', '?', '.', ',', '(',')']
    b = 0
    
    for i in txt:
        if i in a:
            b += 1
            
    return b 
    
kik = '(Как дела?)'
car = bear(kik)
print(car)