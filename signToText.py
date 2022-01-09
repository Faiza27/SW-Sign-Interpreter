import unittest

from connectDb import convertSignToText


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(convertSignToText('images/alpa.jpeg'), "('A',)")  # add assertion here


if __name__ == '__main__':
    unittest.main()
