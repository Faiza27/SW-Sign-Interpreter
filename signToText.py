import unittest

from convertSignToText import convert_sign_to_text


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(convert_sign_to_text('/images/alpa.jpeg'), "('A',)")  # add assertion here


if __name__ == '__main__':
    unittest.main()
