#dùng kỹ thuật Slcing
s = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược (slicing):", s[::-1])

#không dùng kỹ thuật Slicing 
s = input("Nhập chuỗi: ")
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s
print("Chuỗi đảo ngược (không slicing):", reversed_s)


