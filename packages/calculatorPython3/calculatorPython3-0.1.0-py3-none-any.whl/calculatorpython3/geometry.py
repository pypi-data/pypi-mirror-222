import numpy as np
import math as m


class GeometryCalculator:
    def distance_between_points(self, p, q):
        """Calculate the distance between two points in 2D space."""
        return np.linalg.norm(np.array(p) - np.array(q))

    def angle_between_vectors(self, vector1, vector2):
        """Calculate the angle (in radians) between two vectors."""
        return np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))

    def area_of_circle(self, radius):
        """Calculate the area of a circle."""
        return m.pi * radius**2

    def circumference_of_circle(self, radius):
        """Calculate the circumference of a circle."""
        return 2 * m.pi * radius

    def rectangle_area(self, length, width):
        """Calculate the area of a rectangle."""
        return length * width

    def rectangle_perimeter(self, length, width):
        """Calculate the perimeter of a rectangle."""
        return 2 * (length + width)

    def square_area(self, side):
        """Calculate the area of a square."""
        return side * side

    def square_perimeter(self, side):
        """Calculate the perimeter of a square."""
        return 4 * side

    def circle_area(self, radius):
        """Calculate the area of a circle."""
        return m.pi * radius**2

    def circle_circumference(self, radius):
        """Calculate the circumference of a circle."""
        return 2 * m.pi * radius

    def triangle_area(self, base, height):
        """Calculate the area of a triangle."""
        return 0.5 * base * height

    def triangle_perimeter(self, side1, side2, side3):
        """Calculate the perimeter of a triangle."""
        return side1 + side2 + side3

    def parallelogram_area(self, base, height):
        """Calculate the area of a parallelogram."""
        return base * height

    def parallelogram_perimeter(self, side1, side2):
        """Calculate the perimeter of a parallelogram."""
        return 2 * (side1 + side2)

    def trapezoid_area(self, base1, base2, height):
        """Calculate the area of a trapezoid."""
        return 0.5 * (base1 + base2) * height

    def trapezoid_perimeter(self, side1, side2, side3, side4):
        """Calculate the perimeter of a trapezoid."""
        return side1 + side2 + side3 + side4

    def ellipse_area(self, major_axis, minor_axis):
        """Calculate the area of an ellipse."""
        return m.pi * major_axis * minor_axis

    def ellipse_circumference(self, major_axis, minor_axis):
        """Calculate the circumference of an ellipse."""
        circle_area = self.circle_area(minor_axis / 2)
        circle_circumference = self.circle_circumference(minor_axis / 2)
        a = major_axis / 2
        return 2 * m.pi * m.sqrt((a**2 + circle_area) / 2) + circle_circumference
