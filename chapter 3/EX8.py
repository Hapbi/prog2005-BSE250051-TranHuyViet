danhsach = list(map(int, input("Nhập danh sách số: ").split()))
found = None
for num in danhsach:
    if num > 10:
        found = num
        break
if found is not None:
    print("Số đầu tiên lớn hơn 10 là:", found)
else:
    print("Không có số nào lớn hơn 10")
