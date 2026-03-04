danhsach = list(map(int, input("Nhập danh sách số nguyên: ").split()))
swap_count = 0
for i in range(len(danhsach)):
    for j in range(0, len(danhsach) - i - 1):
        if danhsach[j] > danhsach[j + 1]:
            danhsach[j], danhsach[j + 1] = danhsach[j + 1], danhsach[j]
            swap_count += 1
print("Danh sách sau khi sắp xếp:", danhsach)
print("Số lần hoán đổi:", swap_count)
