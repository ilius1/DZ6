a=int(input('Введите первый диапазон '))
b=int(input('Введите второй диапазон '))
for c1 in range(a,b+1):
    if (c1//3==c1/3 and c1//5==c1/5):
        print('Fizz Buzz')
    elif c1//5==c1/5:
        print('Buzz ')
    elif  c1//3==c1/3:
        print('Fizz')
    else:
        print(c1)
input()