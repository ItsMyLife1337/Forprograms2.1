a3 = int(input('Впишите a3 '))
a2 = int(input('Впишите a2 '))
a1 = int(input('Впишите a1 '))
b3 = int(input('Впишите b3 '))
b2 = int(input('Впишите b2 '))
b1 = int(input('Впишите b1 '))

c3 = a3+b3 + ((a2+b2 + (a1+b1)//10) // 10)
c2 = (a2 + b2 + (a1 + b1) // 10) % 10
c1 = (a1 + b1) % 10

print(c3, c2, c1)
