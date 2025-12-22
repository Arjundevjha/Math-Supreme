class Sphere:
    @staticmethod
    def volume_of_sphere(radius):
        """
        Calculate the volume of a sphere given its radius.

        Parameters:
        radius (float): The radius of the sphere.

        Returns:
        float: The volume of the sphere.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        return (4/3) * Sphere.volume_of_circle(radius)

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the sphere: "))
        volume = Sphere.volume_of_sphere(radius)
        print(f"The volume of the sphere with radius {radius} is {volume}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")