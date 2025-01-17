import math


class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """
        String representation of the quaternion.
        """
        return f"Quaternion(w={self.w}, x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        """
        Add two quaternions component-wise.
        """
        return Quaternion(
            self.w + other.w,
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other):
        """
        Subtract two quaternions component-wise.
        """
        return Quaternion(
            self.w - other.w,
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __mul__(self, other):
        """
        Multiply two quaternions or a quaternion by a scalar.
        """
        if isinstance(other, Quaternion):
            # Multiplying two quaternions
            w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
            z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
            return Quaternion(w, x, y, z)
        elif isinstance(other, (int, float)):
            # Multiplying quaternion by a scalar
            return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Multiplication with unsupported type.")

    def magnitude(self):
        """
        Calculate the magnitude (norm) of the quaternion.
        """
        return math.sqrt(self.w**2 + 
                         self.x**2 + 
                         self.y**2 + 
                         self.z**2)

    def conjugate(self):
        """
        Calculate the conjugate of the quaternion.
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self):
        """
        Calculate the inverse of the quaternion.
        """
        mag_squared = self.magnitude() ** 2
        if mag_squared == 0:
            raise ZeroDivisionError("Cannot invert a quaternion with zero magnitude.")
        return self.conjugate() * (1 / mag_squared)

    def __truediv__(self, other):
        """
        Divide one quaternion by another or a scalar.
        """
        if isinstance(other, Quaternion):
            return self * other.inverse()
        elif isinstance(other, (int, float)):
            return Quaternion(self.w / other, self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Division with unsupported type.")

    def rotate_vector(self, vector):
        """
        Rotate a 3D vector using the quaternion.
        :param vector: A tuple (x, y, z) representing the vector.
        :return: A tuple (x', y', z') representing the rotated vector.
        """
        vector_q = Quaternion(0, *vector)
        rotated_q = self * vector_q * self.inverse()
        return (rotated_q.x, rotated_q.y, rotated_q.z)

    def __eq__(self, other):
        """
        Check equality of two quaternions.
        """
        if not isinstance(other, Quaternion):
            return NotImplemented
        return (
            math.isclose(self.w, other.w, rel_tol=1e-9)
            and math.isclose(self.x, other.x, rel_tol=1e-9)
            and math.isclose(self.y, other.y, rel_tol=1e-9)
            and math.isclose(self.z, other.z, rel_tol=1e-9)
        )


# Testing the fixed code

# Create two quaternions
q1 = Quaternion(0, 1, 2, 3)
q2 = Quaternion(1.5, 2.5, -2, 3)

print("Quaternion 1:", q1)
print("Quaternion 2:", q2)
print("Sum:", q1 + q2)
print("Difference:", q1 - q2)
print("Product:", q1 * q2)
print("Division:", q1 / q2)

# Rotate a vector
vector = (1, 0, 0)
rotated_vector = q1.rotate_vector(vector)

print("Rotated vector (1,1,1):",rotated_vector)
