#bài 1
arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    print(f"\nBước {i}:")
    print("Key =", key)
    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1
        print("  Dịch chuyển:", arr)
    arr[j + 1] = key
    print("  Chèn key:", arr)
print("\nKết quả cuối cùng:", arr)







#bài 2
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
arr = ['hello','no problem','abcxyz','hi','nice']
nhap = input("Nhập từ vào đây: ")
timkiem = binary_search(arr,nhap)
if timkiem != -1:
    print("Nahhh")
else:
    print("Không thấy")







#bài 3
sotinh = list(map(int,input("Nhập số vào đây: ").split()))
songaunhien = []
tatca = 0
for num in sotinh:
    if num % 2 == 0:
        songaunhien.append(num)
        tatca += num
print("Số chẵn", songaunhien)
print("Số lẻ", tatca)








#bài 4
def songuyen(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
so = list(map(int,input("").split()))
so.append(int(input()))
k = int(input())
print(sum(x for x in so if songuyen))
so.sort()
print(so)
so.clear()
print(so)





#bài 5
data = {
    "An": 18,
    "Bình": 20,
    "Cường": 19
}
key = input("Nhập key cần kiểm tra: ")
if key in data:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại")







#bài 6
chiu = int(input("Nhập số người: "))
data = {}
for i in range(chiu):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    data[ten] = tuoi
tinhtuoi = sum(data.values()) / len(data)
print("Tuổi trung bình:", tinhtuoi)
print("Thông tin:", data)







#bài 7
import csv
n = int(input("Số nhân viên: "))
data = []
for i in range(n):
    ten = input("Tên: ")
    tuoi = input("Tuổi: ")
    id_nv = input("ID: ")
    data.append([ten, tuoi, id_nv])
with open("nv.txt", "w", encoding="utf-8") as f:
    for nv in data:
        f.write(", ".join(nv) + "\n")
with open("nv.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(data)
print("\nTXT:\n", open("nv.txt", encoding="utf-8").read())
print("CSV:\n", open("nv.csv", encoding="utf-8").read())





#bài 8
sinh_vien = ("An", 18, 8.5)
ten, tuoi, diem_tb = sinh_vien
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Điểm TB:", diem_tb)










#bài 9
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
diem_tb = float(input("Nhập điểm TB: "))
sinh_vien = (ten, tuoi, diem_tb)
t, u, d = sinh_vien
print("Tên:", t)
print("Tuổi:", u)
print("Điểm TB:", d)
