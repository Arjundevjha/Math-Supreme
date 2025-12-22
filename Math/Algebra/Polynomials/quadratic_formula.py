class QuadraticEquationSolver:
    """A class to solve quadratic equations of the form ax^2 + bx + c = 0."""
    def solve_quadratic(a, b, c):
        """Return the real roots of ``ax^2 + bx + c = 0``.

        If the discriminant is negative, ``(None, None)`` is returned.
        ``ValueError`` is raised when ``a`` is zero.
        """
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return None, None
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    
    def main():
        print("Welcome to the Quadratic Formula Solver!")
        print("This program will help you find the roots of a quadratic equation of the form ax^2 + bx + c = 0.")
        print("We will calculate the discriminant and then find the roots based on its value using the formula (-b +/- sqrt(b^2 - 4ac)/2a where the discriminant is b^2 - 4ac).")
        a = float(input("Enter the coefficient x^2: "))
        b = float(input("Enter the coefficient x: "))
        c = float(input("Enter the constant term: "))
        try:
            root1, root2 = QuadraticEquationSolver.solve_quadratic(a, b, c)
        except ValueError as exc:
            print(str(exc))
            return

        if root1 is None:
            print("The equation has no real roots.")
        elif root1 == root2:
            print(f"The equation has one real root: {root1}")
        else:
            print(f"The equation has two real roots: {root1} and {root2}")

        print(f"Solutions: {root1}, {root2}")

if __name__ == "__main__":
    QuadraticEquationSolver.main()