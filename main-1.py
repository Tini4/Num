from enum import Enum

PRIMES: list[int] = [2, 3, 5, 7, 11, 13]


# noinspection DuplicatedCode
class Num:
    """
    Num class for precise calculations.

    TODO:
     delete values in primes dict with 0
    """
    class Sign(Enum):
        POSITIVE = 1
        NEGATIVE = -1
        SPECIAL = 0

    class Case(Enum):
        ZERO = 0
        INFINITY = 1
        UNDEFINED = -1

    def __init__(self):
        """
        Initializes Num to UNDEFINED.
        """
        self.primes: dict[int, int] = {}
        self.sign: Num.Sign = Num.Sign.SPECIAL
        self.case: Num.Case = Num.Case.UNDEFINED

    def set_num(self, primes: dict[int, int] = None, sign: Sign = Sign.SPECIAL, case: Case = None) -> None:
        self.primes: dict[int, int] = {}

        if case is None:
            self.case: Num.Case = Num.Case.UNDEFINED
        else:
            self.sign: Num.Sign = Num.Sign.SPECIAL
            self.case: Num.Case = case

            return

        if primes is None:
            self.sign: Num.Sign = Num.Sign.SPECIAL
            self.case: Num.Case = Num.Case.UNDEFINED
        else:
            self.primes: dict[int, int] = primes.copy()
            self.sign: Num.Sign = sign

    def set_int(self, integer: int) -> None:
        self.primes: dict[int, int] = {}

        if integer == 0:
            self.sign: Num.Sign = Num.Sign.SPECIAL
            self.case: Num.Case = Num.Case.ZERO

            return
        self.case: Num.Case = Num.Case.UNDEFINED

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

    # def set_int(self, integer: int, sign: Sign = None, case: Case = None) -> None:
    #     self.primes: dict[int, int] = {}
    #
    #     if case is None:
    #         self.case: Num.Case = Num.Case.UNDEFINED
    #     else:
    #         self.sign: Num.Sign = Num.Sign.SPECIAL
    #         self.case: Num.Case = case
    #
    #         return
    #
    #     if integer == 0:
    #         self.sign: Num.Sign = Num.Sign.SPECIAL
    #         self.case: Num.Case = Num.Case.ZERO
    #
    #         return
    #
    #     if sign is None:
    #         if integer < 0:
    #             self.sign: Num.Sign = Num.Sign.NEGATIVE
    #         else:
    #             self.sign: Num.Sign = Num.Sign.POSITIVE
    #     else:
    #         self.sign: Num.Sign = sign
    #
    #     if integer < 0:
    #         integer *= -1
    #
    #     for prime in PRIMES:
    #         while integer % prime == 0:
    #             if prime in self.primes:
    #                 self.primes[prime] += 1
    #             else:
    #                 self.primes[prime] = 1
    #
    #             integer /= prime
    #
    #         if integer <= 1:
    #             break

    def set_float(self, float_: float) -> None:
        raise NotImplementedError  # TODO

    def set_fraction(self, numerator: int, denominator: int) -> None:
        # TODO: 0
        if denominator < 0:
            raise AttributeError('Denominator can\'t be negative!')  # TODO: a^b
        if denominator == 0:
            raise AttributeError('Denominator can\'t be zero!')  # TODO: UNDEFINED

        self.primes: dict[int, int] = {}
        self.sign: bool = True

        if (numerator < 0) ^ (denominator < 0):
            self.sign: Num.Sign = Num.Sign.NEGATIVE
        else:
            self.sign: Num.Sign = Num.Sign.POSITIVE

        if numerator < 0:
            numerator *= -1

        if denominator < 0:
            denominator *= -1

        for prime in PRIMES:
            while numerator % prime == 0:
                if prime in self.primes:
                    self.primes[prime] += 1
                else:
                    self.primes[prime] = 1

                numerator /= prime

            if numerator <= 1:
                break

        for prime in PRIMES:
            while denominator % prime == 0:
                if prime in self.primes:
                    self.primes[prime] -= 1
                else:
                    self.primes[prime] = -1

                denominator /= prime

            if denominator <= 1:
                break

    def get_float(self) -> float:
        out: float = 1 if self.sign else -1

        for prime in self.primes:
            if self.primes[prime] > 0:
                out *= prime ** self.primes[prime]
            else:
                out /= prime ** -self.primes[prime]

        return out

    def get_fraction(self) -> tuple[int, int]:
        numerator: int = 1 if self.sign else -1
        denominator: int = 1

        for prime in self.primes:
            if self.primes[prime] > 0:
                numerator *= prime ** self.primes[prime]
            else:
                denominator *= prime ** -self.primes[prime]

        return numerator, denominator

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        out: Num = Num()
        out.set_num(other.primes, not other.sign ^ self.sign)

        for prime in self.primes:
            if prime in out.primes:
                out.primes[prime] += self.primes[prime]
            else:
                out.primes[prime] = self.primes[prime]

        return out

    def __truediv__(self, other):
        out: Num = Num()
        out.set_num(other.primes, not other.sign ^ self.sign)

        for prime in self.primes:
            if prime in out.primes:
                out.primes[prime] -= self.primes[prime]
            else:
                out.primes[prime] = -self.primes[prime]

        return out

    def __mod__(self, other):
        pass

    def __cmp__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass


if __name__ == '__main__':
    number1 = Num()
    number1.set_num({2: 1, 3: 1}, False)
    number2 = Num()
    number2.set_fraction(4, 1)
    # print(number1.primes)
    # print(number2.primes)
    # print(number.get_float())
    # print(numpy.prod([2,3,5,7,11,13]))
    number3: Num = number1 * number2
    number4: Num = number1 / number2
    # print(number3.primes)
    print('\nnum3')
    print(number3.get_fraction())
    print(number3.get_float())
    print('\nnum4')
    print(number4.get_fraction())
    print(number4.get_float())

# http://www.java2s.com/Tutorials/Python/Class/Overload_divide_operator.htm
# https://www.geeksforgeeks.org/operator-overloading-in-python/
