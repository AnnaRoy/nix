print('''Напишите функцию, которая будет преобразовывать цену к формату, отображающему до двух знаков после точки,
 например:
22.32131 -> 22.32
58.60125 -> 58.6
34.0 -> 34

'''
      )


def float_numb(x):
    x = round(x, 2)
    x = str(x)
    if x.endswith('.0'):
        x = x.strip('.0')
        print(int(x))
    else:
        print(float(x))


numbers = [222.55555555, 22.32131, 58.60125, 34.0, 444.00]

for x in numbers:
    float_numb(x)
