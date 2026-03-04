danhsach = list(map(int, input("Nhập danh sách số: ").split()))
odd_numbers = [num for num in danhsach if num % 2 != 0]
print("Các số lẻ trong danh sách:", odd_numbers)
