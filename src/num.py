from enum import Enum
from math import inf

from primes import PRIMES, PRIMES_MAX, PRIMES_TO


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

        for prime in PRIMES:
            while integer % prime == 0:
                if prime in self.primes:
                    self.primes[prime] += 1
                else:
                    self.primes[prime] = 1

                integer /= prime

            if integer <= 1:
                break

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

        raise NotImplementedError


if __name__ == '__main__':
    number = Num()

    number.set_num()
    print(number.primes)
    print(number.sign)
    print(number.case)

    number.set_num({})
    print(number.primes)
    print(number.sign)
    print(number.case)
