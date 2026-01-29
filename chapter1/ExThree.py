so1 = int(input('Nhập số nguyên thứ nhât: '))
so2 = int(input('Nhâp số nguyên thứ hai: '))

tong = so1 + so2
hieu = so1 - so2
tich = so1 * so2

if so1 == 0:
    print("không thể chia")
    if so2 == 0:
        print("không thể chia")
else:
    thuong = "không thể chia"

print("Tổng:",tong)
print("Hiệu:",hieu)
print("Tích",tich)
print("Thương:",thuong)
