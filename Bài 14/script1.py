#b1
p = 3.14
n = float(input())
tinh_so = n * 2 * p
print(tinh_so)

#b2
n = 5
a = []
for i in range(n):
a.append(input())
print(a)
a.pop(1)
print(a)

#b3
def may (n):
d = 0
if n  < 2:
    return False
for i in range(3, int(n * 0,5)+1):
    if n % i == 0:
        return False
    return True
n = int(input())
t = 0
a = list(map(int, input().split()))
for i in range (0,n):
    if a[i]%2 != 0:
        t = t + a[i]
        print(t)
for i in range(1,n):
    if may a[i]:
        print(a[i],end = "")

#b4
class book():
    def __init__(self, n):
        self.n = n
        self.p = p
    def get_name(self):
        return self.n
    def get_name (self,n):
        self.n = n
    def get_price(self):
        return self.p
    def set_price(self,p):
        self.p = p
    b = book("python", 100)
    print(b.get_price(1))
    b.get_price(120)
    print(b.get_price)


#b5
books = {
    "Book 1": 30000,
    "Book 2": 50000,
    "Book 3": 100000
}
tong = sum(books.values())
with open("data.txt", "w", encoding="utf-8") as f:
    for ten, gia in books.items():
        f.write(f"{ten};{gia}\n")
    f.write(f"Tong;{tong}")
#b6
layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}
print(layers["layer-12"])
print(layers["layer-11"]["layer-22"]["layer-31"])