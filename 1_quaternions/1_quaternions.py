import math


class Quaternion:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        """
        Инициализация кватерниона с параметрами: a, b, c, d

        :param a: скалярная часть
        :param b, c, d: векторная часть
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        """
        Операция сложения

        :param other: другой кватернион, с которым складываем
        :return: квартернион, который является результатом сложения
        """
        return Quaternion(self.a + other.a,
                         self.b + other.b,
                         self.c + other.c,
                         self.d + other.d)

    def __mul__(self, other):
        """
        Операция умножение

        :param other: другой кватернион, с которым перемножаем
        :return: квартернион, который является результатом перемножения
        """
        a = self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d
        b = self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c
        c = self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b
        d = self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a
        return Quaternion(a, b, c, d)

    def conjugate(self):
        """
        Получаем комплексно-сопряженный кватернион

        :return:
        """
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def magnitude(self):
        """
        Норма квартерниона

        :return:
        """
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)

    def reverse(self):
        """
        Обратный квартернион

        :return:
        """
        n = self.magnitude() ** 2
        return Quaternion(self.a / n, -self.b / n, -self.c / n, -self.d / n)

    def rotate_vector(self, vector):
        """
        Поворот вектора на квартернион

        :param vector: вектор, который нужно повернуть
        :return:
        """
        quat = Quaternion(0, *vector)
        rot_vec = self * quat * self.reverse()
        return (rot_vec.b, rot_vec.c, rot_vec.d)

    def __str__(self):
        """
        Вывод квартерниона

        :return:
        """
        return f'Квартернион({self.a}, {self.b}, {self.c}, {self.d})'


if __name__ == '__main__':
    # Создаем два кватерниона
    q1 = Quaternion(1, 0, 1, 0)
    q2 = Quaternion(0, 1, 0, 1)

    # Основные операции
    print("Кватернион q1:", q1)
    print("Кватернион q2:", q2)

    # Сложение
    print("Сложение q1 + q2:", q1 + q2)

    # Умножение
    print("Умножение q1 * q2:", q1 * q2)

    # Сопряжение
    print("Сопряжение q1:", q1.conjugate())

    # Норма
    print("Норма q1:", q1.magnitude())

    # Обратный кватернион
    print("Обратный q1:", q1.reverse())

    # Поворот вектора
    vector = [1, 0, 0]  # Вектор для поворота
    angle = math.pi / 2  # Угол поворота (90 градусов)
    rotation_quaternion = Quaternion(math.cos(angle / 2), 0, 0, math.sin(angle / 2))
    rotated_vector = rotation_quaternion.rotate_vector(vector)
    print("Повернутый вектор:", rotated_vector)