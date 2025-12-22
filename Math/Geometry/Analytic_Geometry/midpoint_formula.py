class MidpointFormula:
    @staticmethod
    def calculate(x1, y1, x2, y2):
        """
        Calculate the midpoint of a line segment in a 2D plane.

        :param x1: x-coordinate of the first point
        :param y1: y-coordinate of the first point
        :param x2: x-coordinate of the second point
        :param y2: y-coordinate of the second point
        :return: A tuple representing the coordinates of the midpoint
        """
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        return (mx, my)

if __name__ == "__main__":
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    
    midpoint = MidpointFormula.calculate(x1, y1, x2, y2)
    print(f"The midpoint of the line segment is: {midpoint}")