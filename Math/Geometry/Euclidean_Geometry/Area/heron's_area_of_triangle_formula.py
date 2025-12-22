# Area of triangle using Heron's formula

class Heronsformula:

    def herons_area_of_triangle(a, b, c):
        """
        Calculate the area of a triangle using Heron's formula.

        Parameters:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

        Returns:
        float: Area of the triangle.
        """
        # Calculate semi-perimeter
        s = (a + b + c) / 2
        
        # Calculate area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        
        return area

if __name__ == "__main__":
    # Example usage
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    area = Heronsformula.herons_area_of_triangle(a, b, c)
    print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area}")