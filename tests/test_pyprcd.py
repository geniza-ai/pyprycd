import unittest

from pyprycd import PyPrycd


class TestPyPrycd(unittest.TestCase):

    def test_get_fips_code(self):
        fips1 = PyPrycd.get_fips_code('Autauga County AL')
        self.assertEqual(fips1, 1001)
