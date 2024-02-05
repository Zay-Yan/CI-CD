def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(3, 4)
    print(f"The result is: {result}")

import unittest

class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()
