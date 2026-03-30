#Câu 1
n = int(input("Nhap so: "))

if n < 0:
    print("Loi: so am")
else:
    print("Phan du khi chia 2 la:", n % 2)


#Câu 2
s = input("Nhap chuoi: ")

print("Do dai chuoi:", len(s))
print("Chu hoa:", s.upper())


#Câu 3
i = 1
tong = 0

while i <= 30:
    if i % 2 == 1:
        print(i)
        tong = tong + i
    i = i + 1

print("Tong cac so le:", tong)


#Câu 4
def tinh_tong(n):
    if n == 0:
        return 0
    else:
        return n + tinh_tong(n - 1)

n2 = int(input("Nhap n: "))
print("Tong tu 1 den n:", tinh_tong(n2))


#Câu 5
class Flower:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


hoa = Flower("do")
print("Mau ban dau:", hoa.get_color())

hoa.set_color("vang")
print("Mau moi:", hoa.get_color())


#Câu6
def sap_xep(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp


a = [5, 2, 9, 1, 3]

sap_xep(a)
print("Mang sau khi sap xep:", a)