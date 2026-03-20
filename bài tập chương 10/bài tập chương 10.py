#bài 1
import os
def get_layfile(path):
    return os.path.join(path)
def lay_tenbainhac(path):
    layfile = os.path.basename(path)
    name, _ = os.path.splitext(layfile)
    return name

path = "Tên file nhạc: d:\\music\\muabui.mp3"
print(lay_tenbainhac(path))
print(get_layfile(path))
#bài 2
nhapchuoi = input("Nhập chuỗi: ")
nhapkytu = input("Nhập ký tự: ")
solan = s.count(nhapkytu)
print(f"Ký tự {nhapkytu} xuất hiện {solan} lần trong chuỗi")

#bài 3
def hamdequy(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hamdequy(n-1)

nhap = int(input("Nhập một số nguyên dương:"))
print(f"Giai thừa của {nhap} là {hamdequy(nhap)}")

#bài 4
nhap = input("Nhập vào một chuỗi: ")
if len(nhap) == 0:
    print("Lỗi")
else:
    print(f"Độ dài của chuỗi là: {len(nhap)}")

#bài 5
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, x**2, color='blue')
ax1.set_title("Đồ thị y = x^2")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax2.plot(x, np.sqrt(x), color='green')
ax2.set_title("Đồ thị y = √x")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
plt.tight_layout()
plt.show()

#bài 6
s = input("Nhập vào một chuỗi: ")
reversed_s = ""
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]
print("chuỗi đảo ngược: ", reversed_s)

#bài 7
matkhau = ""
while matkhau != "python123":
    matkhau = input("Nhập mật khẩu: ")
    if matkhau != "python123":
        print("Sai mật khẩu, vui lòng thử lại!")
print("Đăng nhập thành công!")

#bài 8
strings = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    strings.append(s)
n = len(strings)
for i in range(n - 1):
    for j in range(n - i - 1):
        if len(strings[j]) < len(strings[j + 1]):
            strings[j], strings[j + 1] = strings[j + 1], strings[j]
        print(f"Bước {i}-{j}: {strings}")

print("\nKết quả cuối cùng (giảm dần theo độ dài):")
print(strings)

#bài 9
?





#bài 10
strings = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    strings.append(s)
n = len(strings)
for i in range(n):
    for j in range(0, n-i-1):
        if len(strings[j]) < len(strings[j+1]):
            strings[j], strings[j+1] = strings[j+1], strings[j]
print("Các chuỗi sau khi sắp xếp theo độ dài giảm dần:")
for s in strings:
    print(s, "(", len(s), "ký tự )")

#bài 11
def bubble_sort_desc(strings):
    n = len(strings)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(strings[j]) < len(strings[j+1]):
                strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings
while True:
    print("\n1. Sắp xếp chuỗi")
    print("2. Thoát")
    ch = input("Chọn: ")
    if ch == "1":
        arr = []
        i = 0
        while i < 5:
            arr.append(input(f"Chuỗi {i+1}: "))
            i += 1
        arr = bubble_sort_desc(arr)
        print("Kết quả:", arr)
    elif ch == "2":
        break
    else:
        print("Sai lựa chọn!")