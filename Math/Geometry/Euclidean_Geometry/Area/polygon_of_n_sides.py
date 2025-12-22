# Area of a polyogon with n sides
# Formula: Area = (n * s^2) / (4 * tan(π / n))
# where n is the number of sides and s is the length of each side.
from math import tan, pi

class Polygon:

    def area_of_polygon(n, s):
        
        area_of_polygon = (n * s**2) / (4 * tan(pi / n))
        return area_of_polygon

if __name__ == "__main__":
    n = int(input("Enter the number of sides of the polygon: "))
    s = float(input("Enter the length of each side: "))
    
    area = Polygon.area_of_polygon(n, s)
    print(f"The area of the polygon with {n} sides, each of length {s}, is: {area}")