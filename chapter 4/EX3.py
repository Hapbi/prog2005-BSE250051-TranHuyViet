def kiem_tra_key(d, key):
    if key in d:
        print(f"Key '{key}' tồn tại trong dictionary.")
    else:
        print(f"Key '{key}' KHÔNG tồn tại trong dictionary.")
sinh_vien = {"Bốp": 9, "An": 8.5, "Bình": 7.5}
kiem_tra_key(sinh_vien, "An")
kiem_tra_key(sinh_vien, "Chi")

