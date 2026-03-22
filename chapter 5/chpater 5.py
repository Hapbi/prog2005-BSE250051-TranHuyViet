#bài 1
import matplotlib.pyplot as plt
categories = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]
plt.bar(categories, values, color="skyblue")
plt.title("Kết quả học tập của lớp")
plt.xlabel("Xếp loại")
plt.ylabel("Số lượng học sinh")
plt.show()


#bài 2
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
y1 = x**2
y2 = x**3
plt.plot(x, y1, color="blue", label="y = x^2")
plt.plot(x, y2, color="red", label="y = x^3")  # thêm dấu ) ở cuối
plt.title("Đồ thị các hàm số y = x^2 và y = x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


#bài 3
import matplotlib.pyplot as plt
products = ["A", "B", "C", "D", "E"]
sales = [30, 25, 15, 20, 10]
plt.pie(sales, labels=products, autopct="%1.1f%%", startangle=90)
plt.title("phần trăm doanh số các sản phẩm")
plt.show()

#bài 4
import matplotlib.pyplot as plt
cities = ["Los Angeles", "San Diego", "San Jose", "Bakersfield",
          "Fresno", "Oakland", "Sacramento", "Long Beach",
          "Anaheim", "San Francisco"]
areas = [1302, 964, 469, 382, 298, 202, 259, 130, 131, 121]
sorted_data = sorted(zip(areas, cities), reverse=True)
areas_sorted, cities_sorted = zip(*sorted_data)
plt.barh(cities_sorted, areas_sorted, color="skyblue")
plt.xlabel("Diện tích (km2)")
plt.title("Top 10 thành phố lớn nhất California theo diện tích")
plt.show()




