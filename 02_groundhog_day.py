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
    while enlightenment_carma_level < 777:
        dice = random.randint(1, 13)
        try:
            if dice == 1:
                enlightenment_carma_level += 1
                raise IamGodError('Я Бог')
        except IamGodError as exc:
            print(f'Поймано исключение {exc}')
        try:
            if dice == 2:
                enlightenment_carma_level += 2
                raise DrunkError('Напился')
        except DrunkError as exc:
            print(f'Поймано исключение {exc}')
        try:
            if dice == 3:
                enlightenment_carma_level += 3
                raise CarCrashError('Разбился на машине')
        except CarCrashError as exc:
            print(f'Поймано исключение {exc}')
        try:
            if dice == 4:
                enlightenment_carma_level += 4
                raise GluttonyError('Обожрался')
        except GluttonyError as exc:
            print(f'Поймано исключение {exc}')
        try:
            if dice == 5:
                enlightenment_carma_level += 5
                raise DepressionError('Депресняк')
        except DepressionError as exc:
            print(f'Поймано исключение {exc}')
        try:
            if dice == 6:
                enlightenment_carma_level += 6
                raise SuicideError('Суицид')
        except SuicideError as exc:
            print(f'Поймано исключение {exc}')
        else:
            if dice > 6:
                enlightenment_carma_level += 7
                print(dice)


one_day()
