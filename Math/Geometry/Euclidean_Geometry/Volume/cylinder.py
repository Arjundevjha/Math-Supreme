import sys
sys.path.append("..")  # Adjust the path as necessary to import Circle

from Area.circle import Circle

# volume of cylinder
class Cylinder:
    @staticmethod
    def volume_of_cylinder(radius, height):
        """
        Calculate the volume of a cylinder given its radius and height.

        Parameters:
        radius (float): The radius of the base of the cylinder.
        height (float): The height of the cylinder.

        Returns:
        float: The volume of the cylinder.
        """
        if radius < 0 or height < 0:
            raise ValueError("Radius and height cannot be negative.")
        
        return Circle.area_of_circle(radius) * height
    
if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = Cylinder.volume_of_cylinder(radius, height)
        print(f"The volume of the cylinder with radius {radius} and height {height} is {volume}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")