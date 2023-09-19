import unittest
from unittest import TestCase
from aula import multiplicar


class TestMultiplicar(TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(TestMultiplicar(2, 3), 6)


if __name__ == "__main__" :
    unittest.main()