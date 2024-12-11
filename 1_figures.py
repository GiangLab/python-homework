"""
принцип Барбары-Лисков изначально нарушался для класса Square (квадрат),
так как он наследовюется от класса Rectangle (прямоугольник).
Получается что при изменении высоты не меняется ширина, а при изменении ширины не изменяется высота.
Стороны квадрата получаются не равные, а следовательно искажается смысл класса квадрат: равенство сторон.

Решение проблемы: 
в классе Square были объявлены свойства height и width с помощью методов-сеттеров. 
При изменении одной из величин (ширины или высоты) происходит соответсвующее изменение второй величины.
"""

class Shape:
    #Класс: базовая фигура
    name = 'базовая фигура'

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return (f" {self.name}"
                f"( x ={self.__x}, y = {self.__y} )")
  
class Rectangle(Shape):
    # Класс: прямоугольник"""
    name = 'прямоугольник'

    def __init__(self, width, height, x=0, y=0):
        # вызывается конструктор родительского класса Shape, 
        # и передаются координаты x и y
        super().__init__(x, y) 
        self.width = width
        self.height = height
    @property
    def width(self):
        #возвращает ширину прямоугольника
        return self._width 

    @width.setter
    def width(self, value):
        #позволяет изменять ширину прямоугольника
        #значение свойства width
        self._width = value 

    @property
    def height(self):
        #возвращает высоту прямоугольника
        return self._height 

    @height.setter
    def height(self, value):
        #позволяет изменять высоту прямоугольника
        #значение свойства height
        self._height = value 

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (f"{Shape.__repr__(self)},"
                f" ширина: {self.width}, высота: {self.height},"
                f" площадь: {self.area()}, периметр: {self.perimeter()}")

class Square(Rectangle):
    #Класс: квадрат
    name = 'квадрат'
    def __init__(self, side, x=0, y=0):
        # вызывается конструктор родительского класса Rectangle, 
        # и передается координаты x и y 
        # и значение side для ширины width и высоты height
        super().__init__(side, side, x, y)

    @property
    def width(self):
        return self._width  # возвращаем width

    @width.setter
    def width(self, value):
        # устанавливает одинаковые значения для width и height квадрата
        self._width = value
        self._height = value  
    @property
    def height(self):
        # возвращаем высоту квадрата
        return self._height  

    @height.setter
    def height(self, value):
         # устанавливает одинаковые значения для width и height квадрата
        self._height = value
        self._width = value 
    
   # def __repr__(self):
   #     return (f"{Rectangle.__repr__(self)}")


rectangle_1=Rectangle(3,5,10)        
print(rectangle_1)
if (rectangle_1.width != rectangle_1.height):
   print(f"высота ({rectangle_1.height}) не равна ширине ({rectangle_1.width}).")
   
square_1 = Square(5,20,30)
print(square_1)
    
square_1.height = 10
print(f" высота изменилась на {square_1.height}.")
print(square_1)

if (square_1.width == square_1.height):
   print(f"ширина равна высоте и равна: {square_1.width}.")
    
square_1.width = 7
print(f"ширина изменилась на {square_1.width}.")
print(square_1)

if (square_1.width == square_1.height):
   print(f"высота равна ширине и равна: {square_1.height}.")
       
