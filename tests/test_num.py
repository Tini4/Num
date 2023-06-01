import unittest

from src.Num_Tini4.num import Num


class TestNumEnum(unittest.TestCase):
    def setUp(self):
        pass

    def test_sign(self):  # todo
        assert Num.Sign.POSITIVE, 'Missing POSITIVE in Sign enum.'
        assert Num.Sign.NEGATIVE, 'Missing NEGATIVE in Sign enum.'

        self.assertEqual(Num.Sign.POSITIVE.value, 1, 'Value of POSITIVE should be 1.')
        self.assertEqual(Num.Sign.NEGATIVE.value, -1, 'Value of NEGATIVE should be -1.')

    def test_case(self):  # todo
        assert Num.Case.NUMBER, 'Missing NUMBER in Case enum.'
        assert Num.Case.ZERO, 'Missing ZERO in Case enum.'
        assert Num.Case.INFINITY, 'Missing INFINITY in Case enum.'
        assert Num.Case.UNDEFINED, 'Missing UNDEFINED in Case enum.'


class TestNumInit(unittest.TestCase):
    def setUp(self):
        self.number = Num()

    def test_primes(self):
        self.assertEqual(self.number.primes, {}, 'Primes should be an empty dict. {}')

    def test_sign(self):
        self.assertEqual(self.number.sign, Num.Sign.POSITIVE, 'Sign should be POSITIVE.')

    def test_case(self):
        self.assertEqual(self.number.case, Num.Case.UNDEFINED, 'Case should be UNDEFINED.')


