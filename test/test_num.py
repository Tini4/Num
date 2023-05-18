import unittest

from src.num import Num


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
class TestNumSetInt(unittest.TestCase):  # TODO
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


class TestNumMultiplication(unittest.TestCase):  # TODO
    def setUp(self):
        pass

    def test_something(self):
        pass


class TestNumDivision(unittest.TestCase):  # TODO
    def setUp(self):
        pass

    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
