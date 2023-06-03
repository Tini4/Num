from enum import Enum
from math import inf, sqrt  # , log10

# noinspection PyUnresolvedReferences
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

    def __repr__(self):
        return f"Num(primes={self.primes!r}, sign={self.sign!r}, case={self.case!r})"

    def __str__(self):
        return f'[{self.case.name}, {self.sign.name}, {self.primes}]'

    def _modify_prime_factorization(self, integer: int, sign: Sign) -> None:
        """
        Modifies the primes' factorization.

        :param int integer: Number to be factorized
        :param Sign sign: Add or remove primes' quantities (+, -)
        :return: None
        """
        if integer < 2:
            return

        for i in range(2, int(sqrt(integer)) + 1):
            # Fast precision
            if integer <= PRIMES_TO:
                while integer > 1:
                    if PRIMES[integer] in self.primes:
                        self.primes[PRIMES[integer]] += 1 * sign.value
                    else:
                        self.primes[PRIMES[integer]] = 1 * sign.value

                    integer //= PRIMES[integer]

                break

            # Slow precision
            while integer % i == 0:
                if i in self.primes:
                    self.primes[i] += 1 * sign.value
                else:
                    self.primes[i] = 1 * sign.value

                integer //= i

        # Integer is a prime
        if integer > 1:
            if integer in self.primes:
                self.primes[integer] += 1 * sign.value
            else:
                self.primes[integer] = 1 * sign.value

    def _clean_values(self) -> None:
        """
        Handles cases, removes 0 values from primes and orders them.

        :return: None
        """
        if self.case is not Num.Case.NUMBER:
            self.primes: dict[int, int] = {}

            if self.case is Num.Case.INFINITY:
                return

            self.sign: Num.Sign = Num.Sign.POSITIVE
            return

        self.primes: dict[int, int] = {k: v for k, v in sorted(self.primes.items()) if v}

    def set_num(self, primes: dict[int, int] | None = None, sign: Sign = Sign.POSITIVE,
                case: Case = Case.NUMBER) -> None:
        """
        Sets Num to the Num components.

        :param dict[int, int] | None primes: Dictionary of primes' quantities
        :param Sign sign: Sign of Num (+, -)
        :param Case case: Case of Num (NUMBER, ZERO, INFINITY, UNDEFINED)
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
        Sets Num to an integer.

        :param int integer: Integer to set Num to
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
        Sets Num to a float.

        :param float float\_: Float to set Num to
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
        """
        Sets Num to a fraction.

        :param int numerator: Numerator to set Num to
        :param int denominator: Denominator to set Num to
        :return: None
        """
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

    def get_float(self) -> float:
        """
        Returns float value of Num

        :return: Value of Num
        :rtype: float
        """
        if self.case is not Num.Case.NUMBER:
            if self.case is Num.Case.ZERO:
                return 0.0

            if self.case is Num.Case.INFINITY:
                return float('inf') * self.sign.value

            if self.case is Num.Case.UNDEFINED:
                return float('nan')

        out: float = float(self.sign.value)

        for prime in self.primes:
            if self.primes[prime] > 0:
                out *= prime ** self.primes[prime]
            else:
                out /= prime ** -self.primes[prime]

        return out

    def get_fraction(self) -> tuple[int, int] | tuple[float, int] | None:
        """
        Returns fraction value of Num

        :return: Value of Num
        :rtype: tuple[int, int] | tuple[float, int] | None
        """
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

    def __mul__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

        out: Num = Num()

        if (self.case is Num.Case.UNDEFINED) or (other.case is Num.Case.UNDEFINED):
            out.set_num(case=Num.Case.UNDEFINED)

            return out

        if (self.case is Num.Case.ZERO) or (other.case is Num.Case.ZERO):
            out.set_num(case=Num.Case.ZERO)

            return out

        if (self.sign is Num.Sign.NEGATIVE) ^ (other.sign is Num.Sign.NEGATIVE):
            out.sign = Num.Sign.NEGATIVE
        else:
            out.sign = Num.Sign.POSITIVE

        if (self.case is Num.Case.INFINITY) or (other.case is Num.Case.INFINITY):
            out.case = Num.Case.INFINITY

            return out

        out.case = Num.Case.NUMBER
        out.primes = self.primes.copy()

        for prime in other.primes:
            if prime in out.primes:
                out.primes[prime] += other.primes[prime]
            else:
                out.primes[prime] = other.primes[prime]

        out._clean_values()

        return out

    def __truediv__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

        out: Num = Num()

        if (self.case is Num.Case.UNDEFINED) or (other.case is Num.Case.UNDEFINED) or (other.case is Num.Case.ZERO) or (
                (self.case is Num.Case.INFINITY) and (other.case is Num.Case.INFINITY)):
            out.set_num(case=Num.Case.UNDEFINED)

            return out

        if (self.case is Num.Case.ZERO) or (other.case is Num.Case.INFINITY):
            out.set_num(case=Num.Case.ZERO)

            return out

        if (self.sign is Num.Sign.NEGATIVE) ^ (other.sign is Num.Sign.NEGATIVE):
            out.sign = Num.Sign.NEGATIVE
        else:
            out.sign = Num.Sign.POSITIVE

        if self.case is Num.Case.INFINITY:
            out.case = Num.Case.INFINITY

            return out

        out.case = Num.Case.NUMBER
        out.primes = self.primes.copy()

        for prime in other.primes:
            if prime in out.primes:
                out.primes[prime] -= other.primes[prime]
            else:
                out.primes[prime] = -other.primes[prime]

        out._clean_values()

        return out

    def __add__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

        out: Num = Num()

        if (self.case is Num.Case.UNDEFINED) or (other.case is Num.Case.UNDEFINED):
            out.set_num(case=Num.Case.UNDEFINED)

            return out

        if self.case is Num.Case.ZERO:
            out.set_num(other.primes, sign=other.sign, case=other.case)

            return out

        if other.case is Num.Case.ZERO:
            out.set_num(self.primes, sign=self.sign, case=self.case)

            return out

        if (self.case is Num.Case.INFINITY) ^ (other.case is Num.Case.INFINITY):
            out.case = Num.Case.INFINITY

            if ((self.case is Num.Case.INFINITY) and (self.sign is Num.Sign.NEGATIVE)) or (
                    (other.case is Num.Case.INFINITY) and (other.sign is Num.Sign.NEGATIVE)):
                out.sign = Num.Sign.NEGATIVE

            return out

        if (self.case is Num.Case.INFINITY) and (other.case is Num.Case.INFINITY):
            if self.sign is not other.sign:
                out.set_num(case=Num.Case.UNDEFINED)

                return out

            out.set_num(self.primes, sign=self.sign, case=self.case)

            return out

        out.case = Num.Case.NUMBER

        a_numerator: dict[int, int] = self.primes.copy()
        b_numerator: dict[int, int] = other.primes.copy()
        denominator: dict[int, int] = {k: -v for k, v in self.primes.items() if v < 0}

        for prime in other.primes:
            if other.primes[prime] < 0:
                if prime in denominator:
                    denominator[prime] = max(denominator[prime], -other.primes[prime])
                else:
                    denominator[prime] = -other.primes[prime]

        for prime in denominator:
            if prime in a_numerator:
                a_numerator[prime] += denominator[prime]
            else:
                a_numerator[prime] = denominator[prime]

            if prime in b_numerator:
                b_numerator[prime] += denominator[prime]
            else:
                b_numerator[prime] = denominator[prime]

        a: int = 1
        b: int = 1

        for prime in a_numerator:
            a *= prime ** a_numerator[prime]

        for prime in b_numerator:
            b *= prime ** b_numerator[prime]

        out.set_int(a * self.sign.value + b * other.sign.value)

        for prime in denominator:
            if prime in out.primes:
                out.primes[prime] -= denominator[prime]
            else:
                out.primes[prime] = -denominator[prime]

        out._clean_values()

        return out

    def __sub__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

        out: Num = Num()

        if (self.case is Num.Case.UNDEFINED) or (other.case is Num.Case.UNDEFINED):
            out.set_num(case=Num.Case.UNDEFINED)

            return out

        if self.case is Num.Case.ZERO:
            if other.sign is Num.Sign.POSITIVE:
                out.set_num(other.primes, sign=Num.Sign.NEGATIVE, case=other.case)
            else:
                out.set_num(other.primes, sign=Num.Sign.POSITIVE, case=other.case)

            return out

        if other.case is Num.Case.ZERO:
            out.set_num(self.primes, sign=self.sign, case=self.case)

            return out

        if (self.case is Num.Case.INFINITY) ^ (other.case is Num.Case.INFINITY):
            out.case = Num.Case.INFINITY

            if ((self.case is Num.Case.INFINITY) and (self.sign is Num.Sign.NEGATIVE)) or (
                    (other.case is Num.Case.INFINITY) and (other.sign is Num.Sign.POSITIVE)):
                out.sign = Num.Sign.NEGATIVE

            return out

        if (self.case is Num.Case.INFINITY) and (other.case is Num.Case.INFINITY):
            if self.sign is other.sign:
                out.set_num(case=Num.Case.UNDEFINED)

                return out

            out.set_num(self.primes, sign=self.sign, case=self.case)

            return out

        out.case = Num.Case.NUMBER

        a_numerator: dict[int, int] = self.primes.copy()
        b_numerator: dict[int, int] = other.primes.copy()
        denominator: dict[int, int] = {k: -v for k, v in self.primes.items() if v < 0}

        for prime in other.primes:
            if other.primes[prime] < 0:
                if prime in denominator:
                    denominator[prime] = max(denominator[prime], -other.primes[prime])
                else:
                    denominator[prime] = -other.primes[prime]

        for prime in denominator:
            if prime in a_numerator:
                a_numerator[prime] += denominator[prime]
            else:
                a_numerator[prime] = denominator[prime]

            if prime in b_numerator:
                b_numerator[prime] += denominator[prime]
            else:
                b_numerator[prime] = denominator[prime]

        a: int = 1
        b: int = 1

        for prime in a_numerator:
            a *= prime ** a_numerator[prime]

        for prime in b_numerator:
            b *= prime ** b_numerator[prime]

        out.set_int(a * self.sign.value - b * other.sign.value)

        for prime in denominator:
            if prime in out.primes:
                out.primes[prime] -= denominator[prime]
            else:
                out.primes[prime] = -denominator[prime]

        out._clean_values()

        return out

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

        if (self.case is Num.Case.UNDEFINED) or (other.case is Num.Case.UNDEFINED):
            return False

        if (self.case is Num.Case.INFINITY) and (other.case is Num.Case.INFINITY):
            return False

        if self.case is Num.Case.INFINITY:
            if self.sign is Num.Sign.POSITIVE:
                return False

            return True

        if other.case is Num.Case.INFINITY:
            if other.sign is Num.Sign.POSITIVE:
                return True

            return False

        if (self.case is Num.Case.ZERO) and (other.case is Num.Case.ZERO):
            return False

        if self.case is Num.Case.ZERO:
            if other.sign is Num.Sign.POSITIVE:
                return True

            return False

        if other.case is Num.Case.ZERO:
            if self.sign is Num.Sign.POSITIVE:
                return False

            return True

        if (self.sign is Num.Sign.NEGATIVE) ^ (other.sign is Num.Sign.NEGATIVE):
            if self.sign is Num.Sign.NEGATIVE:
                return True

            return False

        return self.get_float() < other.get_float()

    def __gt__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __le__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __ge__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __ne__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __imul__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __idiv__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __iadd__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __isub__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError

    def __abs__(self):
        out: Num = Num()

        out.set_num(self.primes, sign=Num.Sign.POSITIVE, case=self.case)

        out._clean_values()

        return out

    def __neg__(self):
        out: Num = Num()

        if self.sign is Num.Sign.POSITIVE:
            out.set_num(self.primes, sign=Num.Sign.NEGATIVE, case=self.case)
        else:
            out.set_num(self.primes, sign=Num.Sign.POSITIVE, case=self.case)

        out._clean_values()

        return out

    def __invert__(self):
        pass  # todo: ?

    def __float__(self):
        return self.get_float()


if __name__ == '__main__':
    if PRIMES_TO is not None:
        print(f'Fast precision to: {PRIMES_TO:,}\n')
    else:
        print('Precision: infinite\n')

    number1 = Num()
    number2 = Num()

    number1.set_int(5)
    number2.set_int(2)

    print(number1 < number2)
    print(number1 > number2)
    print()
    print(number1 <= number2)
    print(number1 >= number2)
    print(number2 <= number2)
    print(number1 >= number1)
    print()
    print(number1 == number2)
    print(number1 == number1)
    print(number1 != number2)
    print(number2 != number2)
    print()
