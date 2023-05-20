from enum import Enum
from math import inf, log10
from typing import Tuple

from src.primes.primes import PRIMES, PRIMES_TO


class Num:
    class Sign(Enum):
        POSITIVE = 1
        NEGATIVE = -1

    class Case(Enum):
        NUMBER = 1
        ZERO = 0
        INFINITY = 100
        UNDEFINED = None

    def __init__(self):
        """
        Initializes Num to UNDEFINED.
        """
        self.primes: dict[int, int] = {}
        self.sign: Num.Sign = Num.Sign.POSITIVE
        self.case: Num.Case = Num.Case.UNDEFINED

    def _modify_prime_factorization(self, integer: int, sign: Sign):
        if integer > PRIMES_TO:
            size_integer: int = int(log10(integer)) + 1
            size_primes: int = int(log10(PRIMES_TO)) + 1

            over: int = size_integer - size_primes + 1

            integer //= 10 ** over

            for prime in [2, 5]:
                if prime in self.primes:
                    self.primes[prime] += over * sign.value
                else:
                    self.primes[prime] = over * sign.value

        for prime in PRIMES:
            while integer % prime == 0:
                if prime in self.primes:
                    self.primes[prime] += 1 * sign.value
                else:
                    self.primes[prime] = 1 * sign.value

                integer /= prime

            if integer <= 1:
                break

    def _clean_values(self):
        if self.case is not Num.Case.NUMBER:
            self.primes: dict[int, int] = {}

            if self.case is Num.Case.INFINITY:
                return

            self.sign: Num.Sign = Num.Sign.POSITIVE
            return

        self.primes: dict[int, int] = {k: v for k, v in sorted(self.primes.items()) if v}

    def set_num(
            self,
            primes: dict[int, int] | None = None,
            sign: Sign = Sign.POSITIVE,
            case: Case = Case.NUMBER
    ) -> None:
        """
        Sets Num to Num components.
        :param primes: Dictionary of primes quantities
        :param sign: Sign of Num (+, -)
        :param case: Case of Num (NUMBER, ZERO, INFINITY, UNDEFINED)
        :return: None
        """
        self.primes: dict[int, int] = {}
        self.case: Num.Case = case

        if case is not Num.Case.NUMBER:
            if case is Num.Case.INFINITY:
                self.sign: Num.Sign = sign
            else:
                self.sign: Num.Sign = Num.Sign.POSITIVE

            return

        if primes is None:
            self.sign: Num.Sign = Num.Sign.POSITIVE
            self.case: Num.Case = Num.Case.UNDEFINED
        else:
            self.primes: dict[int, int] = primes.copy()
            self.sign: Num.Sign = sign

    def set_int(self, integer: int) -> None:
        """
        Sets Num to integer.
        :param integer: Integer to set Num to
        :return: None
        """
        self.primes: dict[int, int] = {}
        self.case: Num.Case = Num.Case.NUMBER

        if integer == 0:
            self.sign: Num.Sign = Num.Sign.POSITIVE
            self.case: Num.Case = Num.Case.ZERO

            return

        if integer < 0:
            integer *= -1
            self.sign: Num.Sign = Num.Sign.NEGATIVE
        else:
            self.sign: Num.Sign = Num.Sign.POSITIVE

        self._modify_prime_factorization(integer, Num.Sign.POSITIVE)

    def set_float(self, float_: float) -> None:
        """
        Sets Num to float.
        :param float_: Float to set Num to
        :return: None
        """
        self.primes: dict[int, int] = {}
        self.case: Num.Case = Num.Case.NUMBER

        if float_ == 0:
            self.sign: Num.Sign = Num.Sign.POSITIVE
            self.case: Num.Case = Num.Case.ZERO

            return

        if float_ == inf:
            self.sign: Num.Sign = Num.Sign.POSITIVE
            self.case: Num.Case = Num.Case.INFINITY

            return

        if float_ == -inf:
            self.sign: Num.Sign = Num.Sign.NEGATIVE
            self.case: Num.Case = Num.Case.INFINITY

            return

        if float_ < 0:
            float_ *= -1
            self.sign: Num.Sign = Num.Sign.NEGATIVE
        else:
            self.sign: Num.Sign = Num.Sign.POSITIVE

        numerator, denominator = float_.as_integer_ratio()
        self._modify_prime_factorization(numerator, Num.Sign.POSITIVE)
        self._modify_prime_factorization(denominator, Num.Sign.NEGATIVE)

        self._clean_values()

    def set_fraction(self, numerator: int, denominator: int) -> None:
        self.primes: dict[int, int] = {}
        self.case: Num.Case = Num.Case.NUMBER

        if denominator == 0:
            self.sign: Num.Sign = Num.Sign.POSITIVE
            self.case: Num.Case = Num.Case.UNDEFINED

            return

        if numerator == 0:
            self.sign: Num.Sign = Num.Sign.POSITIVE
            self.case: Num.Case = Num.Case.ZERO

            return

        if (numerator < 0) ^ (denominator < 0):
            self.sign: Num.Sign = Num.Sign.NEGATIVE
        else:
            self.sign: Num.Sign = Num.Sign.POSITIVE

        if numerator < 0:
            numerator *= -1

        if denominator < 0:
            denominator *= -1

        self._modify_prime_factorization(numerator, Num.Sign.POSITIVE)
        self._modify_prime_factorization(denominator, Num.Sign.NEGATIVE)

        self._clean_values()

    def get_float(self) -> int | float | None:
        if self.case is not Num.Case.NUMBER:
            if self.case is Num.Case.ZERO:
                return 0

            if self.case is Num.Case.INFINITY:
                return float('inf') * self.sign.value

            if self.case is Num.Case.UNDEFINED:
                return None

        out: float = self.sign.value

        for prime in self.primes:
            if self.primes[prime] > 0:
                out *= prime ** self.primes[prime]
            else:
                out /= prime ** -self.primes[prime]

        return out

    def get_fraction(self) -> tuple[int, int] | tuple[float, int] | None:
        if self.case is not Num.Case.NUMBER:
            if self.case is Num.Case.ZERO:
                return 0, 1

            if self.case is Num.Case.INFINITY:
                return float('inf') * self.sign.value, 1

            if self.case is Num.Case.UNDEFINED:
                return None

        numerator: int = self.sign.value
        denominator: int = 1

        for prime in self.primes:
            if self.primes[prime] > 0:
                numerator *= prime ** self.primes[prime]
            else:
                denominator *= prime ** -self.primes[prime]

        return numerator, denominator


if __name__ == '__main__':
    number = Num()

    number.set_float(-18 / -11)
    print(number.primes)
    print(number.sign)
    print(number.case)
    print()
    print(number.get_float())
    print(-18 / -11)

# http://www.java2s.com/Tutorials/Python/Class/Overload_divide_operator.htm
# https://www.geeksforgeeks.org/operator-overloading-in-python/

# https://t5k.org/lists/small/millions/
# https://t5k.org/notes/faq/LongestList.html
# http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