# noinspection DuplicatedCode
class TestNumSetNum(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.POSITIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.POSITIVE)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2})
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_number_negative(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_zero(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.POSITIVE, case=Num.Case.ZERO)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE, case=Num.Case.ZERO)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, case=Num.Case.ZERO)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.POSITIVE, case=Num.Case.ZERO)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.NEGATIVE, case=Num.Case.ZERO)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_num(case=Num.Case.ZERO)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

    def test_infinity_positive(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.POSITIVE, case=Num.Case.INFINITY)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, case=Num.Case.INFINITY)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.POSITIVE, case=Num.Case.INFINITY)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

        number.set_num(case=Num.Case.INFINITY)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

    def test_infinity_negative(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE, case=Num.Case.INFINITY)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.NEGATIVE, case=Num.Case.INFINITY)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

    def test_undefined(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.POSITIVE, case=Num.Case.UNDEFINED)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.POSITIVE, case=Num.Case.UNDEFINED)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.POSITIVE)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(None, sign=Num.Sign.POSITIVE)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.POSITIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(None, sign=Num.Sign.POSITIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE, case=Num.Case.UNDEFINED)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.NEGATIVE, case=Num.Case.UNDEFINED)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(None, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(sign=Num.Sign.NEGATIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(None, sign=Num.Sign.NEGATIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num({2: 1, 3: 2}, case=Num.Case.UNDEFINED)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(case=Num.Case.UNDEFINED)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num()
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(None)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_num(None, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

    def test_one_positive(self):
        number = Num()

        number.set_num({}, sign=Num.Sign.POSITIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({}, sign=Num.Sign.POSITIVE)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({}, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({})
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_one_negative(self):
        number = Num()

        number.set_num({}, sign=Num.Sign.NEGATIVE, case=Num.Case.NUMBER)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_num({}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')


# noinspection DuplicatedCode
class TestNumSetInt(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number = Num()

        number.set_int(18)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_number_negative(self):
        number = Num()

        number.set_int(-18)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_zero(self):
        number = Num()

        number.set_int(0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

    def test_one_positive(self):
        number = Num()

        number.set_int(1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_one_negative(self):
        number = Num()

        number.set_int(-1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')


# noinspection DuplicatedCode
class TestNumSetFloat(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number = Num()

        number.set_float(18)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def _test_number_positive(self):
        number = Num()

        number.set_float(18 / 11)
        self.assertEqual(number.primes, {2: -52, 19: 1, 26041: 1, 14894582557: 1}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_number_negative(self):
        number = Num()

        number.set_float(-18)
        self.assertEqual(number.primes, {2: 1, 3: 2}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def _test_number_negative(self):
        number = Num()

        number.set_float(-18 / 11)
        self.assertEqual(number.primes, {2: -52, 19: 1, 26041: 1, 14894582557: 1}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_zero(self):
        number = Num()

        number.set_float(0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

    def test_infinity_positive(self):
        number = Num()

        number.set_float(float('inf'))
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

    def test_infinity_negative(self):
        number = Num()

        number.set_float(float('-inf'))
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

    def test_one_positive(self):
        number = Num()

        number.set_float(1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_one_negative(self):
        number = Num()

        number.set_float(-1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')


# noinspection DuplicatedCode
class TestNumSetFraction(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number = Num()

        number.set_fraction(18, 11)
        self.assertEqual(number.primes, {2: 1, 3: 2, 11: -1}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(-18, -11)
        self.assertEqual(number.primes, {2: 1, 3: 2, 11: -1}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_number_negative(self):
        number = Num()

        number.set_fraction(-18, 11)
        self.assertEqual(number.primes, {2: 1, 3: 2, 11: -1}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(18, -11)
        self.assertEqual(number.primes, {2: 1, 3: 2, 11: -1}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_zero(self):
        number = Num()

        number.set_fraction(0, 11)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_fraction(-0, 11)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_fraction(-0, -11)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        number.set_fraction(0, -11)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

        # number.set_fraction(18, float('inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')
        #
        # number.set_fraction(-18, float('inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')
        #
        # number.set_fraction(-18, float('-inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')
        #
        # number.set_fraction(18, float('-inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.ZERO, 'Case not assigned properly.')

    # def test_infinity_positive(self):
    #     number = Num()
    #
    #     number.set_fraction(float('inf'), 11)
    #     self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
    #     self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
    #     self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')
    #
    #     number.set_fraction(float('-inf'), -11)
    #     self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
    #     self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
    #     self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')
    #
    # def test_infinity_negative(self):
    #     number = Num()
    #
    #     number.set_fraction(float('-inf'), 11)
    #     self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
    #     self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
    #     self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')
    #
    #     number.set_fraction(float('inf'), -11)
    #     self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
    #     self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
    #     self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

    def test_undefined(self):
        number = Num()

        number.set_fraction(18, 0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(0, 0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(-18, 0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(-0, 0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(18, -0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(0, -0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(-18, -0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        number.set_fraction(-0, -0)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.UNDEFINED, 'Case not assigned properly.')

        # number.set_fraction(float('inf'), float('inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')
        #
        # number.set_fraction(float('-inf'), float('inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')
        #
        # number.set_fraction(float('inf'), float('-inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')
        #
        # number.set_fraction(float('-inf'), float('-inf'))
        # self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        # self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        # self.assertEqual(number.case, Num.Case.INFINITY, 'Case not assigned properly.')

    def test_one_positive(self):
        number = Num()

        number.set_fraction(1, 1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(18, 18)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(-1, -1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(-18, -18)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.POSITIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

    def test_one_negative(self):
        number = Num()

        number.set_fraction(-1, 1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(-18, 18)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(1, -1)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')

        number.set_fraction(18, -18)
        self.assertEqual(number.primes, {}, 'Primes not assigned properly.')
        self.assertEqual(number.sign, Num.Sign.NEGATIVE, 'Sign not assigned properly.')
        self.assertEqual(number.case, Num.Case.NUMBER, 'Case not assigned properly.')


# noinspection DuplicatedCode
class TestNumGetFloat(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number = Num()

        number.set_num({2: 1, 3: 2})
        self.assertEqual(number.get_float(), 18, 'Wrong output.')

        number.set_num({2: 1, 3: 2, 11: -1})
        self.assertEqual(number.get_float(), 18 / 11, 'Wrong output.')

    def test_number_negative(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.get_float(), -18, 'Wrong output.')

        number.set_num({2: 1, 3: 2, 11: -1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.get_float(), -18 / 11, 'Wrong output.')

    def test_zero(self):
        number = Num()

        number.set_num(case=Num.Case.ZERO)
        self.assertEqual(number.get_float(), 0, 'Wrong output.')

    def test_infinity_positive(self):
        number = Num()

        number.set_num(case=Num.Case.INFINITY)
        self.assertEqual(number.get_float(), float('inf'), 'Wrong output.')

    def test_infinity_negative(self):
        number = Num()

        number.set_num(sign=Num.Sign.NEGATIVE, case=Num.Case.INFINITY)
        self.assertEqual(number.get_float(), float('-inf'), 'Wrong output.')

    def test_undefined(self):
        number = Num()

        value = number.get_float()  # nan
        self.assertNotEqual(value, value, 'Wrong output.')

    def test_one_positive(self):
        number = Num()

        number.set_num({})
        self.assertEqual(number.get_float(), 1, 'Wrong output.')

    def test_one_negative(self):
        number = Num()

        number.set_num({}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.get_float(), -1, 'Wrong output.')


# noinspection DuplicatedCode
class TestNumGetFraction(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number = Num()

        number.set_num({2: 1, 3: 2})
        self.assertEqual(number.get_fraction(), (18, 1), 'Wrong output.')

        number.set_num({2: 1, 3: 2, 11: -1})
        self.assertEqual(number.get_fraction(), (18, 11), 'Wrong output.')

    def test_number_negative(self):
        number = Num()

        number.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.get_fraction(), (-18, 1), 'Wrong output.')

        number.set_num({2: 1, 3: 2, 11: -1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.get_fraction(), (-18, 11), 'Wrong output.')

    def test_zero(self):
        number = Num()

        number.set_num(case=Num.Case.ZERO)
        self.assertEqual(number.get_fraction(), (0, 1), 'Wrong output.')

    def test_infinity_positive(self):
        number = Num()

        number.set_num(case=Num.Case.INFINITY)
        self.assertEqual(number.get_fraction(), (float('inf'), 1), 'Wrong output.')

    def test_infinity_negative(self):
        number = Num()

        number.set_num(sign=Num.Sign.NEGATIVE, case=Num.Case.INFINITY)
        self.assertEqual(number.get_fraction(), (float('-inf'), 1), 'Wrong output.')

    def test_undefined(self):
        number = Num()

        self.assertEqual(number.get_fraction(), None, 'Wrong output.')

    def test_one_positive(self):
        number = Num()

        number.set_num({})
        self.assertEqual(number.get_fraction(), (1, 1), 'Wrong output.')

    def test_one_negative(self):
        number = Num()

        number.set_num({}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number.get_fraction(), (-1, 1), 'Wrong output.')


# noinspection DuplicatedCode
class TestNumMul(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: 1}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: 1}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

    def test_number_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: 1}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: 1}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

    def test_zero(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not multiplied properly.')

    def test_infinity_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

    def test_infinity_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not multiplied properly.')

    def test_undefined(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not multiplied properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not multiplied properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not multiplied properly.')

    def test_one_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({})
        number2.set_num({})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({5: 1})
        number2.set_num({5: -1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({5: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

    def test_one_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({})
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({5: -1})
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')

        number1.set_num({5: 1})
        number2.set_num({5: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 * number2
        self.assertEqual(number3.primes, {}, 'Primes not multiplied properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not multiplied properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not multiplied properly.')


# noinspection DuplicatedCode
class TestNumTruediv(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: -1}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: -1}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

    def test_number_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: -1}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {2: 1, 3: 2, 11: -1}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

    def test_zero(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not divided properly.')

    def test_infinity_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not divided properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not divided properly.')

    def test_infinity_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not divided properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not divided properly.')

    def test_undefined(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not divided properly.')

    def test_one_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({})
        number2.set_num({})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({5: 1})
        number2.set_num({5: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

    def test_one_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({})
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({5: 1})
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')

        number1.set_num({5: 1})
        number2.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 / number2
        self.assertEqual(number3.primes, {}, 'Primes not divided properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not divided properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not divided properly.')


# noinspection DuplicatedCode
class TestNumAdd(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {29: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {7: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: -1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {11: -1, 199: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {11: -1, 197: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {11: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {2: 1, 3: 2}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

    def test_number_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {29: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {7: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {11: -1, 199: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: -1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {11: -1, 197: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {11: 1}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {2: 1, 3: 2}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

    def test_zero(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not added properly.')

        number1.set_num({5: 1})
        number2.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not added properly.')

        number1.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({5: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not added properly.')

    def test_infinity_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

    def test_infinity_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not added properly.')

    def test_undefined(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not added properly.')

    def test_one_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({})
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1})
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: -1})
        number2.set_num({2: -1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: -1, 3: 1})
        number2.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: -1, 3: 1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

    def test_one_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({})
        number2.set_num({2: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: -1, 3: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: -1})
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')

        number1.set_num({2: -1})
        number2.set_num({2: -1, 3: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 + number2
        self.assertEqual(number3.primes, {}, 'Primes not added properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not added properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not added properly.')


# noinspection DuplicatedCode
class TestNumSub(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {7: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {29: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: -1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {11: -1, 197: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {11: -1, 199: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {2: 1, 3: 2}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {11: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

    def test_number_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {7: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {29: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {11: -1, 197: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: -1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {11: -1, 199: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {2: 1, 3: 2}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {11: 1}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

    def test_zero(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not subtracted properly.')

        number1.set_num({5: 1})
        number2.set_num({5: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not subtracted properly.')

        number1.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({5: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not subtracted properly.')

    def test_infinity_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

    def test_infinity_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not subtracted properly.')

    def test_undefined(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not subtracted properly.')

    def test_one_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({})
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1})
        number2.set_num({})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: -1})
        number2.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: -1, 3: 1})
        number2.set_num({2: -1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: -1, 3: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

    def test_one_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({})
        number2.set_num({2: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: -1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: -1, 3: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: -1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')

        number1.set_num({2: -1})
        number2.set_num({2: -1, 3: 1})
        number3 = number1 - number2
        self.assertEqual(number3.primes, {}, 'Primes not subtracted properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not subtracted properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not subtracted properly.')


# noinspection DuplicatedCode
class TestNumPow(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {2: 11, 3: 22}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {2: 2, 3: 4}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

    def test_number_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {2: 11, 3: 22}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

    def test_zero(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not powered properly.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.ZERO, 'Case not powered properly.')

    def test_infinity_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not powered properly.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not powered properly.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not powered properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: 3})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not powered properly.')

    def test_infinity_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not powered properly.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.INFINITY, 'Case not powered properly.')

    def test_undefined(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not powered properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not powered properly.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not powered properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not powered properly.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num(case=Num.Case.UNDEFINED)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.UNDEFINED, 'Case not powered properly.')

    def test_one_positive(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({})
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num({2: 3})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num({2: 3}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num({})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num(case=Num.Case.INFINITY)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({})
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.POSITIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

    def test_one_negative(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({})
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')

        number1.set_num({}, sign=Num.Sign.NEGATIVE)
        number2.set_num({}, sign=Num.Sign.NEGATIVE)
        number3 = number1 ** number2
        self.assertEqual(number3.primes, {}, 'Primes not powered properly.')
        self.assertEqual(number3.sign, Num.Sign.NEGATIVE, 'Sign not powered properly.')
        self.assertEqual(number3.case, Num.Case.NUMBER, 'Case not powered properly.')


# noinspection DuplicatedCode
class TestNumLt(unittest.TestCase):
    def setUp(self):
        pass

    def test_number(self):
        number1 = Num()
        number2 = Num()

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1})
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({11: 1})
        number2.set_num({2: 1, 3: 2})
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({11: 1})
        number2.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        number2.set_num({2: 1, 3: 2})
        self.assertEqual(number1 < number2, True, 'Less than not working.')

    def test_zero(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1})
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.ZERO)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.ZERO)
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num(case=Num.Case.ZERO)
        number2.set_num(case=Num.Case.ZERO)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

    def test_infinity(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num(case=Num.Case.INFINITY)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY)
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1})
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY)
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num(case=Num.Case.INFINITY)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1})
        self.assertEqual(number1 < number2, True, 'Less than not working.')

        number1.set_num({2: 1, 3: 2}, sign=Num.Sign.NEGATIVE)
        number2.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num(case=Num.Case.INFINITY, sign=Num.Sign.NEGATIVE)
        number2.set_num({11: 1}, sign=Num.Sign.NEGATIVE)
        self.assertEqual(number1 < number2, True, 'Less than not working.')

    def test_undefined(self):
        number1 = Num()
        number2 = Num()

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num(case=Num.Case.UNDEFINED)
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num(case=Num.Case.UNDEFINED)
        number2.set_num({11: 1})
        self.assertEqual(number1 < number2, False, 'Less than not working.')

        number1.set_num({2: 1, 3: 2})
        number2.set_num(case=Num.Case.UNDEFINED)
        self.assertEqual(number1 < number2, False, 'Less than not working.')


if __name__ == '__main__':
    unittest.main()
