class Product:
    def __init__(self, price):
        self._price = None   
        self.price = price   
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá phải lớn hơn 0")
  def __str__(self):
        return f"Product price: {self._price}"
        
p = Product(19000)
print(p)

p.price = 20000
print(p)

