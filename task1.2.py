class Shape:
    def __init__(self, color, is_filled, created_date):
        self.__color = color
        self.__is_filled = is_filled
        self.__created_date = created_date
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    
    def get_is_filled(self):
        return self.__is_filled
    def set_is_filled(self, fill):
        self.__is_filled = fill

    def get_created_date(self):
        return self.__created_date
    def set_color(self, date):
        self.__created_date = date

    def get_area(self, a):
        return a*a
    def get_perimeter(self, a):
        return 4*a
    def describe(self):
        print("color:", self.__color, "filled:", self.__is_filled, "data:", self.__created_date)
    def compare_shapes(self, shapes_list):
        for shape in shapes_list:
            return self.get_area == shape
        
    def get_dimension(self, a):
        return a
        

    
        
class Circle(Shape):
    def __init__(self, color, is_filled, created_data, radius):
        super().__init__(color, is_filled, created_data)
        self.__radius = radius

    def get_area(self):
        print("circle")

    def get_perimeter(self, radius):
        return 3.14 * radius * radius
    
    def get_diameter(self, radius):
        return 2 * radius
    
    def get_dimension(self, radius):
        return radius
    
    def __eq__(self, other):
        return self.get_area() == other.get_area()
    
    def __gt__(self, other):
        return self.get_perimeter() > other.get_perimeter()
    
    def __mul__(self, more):
        self.__radius *= more

    def __str__(self):
        print("circle: radius:", self.__radius, "color:", self.__color)