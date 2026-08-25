class Example:
    x = 100
    def display(self):
        print("Hello World")

obj = Example()
print(obj.x)
obj.display()

class Circle:
    r = 14
    def area(self,r):
        return 3.14 * r * r
    def perimeter(self,r):
        return 2 * 3.14 * r

obj = Circle()
print("Area of Circle is:",obj.area(14))
print("Perimeter of Circle is:",obj.perimeter(14))
print("Area of Circle is:",obj.area(7))
print("Perimeter of Circle is:",obj.perimeter(7))