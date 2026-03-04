s = input("Nhập chuỗi: ")
if s.lower() == s[::-1].lower():
    print("Chuỗi là Palindrome")
else:
    print("Chuỗi không phải Palindrome")
