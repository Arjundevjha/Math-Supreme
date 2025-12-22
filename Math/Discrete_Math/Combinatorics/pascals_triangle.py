#pascale_triangle  in python
class PascalTriangle:
    def __init__(self, n):
        self.n = n
        self.triangle = self.generate_triangle()

    def generate_triangle(self):
        triangle = []
        for i in range(self.n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle

    def print_triangle(self):
        max_length = len(" ".join(map(str, self.triangle[-1])))
        for row in self.triangle:
            print(" ".join(map(str, row)).center(max_length))
        
# Example usage
n = int(input("Enter the number of rows for Pascal's Triangle: "))  # Change this value to generate more or fewer rows
pascals_triangle = PascalTriangle(n)
pascals_triangle.print_triangle()