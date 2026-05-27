import unittest
from quadratic_solver import solve_quadratic

class TestQuadraticSolver(unittest.TestCase):
    def test_quadratic_real_solutions(self):
        # x² - 5x + 6 = 0 -> x1 = 3, x2 = 2
        self.assertEqual(solve_quadratic(1, -5, 6), (3.0, 2.0))

    def test_quadratic_one_real_solution(self):
        # x² - 4x + 4 = 0 -> x1 = 2, x2 = 2
        self.assertEqual(solve_quadratic(1, -4, 4), (2.0, 2.0))

    def test_quadratic_complex_solutions(self):
        # x² + 1 = 0 -> x1 = 1j, x2 = -1j
        solutions = solve_quadratic(1, 0, 1)
        self.assertEqual(solutions[0], 1j)
        self.assertEqual(solutions[1], -1j)

    def test_linear_equation(self):
        # 0x² + 2x - 4 = 0 -> x = 2
        self.assertEqual(solve_quadratic(0, 2, -4), (2.0,))

    def test_linear_no_solution(self):
        # 0x² + 0x + 5 = 0 -> Keine Lösung
        self.assertEqual(solve_quadratic(0, 0, 5), "Keine Lösung")

    def test_linear_infinite_solutions(self):
        # 0x² + 0x + 0 = 0 -> Unendlich viele Lösungen
        self.assertEqual(solve_quadratic(0, 0, 0), "Unendlich viele Lösungen")

if __name__ == "__main__":
    unittest.main()
