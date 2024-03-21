class Vendor:
    def __init__(self,id,name,quantity,price):
        self.item_id=id
        self.name=name
        self.quantity=quantity
        self.price=price
    def print(self):
        print("Item Id:",self.item_id)
        print("Item Name:",self.name)
        print("Purchased Quantity:",self.quantity)
        print("Price:",self.price)

