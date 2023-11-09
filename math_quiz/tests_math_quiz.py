import unittest
from math_quiz import task_1, task_2, task_3

class TestMathGame(unittest.TestCase):

    def test_task_1(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = task_1(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_task_2(self):  # Set of valid operators
        valid_operators = {'+', '-', '*'}  # Set of valid operators

        for _ in range(1000):
            operator = task_2()
            self.assertIn(operator, valid_operators)

    def test_task_3(self):
            test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 5, '-', '8 - 5', 3),
            (4, 3, '*', '4 * 3', 12),
            (10, 2, '+', '10 + 2', 12),
            (15, 7, '-', '15 - 7', 8),
            (6, 2, '*', '6 * 2', 12),
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = task_3(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                
if __name__ == "__main__":
    unittest.main()
