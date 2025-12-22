import sys
sys.path.append("..")  # Adjust the path as necessary to import Circle

from Area.circle import Circle

# volume of prism
class Prism:
    @staticmethod
    def volume_of_prism(base_area, height):
        """
        Calculate the volume of a prism given its base area and height.

        Parameters:
        base_area (float): The area of the base of the prism.
        height (float): The height of the prism.

        Returns:
        float: The volume of the prism.
        """
        if base_area < 0 or height < 0:
            raise ValueError("Base area and height cannot be negative.")
        
        return base_area * height
    
if __name__ == "__main__":
    try:
        base_area = float(input("Enter the base area of the prism: "))
        height = float(input("Enter the height of the prism: "))
        volume = Prism.volume_of_prism(base_area, height)
        print(f"The volume of the prism with base area {base_area} and height {height} is {volume}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")