danhsach = list(map(float, input("Nhập danh sách số thực: ").split()))
for i in range(1, len(danhsach)):
    key = danhsach[i]
    j = i - 1
    while j >= 0 and danhsach[j] < key:
        lst[j + 1] = danhsach[j]
        j -= 1
    danhsach[j + 1] = key
print("Danh sách sau khi sắp xếp giảm dần:", danhsach)
