# -*- coding: utf-8 -*-
import random


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    enlightenment_carma_level = 0

    with open('karma.log', 'w'):
        pass

    while enlightenment_carma_level < 777:
        dice = random.randint(1, 13)
        with open('karma.log', 'a+', encoding='utf-8') as karma:
            try:
                if dice == 1:
                    enlightenment_carma_level += 1
                    raise IamGodError('IamGodError')
            except IamGodError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 2:
                    enlightenment_carma_level += 2
                    raise DrunkError('DrunkError')
            except DrunkError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 3:
                    enlightenment_carma_level += 3
                    raise CarCrashError('CarCrashError')
            except CarCrashError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 4:
                    enlightenment_carma_level += 4
                    raise GluttonyError('GluttonyError')
            except GluttonyError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 5:
                    enlightenment_carma_level += 5
                    raise DepressionError('DepressionError')
            except DepressionError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 6:
                    enlightenment_carma_level += 6
                    raise SuicideError('SuicideError')
            except SuicideError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            else:
                if dice > 6:
                    enlightenment_carma_level += 7
                    print(dice)
            karma.close()


one_day()
