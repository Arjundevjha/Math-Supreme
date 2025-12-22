# Finnding an equation of a line given two points
class LinearEquation:

    def equation_from_two_points(x1, y1, x2, y2):
        """
        Calculate the equation of a line given two points (x1, y1) and (x2, y2).

        Parameters:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.

        Returns:
        str: The equation of the line in the form "y = mx + b".
        """
        if x1 == x2:
            raise ValueError("The x-coordinates cannot be the same (vertical line).")

        # Calculate slope (m)
        m = (y2 - y1) / (x2 - x1)

        # Calculate y-intercept (b)
        b = y1 - m * x1

        return f"y = {m}x + {b}"
if __name__ == "__main__":
    equation_from_two_points = LinearEquation.equation_from_two_points
    try:
        x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
        x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())
        equation = equation_from_two_points(x1, y1, x2, y2)
        print(f"The equation of the line is: {equation}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")