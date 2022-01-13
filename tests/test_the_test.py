import unittest

class TestMe(unittest.TestCase):

    def test_the_test(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
