#bài 1
cannang = int(input("nhập cân nặng vào đây: "))
chieucao = float(input("nhập chiều cao vào đây: "))
BMI = cannang / (chieucao * chieucao)
lamtron = round(BMI, 2)
print(lamtron)

#bài 2
n = int(input("Nhập nhiều số để tính tổng: "))
tong = 0
while n > 0:
    chu_so = n % 10
    tong += chu_so
    n //= 10
print("Tổng các chữ số là:", tong)

#bài 3
def tinh_chinh_ten(ten: str) -> str:
    ten = ten.strip()
    cac_tu = ten.split()
    cac_tu_chuan = [tu.capitalize() for tu in cac_tu]
    return " ".join(cac_tu_chuan)
ten_nguoi_nhap = input("Nhập tên: ")
print("Tên: ", tinh_chinh_ten(ten_nguoi_nhap))

#bài 4




#bài 5
class User:
    def __init__(self,user_id):
        self.id = user_id
    @property
    def id(self):
        return self.id
#bài 6
class Product():
    def __init__(self, price):
        self.price = price
    @property
    def price(self, vaule):
        if vaule > 0:
            self._price = vaule
        else:
            raise ValueError("Giá trị phải lớn hơn 0")
    def __str__(self):
        return f"Giá trị {self.price}"
price = Product(2500)
print(price)
price.vaule = 1000
print(price)
#bài 7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s:str):
        name, age = s.split("-")
        return cls(name.strip(), int(age.strip()))
p = Person.from_string("Nam-20")
print(p.name)
print(p.age)
#bài 8
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __str__(self):
        return f"({self.x}, {self.y})"
x = Vector(2,3)
y = Vector(4,5)
print(x+y)

#bài 9
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Gâu gâu!")
d = Dog("Chó Đen")
print("Tên:", d.name)
d.sound()

#bài 10
