# area of rectangle

class Rectangle:

    def area_of_rectangle(length, width):
        """
        Calculate the area of a rectangle given its length and width.

        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        
        return length * width  
if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = Rectangle.area_of_rectangle(length, width)
        print(f"The area of the rectangle with length {length} and width {width} is {area}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")