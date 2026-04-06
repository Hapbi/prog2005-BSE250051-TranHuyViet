n1 = int(float(input()))
n2 = int(float(input()))
print(n1 + n2)

#b2
def greet(name = "Student"):
    print("Hello", name)
greet()

#b3
def de_quy(n):
    if n <= 1:
        return 1
    return n * de_quy(n - 1)
n = int(input())
print(de_quy(n))
    
    
    
#b4
n1 = float(input())
n2 = float(input())
n3 = float(input())
tinh_diem = (n1 + n2 + n3) / 3
if tinh_diem >= 8:
    print("gioi")
elif tinh_diem >= 6.5:
    print("kha")
elif tinh_diem >= 5:
    print("trung binh")
else:
    print("yeu")
    
#b5
def count_vowels(s):
    chu = "aeiou"
    d = 0
for i in s.lower():
    if d in chu
        count += 1
    return d
nhap = input()
print(count_vowels(nhap))

#b6
mau = ["do","xanh","hong","tim","vang"]
    mau.remove("xanh")
print(mau)


#b7
students = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}
def tinh_trung_binh(ds):
    return sum(ds.values()) / len(ds)
print("Điểm trung bình:", tinh_trung_binh(students))


#b8
class Product:
    def __int__(self,price):
        self.price = o 
        self.set_price(price)
    def get_price(self):
        return self_price
    def set_price(self,price):
        if price < 0:
            print("loi")
        else:
            self_price = price
p = Product(100)
print(p.get_price())
p.set_price(-50)
print(p.get_price())

#b9
def luu_chuoi():
    s = input("Nhập chuỗi: ")
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(s)
luu_chuoi()


#b10
a = input("Nhập a: ")
b = input("Nhập b: ")
s = f"{a}---{b}"
print(s)
