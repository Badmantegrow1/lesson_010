# -*- coding: utf-8 -*-

class NotEmailError(Exception):
    pass


class NotNameError(Exception):
    pass


with open('registrations.txt', 'r', encoding='utf-8') as lines:
    with open('registrations_good.log', 'w') as good:
        pass
    with open('registrations_bad.log', 'w') as bad:
        pass
    for line in lines:
        a = line.rstrip('\n')
        try:
            with open('registrations_bad.log', 'a+', encoding='utf-8') as bad:
                if len(a.split(' ')) == 3:
                    name, email, age = a.split(' ')
                    age = int(''.join(age for age in age if age.isdigit()))
                    if name.isalpha():
                        if '@' in a and '.' in a:
                            if 10 <= age <= 99:
                                with open('registrations_good.log', 'a+', encoding='utf-8') as good:
                                    good.write(f'{name} {email} {age}\n')
                            else:
                                try:
                                    raise ValueError()
                                except ValueError:
                                    bad.write(
                                        f'{a} Тип ошибки: ({ValueError.__name__}) - Поле возраст НЕ является числом '
                                        f'от 10 до 99\n')
                        else:
                            try:
                                raise NotEmailError()
                            except NotEmailError:
                                bad.write(f'{a} Тип ошибки: ({NotEmailError.__name__}) - Поле емейл НЕ содержит @ '
                                          f'и .(точку)\n')
                    else:
                        try:
                            raise NotNameError()
                        except NotNameError:
                            bad.write(f'{a} Тип ошибки: ({NotNameError.__name__}) - Поле имени содержит НЕ только '
                                      f'буквы\n')
                else:
                    if 1 < len(a.split(' ')) < 3:
                        try:
                            raise ValueError()
                        except ValueError:
                            bad.write(f'{a} Тип ошибки: ({ValueError.__name__}) - НЕ присутсвуют все три поля\n')
                    else:
                        try:
                            raise ValueError()
                        except ValueError:
                            bad.write(f'Тип ошибки: ({ValueError.__name__}) - Пустая строка\n')
        except ValueError:
            with open('registrations_bad.log', 'a+', encoding='utf-8') as bad:
                bad.write(f'{a} Тип ошибки: ({ValueError.__name__}) - Не верные данные\n')
good.close()
bad.close()
lines.close()
