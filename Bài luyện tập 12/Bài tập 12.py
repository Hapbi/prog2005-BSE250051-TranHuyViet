#Bài 1
print("Xin chào các bạn!")

#Bài 2
name = input("Nhap ten cua ban: ")
print("Xin chao:", name)

#Bài 3
nhapso = int(input("Nhập số bất kỳ: "))
nhapso1 = int(input("Nhập số bất kỳ: "))
print(nhapso)
print(nhapso1)
#Bai 4
nhapso = int(input("Nhap so: "))
if nhapso % 2 == 0:
    print(nhapso, " la so chan")
else:
    print(nhapso, "la so le")

#Bai 5
for i in range(1, 11):
    print(i)

#Bai 6
for i in range(1, 11):
    print("5 x",i,"=",5 * i)


#Bai 7
candy = int(input("Nhap so keo ban co: "))
if candy > 10:
    print("Bạn có nhiều kẹo quá!")
elif candy <= 10:
    print("Bạn có ít kẹo.")

#bai 8
namsinh = int(input("nhap so tuoi"))
nam_hien_nay = 2026
tinh_tuoi = nam_hien_nay - namsinh
print(tinh_tuoi)

#bai 9
nhapso = int(input("Nhap so bat ky"))
for i in range(nhapso):
    print("*" * nhapso)

#bai 10
import random
randomso = random.randint(1, 10)
nhapso = int(input("Nhap so bat ky "))
if nhapso == randomso:
    print("Bạn giỏi quá!", randomso)
else:
    print("Sai rồi!", randomso)
