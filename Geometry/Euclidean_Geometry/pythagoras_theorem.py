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
    
