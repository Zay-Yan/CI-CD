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

<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Test</title>
</head>
<body>
    <h1>CI/CD Test</h1>
    <p>This is a simple HTML page to test the CI/CD workflow.</p>
</body>
</html>
