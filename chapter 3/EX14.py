def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

s = input("Nhập chuỗi: ")
print("Số lượng nguyên âm:", count_vowels(s))
