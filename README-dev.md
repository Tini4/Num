# Num

[![Pylint](https://github.com/Tini4/Num/actions/workflows/pylint.yml/badge.svg)](https://github.com/Tini4/Num/actions/workflows/pylint.yml)
[![CodeCov](https://codecov.io/gh/Tini4/Num/branch/master/graph/badge.svg?token=BILTI4331O)](https://codecov.io/gh/Tini4/Num)

Python precise number type.

## Why?

Because float:
```python
print(0.1 * 3.0)         # 0.30000000000000004
print(0.3)               # 0.3
print(0.1 * 3.0 == 0.3)  # False
```

## Installation

`pip install num-tini4`

## Usage

```python
# Importing the Num class from the library
from src.num_tini4.num import Num

# Declaring variables
num1: Num = Num()
num2: Num = Num()

# Defining variables
num1.set_fraction(1, 11)  # 1/11
num2.set_int(-18)         # -18

print(num1)  # [NUMBER, POSITIVE, {11: -1}, {'pi': 0, 'e': 0, 'root': 1}]
print(num2)  # [NUMBER, NEGATIVE, {2: 1, 3: 2}, {'pi': 0, 'e': 0, 'root': 1}]

print(repr(num1))  # Num(primes={11: -1}, special={'pi': 0, 'e': 0, 'root': 1}, sign=<Sign.POSITIVE: 1>, case=<Case.NUMBER: 1>)
print(repr(num2))  # Num(primes={2: 1, 3: 2}, special={'pi': 0, 'e': 0, 'root': 1}, sign=<Sign.NEGATIVE: -1>, case=<Case.NUMBER: 1>)

print(float(num1))  # 0.09090909090909091
print(float(num2))  # -18.0

# Operations
print((num1 + num2).get_fraction())  # (-197, 11)
print((num1 + num2).get_float())     # -17.90909090909091
print((1/11) + -18.0)                # -17.90909090909091
print('--------------------------------------------------')

print((num1 - num2).get_fraction())  # (199, 11)
print((num1 - num2).get_float())     # 18.09090909090909
print((1/11) - -18.0)                # 18.09090909090909
print('--------------------------------------------------')

print((num1 * num2).get_fraction())  # (-18, 11)
print((num1 * num2).get_float())     # -1.6363636363636365
print((1/11) * -18.0)                # -1.6363636363636365
print('--------------------------------------------------')

print((num1 / num2).get_fraction())  # (-1, 198)
print((num1 / num2).get_float())     # -0.00505050505050505
print((1/11) / -18.0)                # -0.005050505050505051
print('--------------------------------------------------')

print((num1 ** num2).get_fraction())  # (5559917313492231481, 1)
print((num1 ** num2).get_float())     # 5.559917313492231e+18
print((1/11) ** -18.0)                # 5.559917313492229e+18
print('--------------------------------------------------')


print()
print(abs(num1))

num1.set_float(18 / 11)
print(18 / 11)
print(num1.get_float())
print(num1)
print(num1.get_fraction())
print()

num1.set_float(-18 / 11)

print(num1)
print(num1.get_float())
print(-18 / 11)

num1.set_int(3)
num2.set_int(2)
print((num1 ** num2).get_float())
```

## 1
- http://www.java2s.com/Tutorials/Python/Class/Overload_divide_operator.htm
- https://www.geeksforgeeks.org/operator-overloading-in-python/

## 2
- https://t5k.org/lists/small/millions/
- https://t5k.org/notes/faq/LongestList.html
- http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php