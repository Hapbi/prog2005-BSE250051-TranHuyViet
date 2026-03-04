danhsach = list(map(int, input("Nhập danh sách số: ").split()))
x = int(input("Nhập số cần tìm: "))
found = -1
for i in range(len(danhsach)):
    if danhsach[i] == x:
        found = i
        break
if found != -1:
    print("Chỉ số của", x, "là:", found)
else:
    print(x, "không có trong danh sách")
