# area of a square

class Square:

    def area_of_square(side_length):
        """
        Calculate the area of a square given the length of its side.

        Parameters:
        side_length (float): The length of one side of the square.

        Returns:
        float: The area of the square.
        """
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        
        return side_length ** 2 

if __name__ == "__main__":
    try:
        side_length = float(input("Enter the length of the side of the square: "))
        area = Square.area_of_square(side_length)
        print(f"The area of the square with side length {side_length} is {area}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")