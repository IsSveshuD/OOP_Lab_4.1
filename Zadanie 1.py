#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Equation:
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def read(self):
        self.first = float(input("Введите значение коэффициента A: "))
        self.second = float(input("Введите значение коэффициента B: "))

    def display(self):
        print(f"Уравнение y = {self.first}x + {self.second}")

    def function(self, x):
        return self.first * x + self.second


def make_equation(a, b):
    return Equation(a, b)


if __name__ == "__main__":
    equation = make_equation(2, 3)
    equation.read()
    equation.display()
    x = float(input("Введите значение x: "))
    result = equation.function(x)
    print(f"Значение функции y для x = {x} равно {result}")
