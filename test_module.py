import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        input_data = [2, 6, 2, 8, 4, 0, 1, 5, 7]
        expected_output = {
            'mean': [[3.6666666667, 5.0, 3.0],
                     [3.3333333333, 4.0, 4.3333333333],
                     3.8888888889],
            'variance': [[9.5555555556, 0.6666666667, 13.5555555556],
                         [4.0, 10.6666666667, 6.2222222222],
                         9.2098765432],
            'standard deviation': [[3.0912061652, 0.8164965809, 3.6817870057],
                                   [2.0, 3.2659863237, 2.4944382578],
                                   3.0347778400],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }

        actual = calculate(input_data)

        for key in expected_output:
            for i in range(2):  # column and row axes
                for a, b in zip(actual[key][i], expected_output[key][i]):
                    self.assertAlmostEqual(a, b, delta=0.1, msg=f"{key} axis {i} value mismatch: {a} != {b}")
            self.assertAlmostEqual(actual[key][2], expected_output[key][2], delta=0.1, msg=f"{key} flat value mismatch")

if __name__ == "__main__":
    unittest.main()
