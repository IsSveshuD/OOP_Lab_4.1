#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Money:
    def __init__(self, denominations=None):
        if denominations is None:
            self.denominations = {
                5000: 0,
                1000: 0,
                500: 0,
                100: 0,
                50: 0,
                10: 0,
                5: 0,
                2: 0,
                1: 0,
                0.5: 0,
                0.1: 0,
                0.05: 0,
                0.01: 0
            }
        else:
            self.denominations = denominations

    def read(self):
        print("Введите количество купюр/монет каждого номинала:")
        for denom in self.denominations.keys():
            self.denominations[denom] = int(input(f"{denom} рублей/копеек: "))

    def display(self):
        total = sum(denom * count for denom, count
                    in self.denominations.items())
        print(f"Общая сумма: {total:.2f} рублей".replace('.', ','))

    def add(self, other):
        result = Money()
        for denom in self.denominations.keys():
            result.denominations[denom] = self.denominations[denom] + \
                                          other.denominations[denom]
        return result

    def sub(self, other):
        result = Money()
        for denom in self.denominations.keys():
            result.denominations[denom] = self.denominations[denom] - \
                                          other.denominations[denom]
        return result

    def div(self, divisor):
        result = Money()
        for denom in self.denominations.keys():
            result.denominations[denom] = self.denominations[denom] / divisor
        return result

    def mul(self, multiplier):
        result = Money()
        for denom in self.denominations.keys():
            result.denominations[denom] = self.denominations[denom] \
                                          * multiplier
        return result

    def equals(self, other):
        if isinstance(other, Money):
            a = sum(denom * count for denom, count
                    in self.denominations.items())
            b = sum(denom * count for denom, count
                    in other.denominations.items())

            return a == b
        else:
            return False

    def less(self, other):
        if isinstance(other, Money):
            a = sum(denom * count for denom, count
                    in self.denominations.items())
            b = sum(denom * count for denom, count
                    in other.denominations.items())

            return a < b
        else:
            return False

    def greater(self, other):
        if isinstance(other, Money):
            a = sum(denom * count for denom, count in
                    self.denominations.items())
            b = sum(denom * count for denom, count in
                    other.denominations.items())

            return a > b
        else:
            return False


if __name__ == '__main__':
    money1 = Money()
    money1.read()
    money1.display()

    money2 = Money()
    money2.read()
    money2.display()

    result = money1.add(money2)
    print("\nСумма:")
    result.display()

    result = money1.sub(money2)
    print("\nРазница:")
    result.display()

    divisor = float(
        input("\nВведите число, на которое хотите разделить сумму: "))
    result = money1.div(divisor)
    print("\nРезультат деления:")
    result.display()

    multiplier = float(
        input("\nВведите число, на которое хотите умножить сумму: "))
    result = money1.mul(multiplier)
    print("\nРезультат умножения:")
    result.display()
