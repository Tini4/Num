import unittest

from src.num_tini4.num import Num


class TestSpeedNum(unittest.TestCase):
    def setUp(self):
        pass

    def test_prime_factorization_fast(self):
        number = Num()

        for _ in range(10**5):
            number.set_int(1000000*2)

    def test_prime_factorization_slow(self):
        number = Num()

        for _ in range(10**5):
            number.set_int(1000003)


if __name__ == '__main__':
    unittest.main()
