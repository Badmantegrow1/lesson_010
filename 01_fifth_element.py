# -*- coding: utf-8 -*-

BRUCE_WILLIS = 42

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
except ValueError:
    print('Невозможно преобразовать к числу')
except IndexError:
    print('Выход за границы списка')
except NameError:
    print('Остальные исключения')
else:
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
