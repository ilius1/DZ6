a=int(input('Введите первый диапазон '))
b=int(input('Введите второй диапазон '))
d=0
for c1 in range(a,b+1):
    print(c1,end='\t')
print('\n')
for c2 in reversed(range(a,b+1)):
    print(c2, end='\t')
print('\n')
for c3 in range(a,b+1):
    if c3//7==c3/7:
        print(c3, end='\t')
print('\n')
for c4 in range(a,b+1):
    if c4//5==c4/5:
        d=d+1
print(d, end='\t')