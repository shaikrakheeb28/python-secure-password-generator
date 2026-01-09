# test_password_generator.py

import unittest
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        pg = PasswordGenerator()
        pwd = pg.generate()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        pg = PasswordGenerator(length=20)
        pwd = pg.generate()
        self.assertEqual(len(pwd), 20)

    def test_include_uppercase(self):
        pg = PasswordGenerator(length=20, use_uppercase=True)
        pwd = pg.generate()
        self.assertTrue(any(c.isupper() for c in pwd))

    def test_include_digits(self):
        pg = PasswordGenerator(length=20, use_digits=True)
        pwd = pg.generate()
        self.assertTrue(any(c.isdigit() for c in pwd))

    def test_include_specials(self):
        pg = PasswordGenerator(length=20, use_specials=True)
        pwd = pg.generate()
        self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in pwd))

if __name__ == "__main__":
    unittest.main()
