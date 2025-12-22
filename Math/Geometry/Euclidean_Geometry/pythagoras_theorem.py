class PythagoreanTheorem:
    @staticmethod
    def calculate(a, b):
        """
        Calculate the length of the hypotenuse of a right triangle using the Pythagorean theorem.
        
        :param a: Length of one leg of the triangle
        :param b: Length of the other leg of the triangle
        :return: Length of the hypotenuse
        """
        return (a ** 2 + b ** 2) ** 0.5
    
if __name__ == "__main__":
    a = int(input("Enter the length of one leg of the triangle: "))
    b = int(input("Enter the length of the other leg of the triangle: "))
    hypotenuse = PythagoreanTheorem.calculate(a, b)
    if hypotenuse.is_integer():
        triangle_type = "right triangle"
    else:
        triangle_type = "not a right triangle"
    print(f"The length of the hypotenuse is: {hypotenuse}")
    print(f"The triangle is a {triangle_type}.")