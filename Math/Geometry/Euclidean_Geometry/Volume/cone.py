import sys
sys.path.append("..")  # Adjust the path as necessary to import Circle

from Area.circle import Circle

# volume of cone
class Cone:
    @staticmethod
    def volume_of_cone(radius, height):
        """
        Calculate the volume of a cone given its radius and height.

        Parameters:
        radius (float): The radius of the base of the cone.
        height (float): The height of the cone.

        Returns:
        float: The volume of the cone.
        """
        if radius < 0 or height < 0:
            raise ValueError("Radius and height cannot be negative.")
        
        return (1/3) * Circle.area_of_circle(radius) * height
    
if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        volume = Cone.volume_of_cone(radius, height)
        print(f"The volume of the cone with radius {radius} and height {height} is {volume}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")