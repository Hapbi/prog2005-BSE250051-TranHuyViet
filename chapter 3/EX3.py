mau = ["Red", "Blue", "Green", "Yellow", "Purple"]
try:
    mau.remove("Green")
except ValueError:
    print("Không có màu Green trong danh sách")
print(mau)
