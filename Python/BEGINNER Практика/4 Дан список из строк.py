print('''
Дан список из строк. Создайте однострочное решение (при помощи list comprehension), которое приведёт к 
верхнему регистру все строки, содержащие слово 'price')

''')


list_str = ['discount price', 'sale', 'price', 'percent', 'price sale', 'price падает вниз']
print([i.upper() if 'price' in i else i for i in list_str])
