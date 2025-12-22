# area of triangle

class Triangle:


    def area_of_triangle(base, height):
        """
        Calculate the area of a triangle given its base and height.

        Parameters:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle.

        Returns:
        float: The area of the triangle.
        """
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        
        return 0.5 * base * height

if __name__ == "__main__":
    try:
        base = float(input("Enter the length of the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = Triangle.area_of_triangle(base, height)
        print(f"The area of the triangle with base {base} and height {height} is {area}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")