danhsach = list(map(int, input("Nhập danh sách số: ").split()))
even_numbers = [num for num in danhsach if num % 2 == 0]
print("Các số chẵn:", even_numbers)
print("Tổng các số chẵn:", sum(even_numbers))
