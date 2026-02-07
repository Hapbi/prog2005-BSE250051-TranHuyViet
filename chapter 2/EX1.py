nhapso = int(input("Nhập một số từ 1 đến 9: "))
if 1 <= nhapso <= 9:
    for i in range(1, 10):
        print(f"{nhapso} x {i} = {nhapso * i}")
else:
    print("Số không hợp lệ, vui lòng nhập từ 1 đến 9.")