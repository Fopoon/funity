import unittest

from funity import UnityVersion


class UnityVersionTestCase(unittest.TestCase):

    def test_eq(self):

        a = UnityVersion(2019, 2, 0, 0)

        self.assertEqual(a, UnityVersion(2019, 2, 0, 0))
        self.assertNotEqual(a, UnityVersion(2019, 2, 0, 1))

    def test_gt(self):

        a = UnityVersion(4, 3, 2, 1)

        self.assertGreater(a, UnityVersion(0, 0, 0, 0))
        self.assertGreater(a, UnityVersion(3, 9, 9, 9))
        self.assertGreater(a, UnityVersion(4, 0, 0, 0))
        self.assertGreater(a, UnityVersion(4, 1, 0, 0))
        self.assertGreater(a, UnityVersion(4, 2, 0, 0))
        self.assertGreater(a, UnityVersion(4, 3, 1, 0))
        self.assertGreater(a, UnityVersion(4, 3, 2, 0))

    def test_lt(self):

        a = UnityVersion(4, 3, 2, 1)

        self.assertLess(a, UnityVersion(4, 3, 2, 2))
        self.assertLess(a, UnityVersion(4, 3, 3, 0))
        self.assertLess(a, UnityVersion(4, 4, 2, 0))
        self.assertLess(a, UnityVersion(5, 0, 0, 0))
        self.assertLess(a, UnityVersion(5, 1, 1, 1))
        self.assertLess(a, UnityVersion(5, 2, 1, 0))
        self.assertLess(a, UnityVersion(9, 9, 9, 9))

    def test_eq_fuzzy(self):

        a = UnityVersion(4, 3, 2, 1)

        self.assertTrue(a.is_equal_to(UnityVersion(4, 3, 0, 0), fuzzy=True))
        self.assertTrue(a.is_equal_to(UnityVersion(4, 3, 100, 100), fuzzy=True))
        self.assertFalse(a.is_equal_to(UnityVersion(5, 3, 0, 0), fuzzy=True))
        self.assertFalse(a.is_equal_to(UnityVersion(5, 3, 100, 100), fuzzy=True))


if __name__ == '__main__':
    unittest.main()
