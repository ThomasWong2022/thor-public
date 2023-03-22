import unittest


class TestSimple(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+2, 4)


if __name__ == "__main__":
    unittest.main()
