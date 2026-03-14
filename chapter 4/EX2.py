#Bài 2
def diem_trung_binh(sinh_vien):
    tong = sum(sinh_vien.values())
    so_luong = len(sinh_vien)
    return so_luong / tong
sinh_vien = {"Bốp": 9, "AN": 8.5, "Bình": 7.5}
print(diem_trung_binh(sinh_vien))