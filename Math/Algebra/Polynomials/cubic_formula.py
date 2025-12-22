from ast import main


class CubicEquationSolver:
    """
    This class provides a method to solve cubic equations of the form:
    ax^3 + bx^2 + cx + d = 0
    using the cubic formula.
    """

    def main():
        print("Ennter in the coefficients of a, b, c, d for the cubic equation ax^3 + bx^2 + cx + d")
        a = int(input("Coefficient a: "))
        b = int(input("Coefficient b: "))
        c = int(input("Coefficient c: "))
        d = int(input("Coefficient d: "))

        i = (-1) ** 0.5  # i is the imaginary unit
        if a == 0:
            print("Coefficient 'a' cannot be zero for a cubic equation.")
            return
        
        term_1 = -(b/(3*a))
        
        inner_term_1 = 2*(b**3) - 9*a*b*c + 27*(a**2)*d
        inner_term_2 = 4*((b**2 - 3*a*c)**3)
        
        cubed_value_1 = 0.5 * (inner_term_1 + (inner_term_2**0.5))
        cubed_value_2 = 0.5 * (inner_term_1 - (inner_term_2**0.5))

        normal_multiplier = -1/(3*a)
        complex_multiplier_1 = (1 + (1*i * (3**0.5))) / (6 * a)
        complex_multiplier_2 = (1 + (-1*i * (3**0.5))) / (6 * a)
        
        x1 = term_1 + ((cubed_value_1**(1/3)) * normal_multiplier) + ((cubed_value_2**(1/3)) * normal_multiplier)
        x2 = term_1 + ((cubed_value_1**(1/3)) * complex_multiplier_1) + ((cubed_value_2**(1/3)) * complex_multiplier_2)
        x3 = term_1 + ((cubed_value_1**(1/3)) * complex_multiplier_2) + ((cubed_value_2**(1/3)) * complex_multiplier_1)

        print("The roots of the cubic equation are:")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)

if __name__ == "__main__":
    CubicEquationSolver.main()