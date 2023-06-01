# Num

[![Pylint](https://github.com/Tini4/Num/actions/workflows/pylint.yml/badge.svg)](https://github.com/Tini4/Num/actions/workflows/pylint.yml)
[![CodeCov](https://codecov.io/gh/Tini4/Num/branch/master/graph/badge.svg?token=BILTI4331O)](https://codecov.io/gh/Tini4/Num)

Python precise number type.

## Installation

`pip install num-tini4`

## Usage

```
# Import the Num class from the library.
from num_tini4.num import Num

# Declare variables.
number1: Num = Num()
number2: Num = Num()

# Define variables.
number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)  # 18
number2.set_num({11: -1})  # 1/11

print((number2 + number1).get_fraction())  # 199/11
print()
print(abs(number1))

number1.set_float(18 / 11)
print(18 / 11)
print(number1.get_float())
print(number1)
print(number1.get_fraction())
print()

number1.set_float(-18 / 11)

print(number1)
print(number1.get_float())
print(-18 / 11)

number1.set_int(3)
number2.set_int(2)
print((number1 ** number2).get_float())
```

## 1
- http://www.java2s.com/Tutorials/Python/Class/Overload_divide_operator.htm
- https://www.geeksforgeeks.org/operator-overloading-in-python/

## 2
- https://t5k.org/lists/small/millions/
- https://t5k.org/notes/faq/LongestList.html
- http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
