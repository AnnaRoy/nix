print('''2. Напишите template строки, который можно будет многократно переиспользовать,
 вставляя в него имя и фамилию человека. Используйте метод строки "format".''')

hello = 'Здравствуйте, уважаемый {0} {1}'.format('Петр', 'Иванович')
print(hello)

hello = 'Здравствуйте, уважаемый {name} {surname}'.format(name='Иван', surname='Петрович')
print(hello)

name_list = ['Петр Петрович', 'Генадий Иванович', 'Семен Семенович']
hello = 'Здравствуйте, уважаемый {name} '.format(name=name_list[2])

print(hello)

name_list = {
    'name': 'Петр',
    'surname': 'Семенович',
}
hello = 'Здравствуйте, уважаемый {name} {surname} '.format(name = name_list.get("name"),
                                                           surname = name_list.get('surname'))
print(hello)

name_list = ['Петр Петрович', 'Генадий Иванович', '    Семен Семенович', 'Зинаида Петровна',
             ' Михаил Генадьевич ', ' Анна Павловна ']
for x in name_list:
    x = x.strip()
    pre = x.endswith('а')
    if pre == True:
        print('Здравствуйте, уважаемая {name} '.format(name=x))
    else:
        print('Здравствуйте, уважаемый {name} '.format(name=x))





