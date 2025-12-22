#area of circle
import math

class Circle:

    def area_of_circle(radius):
        """
        Calculate the area of a circle given its radius.

        Parameters:
        radius (float): The radius of the circle.

        Returns:
        float: The area of the circle.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        
        return math.pi * (radius ** 2)

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = Circle.area_of_circle(radius)
        print(f"The area of the circle with radius {radius} is {area}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")