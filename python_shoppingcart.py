class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    


class ShoppingCart:
    def __init__(self):
        self.totalprice = 0
        self.count = 0
        pass
        
    def add(self,item):
        self.count += 1
        self.totalprice += item.price
        
    def total(self):
        return self.totalprice
        
    def __len__(self):
        return self.count
    
cart = ShoppingCart()
cart.add(Item('guitar',1000))
print(cart.total()) # 1000    
print(cart.len())
print(len(cart))
 # 1


        