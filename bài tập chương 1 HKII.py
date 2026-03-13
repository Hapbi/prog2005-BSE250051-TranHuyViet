# Bài 1
a = 4
b = 10
tinh_toan = (a**2 + b**2) / (a - b)
print(tinh_toan)

#Bài 2
import math
a = float(input("nhap so: "))
b = float(input("nhap so: "))
#lữy thừa
luy_thua = a ** b
#chia lấy phần nguyên
nguyen = a // b
#chia lấy phần dư
du = a % b
#làm tròn số
lam_tron = round(a)
lam_tron2 = round(b)
print("đây là lũy thừa", luy_thua)
print("lấy phần nguyên", nguyen)
print("chia lấy phần dư", du)
print("làm tròn số", lam_tron,lam_tron2)

#Bài 3
nhapdulieu = int(input("Nhập số từ 1 đến 9: "))
if 1 <= nhapdulieu <= 9:
    print(f"Bảng cửu chương của {nhapdulieu}")
    for i in range(1,10):
        print(f"{nhapdulieu} * {i} = {nhapdulieu * i}")
else:
    print("Số nhập phải là từ 1 đến 9: ")
    
#Bài 4
for i in range(1,101):
    if i % 3 == 0:
        continue
    print(i, end=" ")
    
#Bài 7
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points
hocsinh1 = Student("An Sinh Viên", 10)
hocsinh2 = Student("Bốp Sinh Viên", 9.5)
print("Tên:",hocsinh1.name, "//điểm:", hocsinh1.points)
print("Tên:",hocsinh2.name, "//điểm:", hocsinh2.points)

#Bài 8
class Student:
    def __init__(self, name, points):
        if 0 <= points <= 10:
            self.name = name
            self.points = points
        else:
            raise ValueError("Điểm phải từ 0 đến 10")
    def thongtin(self):
        print(f"Tên: {self.name}, điểm: {self.points}")
hocsinh = Student("Bốp", 11)
hocsinh2 = Student("An", 9.5)

#Bài 9
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def display(self):
        print(f"Tên: {self.name}, điểm: {self.points}")
hocsinh = Student("Bốp", 10)
hocsinh2 = Student("An", 9.5)
hocsinh.display()
hocsinh2.display()

#Bài 10
import matplotlib as plt:


