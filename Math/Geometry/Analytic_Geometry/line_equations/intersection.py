class IntersectionOfLines:
    """
    Class to find the intersection point of two lines given their equations in the form of y = mx + b.
    """

    def __init__(self, m1, b1, m2, b2):
        """
        Initialize with the slopes and y-intercepts of the two lines.

        :param m1: Slope of the first line
        :param b1: Y-intercept of the first line
        :param m2: Slope of the second line
        :param b2: Y-intercept of the second line
        """
        self.m1 = m1
        self.b1 = b1
        self.m2 = m2
        self.b2 = b2

    def find_intersection(self):
        """
        Find the intersection point of the two lines.

        :return: A tuple (x, y) representing the coordinates of the intersection point.
                 Returns None if the lines are parallel.
        """
        if self.m1 == self.m2:
            return None  # Lines are parallel and do not intersect

        x = (self.b2 - self.b1) / (self.m1 - self.m2)
        y = self.m1 * x + self.b1
        return (x, y)
    
if __name__ == "__main__":
    m1 = float(input("Enter the slope of the first line (m1): "))
    b1 = float(input("Enter the y-intercept of the first line (b1): "))
    m2 = float(input("Enter the slope of the second line (m2): "))
    b2 = float(input("Enter the y-intercept of the second line (b2): "))

    intersection_calculator = IntersectionOfLines(m1, b1, m2, b2)
    
    intersection = intersection_calculator.find_intersection()
    
    if intersection:
        print(f"The intersection point of the lines is: {intersection}")
    else:
        print("The lines are parallel and do not intersect.")