import unittest
import sys
import os

# Add root directory to path to allow "Math.Discrete_Math..." imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)

# the code has imports assuming "Math" is the root in some cases, so let's add it too
math_dir = os.path.abspath(os.path.join(root_dir, 'Math'))
sys.path.insert(0, math_dir)

# E.g. trinomial_theorem.py has `sys.path.append('..')` and `from combination import nCr`
# The internal code inside Math directory assumes sys.path has `Math/Discrete_Math/Combinatorics`
combinatorics_dir = os.path.abspath(os.path.join(math_dir, 'Discrete_Math/Combinatorics'))
sys.path.insert(0, combinatorics_dir)


from Discrete_Math.Combinatorics.trinomial_theorem import expand_trinomial

class TestDiscreteMath(unittest.TestCase):

    def test_expand_trinomial_n_0(self):
        result = expand_trinomial('a', 'b', 'c', 0)
        self.assertEqual(result, '1*a^0*b^0*c^0')

    def test_expand_trinomial_n_1(self):
        result = expand_trinomial('a', 'b', 'c', 1)
        # 1*a^0*b^0*c^1 + 1*a^0*b^1*c^0 + 1*a^1*b^0*c^0
        self.assertEqual(result, '1*a^0*b^0*c^1 + 1*a^0*b^1*c^0 + 1*a^1*b^0*c^0')

    def test_expand_trinomial_n_2(self):
        result = expand_trinomial('x', 'y', 'z', 2)
        # 1*x^0*y^0*z^2 + 2*x^0*y^1*z^1 + 1*x^0*y^2*z^0 + 2*x^1*y^0*z^1 + 2*x^1*y^1*z^0 + 1*x^2*y^0*z^0
        self.assertEqual(result, '1*x^0*y^0*z^2 + 2*x^0*y^1*z^1 + 1*x^0*y^2*z^0 + 2*x^1*y^0*z^1 + 2*x^1*y^1*z^0 + 1*x^2*y^0*z^0')

    def test_expand_trinomial_different_variables(self):
        result = expand_trinomial('p', 'q', 'r', 1)
        self.assertEqual(result, '1*p^0*q^0*r^1 + 1*p^0*q^1*r^0 + 1*p^1*q^0*r^0')

    def test_expand_trinomial_long_variable_names(self):
        result = expand_trinomial('alpha', 'beta', 'gamma', 1)
        self.assertEqual(result, '1*alpha^0*beta^0*gamma^1 + 1*alpha^0*beta^1*gamma^0 + 1*alpha^1*beta^0*gamma^0')

    def test_expand_trinomial_negative_n(self):
        with self.assertRaises(ValueError) as context:
            expand_trinomial('a', 'b', 'c', -1)
        self.assertTrue("Power n must be non-negative." in str(context.exception))

if __name__ == '__main__':
    unittest.main()
