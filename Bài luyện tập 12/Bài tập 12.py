#Bài 1 Hãy viết chương trình Python để in ra màn hình dòng chữ:
Xin chào các bạn!
print("Xin chào các bạn!")

#Bài 2 Hãy viết chương trình nhập tên từ bàn phím và in ra:

Xin chào [tên]!
name = input("Nhap ten cua ban: ")
print("Xin chao:", name)

#Bài 3 Hãy viết chương trình nhập hai số từ bàn phím và in ra tổng của hai số đó.
nhapso = int(input("Nhập số bất kỳ: "))
nhapso1 = int(input("Nhập số bất kỳ: "))
print(nhapso)
print(nhapso1)
#Bai 4  Hãy viết chương trình nhập một số nguyên và cho biết số đó là số chẵn hay số lẻ.
nhapso = int(input("Nhap so: "))
if nhapso % 2 == 0:
    print(nhapso, " la so chan")
else:
    print(nhapso, "la so le")

#Bai 5 Hãy viết chương trình dùng vòng lặp for để in các số từ 1 đến 10.
for i in range(1, 11):
    print(i)

#Bai 6  Hãy viết chương trình in bảng cửu chương 5 từ 5 x 1 đến 5 x 10.
for i in range(1, 11):
    print("5 x",i,"=",5 * i)


#Bai 7 Hãy viết chương trình nhập một số kẹo.

Nếu số kẹo lớn hơn 10 thì in: Bạn có nhiều kẹo quá!
Nếu ≤ 10 thì in: Bạn có ít kẹo.

candy = int(input("Nhap so keo ban co: "))
if candy > 10:
    print("Bạn có nhiều kẹo quá!")
elif candy <= 10:
    print("Bạn có ít kẹo.")

#bai 8 Hãy viết chương trình nhập năm sinh của người dùng và tính tuổi của họ.
namsinh = int(input("nhap so tuoi"))
nam_hien_nay = 2026
tinh_tuoi = nam_hien_nay - namsinh
print(tinh_tuoi)

#bai 9  Hãy viết chương trình nhập một số n và in ra hình vuông n × n bằng dấu *.
nhapso = int(input("Nhap so bat ky"))
for i in range(nhapso):
    print("*" * nhapso)

#bai 10  Hãy viết chương trình game đoán số:

Máy tính chọn một số từ 1 đến 10
Người chơi nhập số đoán
Nếu đúng → in Bạn giỏi quá!
Nếu sai → in Sai rồi!
import random
randomso = random.randint(1, 10)
nhapso = int(input("Nhap so bat ky "))
if nhapso == randomso:
    print("Bạn giỏi quá!", randomso)
else:
    print("Sai rồi!", randomso)
