class Slope:
    """
    Class to calculate the slope of a line given two points.
    """

    def __init__(self, point1, point2):
        """
        Initialize with two points.

        :param point1: A tuple (x1, y1) representing the first point.
        :param point2: A tuple (x2, y2) representing the second point.
        """
        self.point1 = point1
        self.point2 = point2

    def calculate_slope(self):
        """
        Calculate the slope of the line connecting the two points.

        :return: The slope as a float.
        """
        x1, y1 = self.point1
        x2, y2 = self.point2

        if x2 - x1 == 0:
            raise ValueError("Slope is undefined for vertical lines (x1 cannot equal x2).")

        return (y2 - y1) / (x2 - x1)
    
if __name__ == "__main__":
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))

    slope_calculator = Slope((x1, y1), (x2, y2))
    
    try:
        slope = slope_calculator.calculate_slope()
        print(f"The slope of the line connecting the points ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")
    except ValueError as e:
        print(e)