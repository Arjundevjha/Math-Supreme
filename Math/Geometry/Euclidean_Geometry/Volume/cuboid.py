import sys
sys.path.append("..")  # Adjust the path as necessary to import Circle
from Area.rectangle import Rectangle

class Cuboid:
    @staticmethod
    def volume_of_cuboid(length, width, height):
        """
        Calculate the volume of a cuboid given its length, width, and height.

        Parameters:
        length (float): The length of the cuboid.
        width (float): The width of the cuboid.
        height (float): The height of the cuboid.

        Returns:
        float: The volume of the cuboid.
        """
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Length, width, and height cannot be negative.")
        
        return Rectangle.area_of_rectangle(length, width) * height
    
if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        volume = Cuboid.volume_of_cuboid(length, width, height)
        print(f"The volume of the cuboid with length {length}, width {width}, and height {height} is {volume}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")