class LineFromPoints:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def slope(self):
        """Calculate the slope of the line."""
        if self.point2[0] - self.point1[0] == 0:
            raise ValueError("Slope is undefined for vertical lines.")
        return (self.point2[1] - self.point1[1]) / (self.point2[0] - self.point1[0])

    def y_intercept(self):
        """Calculate the y-intercept of the line."""
        m = self.slope()
        return self.point1[1] - m * self.point1[0]

    def equation(self):
        """Return the equation of the line in slope-intercept form."""
        m = self.slope()
        b = self.y_intercept()
        return f"y = {m}x + {b}"
    
if __name__ == "__main__":
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))

    line_calculator = LineFromPoints((x1, y1), (x2, y2))
    
    try:
        equation = line_calculator.equation()
        print(f"The equation of the line passing through points ({x1}, {y1}) and ({x2}, {y2}) is: {equation}")
    except ValueError as e:
        print(e)