class DistanceFormula:
    @staticmethod
    def calculate(x1, y1, x2, y2):
        """
        Calculate the distance between two points (x1, y1) and (x2, y2) using the distance formula.
        
        :param x1: x-coordinate of the first point
        :param y1: y-coordinate of the first point
        :param x2: x-coordinate of the second point
        :param y2: y-coordinate of the second point
        :return: Distance between the two points
        """
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
if __name__ == "__main__":
    # Example usage
    point1 = input("Enter the coordinates of the first point (x1, y1) separated by a comma: ")
    point2 = input("Enter the coordinates of the second point (x2, y2) separated by a comma: ")
    point1 = tuple(map(float, point1.split(',')))
    point2 = tuple(map(float, point2.split(',')))
    if len(point1) != 2 or len(point2) != 2:
        print("Please enter valid coordinates in the format x,y.")
    else:
        distance = DistanceFormula.calculate(point1[0], point1[1], point2[0], point2[1])
        print(f"The distance between points {point1} and {point2} is {distance:.2f}")