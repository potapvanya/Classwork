goroda = { 'Нижний Новгород': 470,
           'Самара': 1080,
           'Магнитогорск': 1690,
           'Омск': 2750,
           'Новосибирск': 3400,
           'Красноярск': 4200,
           'Благовещенск': 7800,
           'Анапа': 1530,
           'Астрахань': 1410,
           'Смоленск': 390
           }

print('Доступные города:')
for gorod in goroda.keys():
    print(gorod)
while True:
    turist = input('Выберите город:')
    if turist in goroda:
        print(f'От Москвы до {turist} - {goroda[turist]} км.')
        break
    else:
        print('Такого города нет в списке. Повторите ввод.')
