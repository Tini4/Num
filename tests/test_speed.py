import unittest

from num_tini4 import Num


class TestSpeedNum(unittest.TestCase):
    def setUp(self):
        pass

    def _test_prime_factorization_fast(self):
        number = Num()

        for _ in range(10**5):
            number.set_int(1000000*2)

        self.assertEqual(True, True)

    def _test_prime_factorization_slow(self):
        number = Num()

        for _ in range(10**5):
            number.set_int(1000003)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
