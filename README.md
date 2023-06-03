# Num

[![Pylint](https://github.com/Tini4/Num/actions/workflows/pylint.yml/badge.svg)](https://github.com/Tini4/Num/actions/workflows/pylint.yml)
[![CodeCov](https://codecov.io/gh/Tini4/Num/branch/master/graph/badge.svg?token=BILTI4331O)](https://codecov.io/gh/Tini4/Num)

Python precise number type.

[![CC BY-NC-ND](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

## Why?

Because float:
```python
print(0.1 * 3.0)         # 0.30000000000000004
print(0.3)               # 0.3
print(0.1 * 3.0 == 0.3)  # False
```

## Installation

```
pip install num-tini4
```

## Usage

```python
# Import the Num class
from num_tini4.num import Num


# Declare variables
num1: Num = Num()
num2: Num = Num()


# Define variables
num1.set_fraction(1, 11)  # 1/11
num2.set_int(-18)         # -18

print(num1)  # [NUMBER, POSITIVE, {11: -1}]
print(num2)  # [NUMBER, NEGATIVE, {2: 1, 3: 2}]

print(repr(num1))  # Num(primes={11: -1}, sign=<Sign.POSITIVE: 1>, case=<Case.NUMBER: 1>)
print(repr(num2))  # Num(primes={2: 1, 3: 2}, sign=<Sign.NEGATIVE: -1>, case=<Case.NUMBER: 1>)

print(float(num1))  # 0.09090909090909091
print(float(num2))  # -18.0


# Arithmetic Operators
print((num1 + num2).get_fraction())  # (-197, 11)
print((num1 + num2).get_float())     # -17.90909090909091
print((1 / 11) + -18.0)              # -17.90909090909091
print('--------------------------------------------------')

print((num1 - num2).get_fraction())  # (199, 11)
print((num1 - num2).get_float())     # 18.09090909090909
print((1 / 11) - -18.0)              # 18.09090909090909
print('--------------------------------------------------')

print((num1 * num2).get_fraction())  # (-18, 11)
print((num1 * num2).get_float())     # -1.6363636363636365
print((1 / 11) * -18.0)              # -1.6363636363636365
print('--------------------------------------------------')

print((num1 / num2).get_fraction())  # (-1, 198)
print((num1 / num2).get_float())     # -0.00505050505050505
print((1 / 11) / -18.0)              # -0.005050505050505051
print('--------------------------------------------------')


# todo: Assignment Operators
#  +=, -=, *=, /=


# todo: Comparison Operators
#  <, >, <=, >=, ==, !=


# Other
# -, abs(), float()


# Inaccurate!!! Slow!!! Avoid!!!
num1.set_float(18 / 11)
print(num1)                 # [NUMBER, POSITIVE, {2: -52, 19: 1, 26041: 1, 14894582557: 1}]
print(num1.get_fraction())  # (7369526662969903, 4503599627370496)
print(num1.get_float())     # 1.6363636363636365
print(18 / 11)              # 1.6363636363636365
```
