class Vendor:
    def __init__(self, id, name, quantity, price):
        self.item_id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def print(self):
        print("Item Id:", self.item_id)
        print("Item Name:", self.name)
        print("Purchased Quantity:", self.quantity,"Kg")
        print("Price:", self.price)


class SuperMarket:
    def __init__(self):
        self.inventory = []

    def buyFromVendor(self):
        print("Enter Item Id,name,quantity and Price")
        obj = Vendor(int(input()), input(), int(input()), int(input()))
        self.inventory.append([obj.item_id, obj.name, obj.quantity, obj.price])
        obj.print()

    def sell(self):
        name = input("Enter Item Name:")
        quantity = int(input("Enter Quantity"))
        for items in self.inventory:
            if items[1]==name and quantity <= id[2]:
                print("Purchase was Successful")
                items[2] -= quantity
    def searchById(self, id):
        for items in self.inventory:
            if items[0] == id:
                print("Item name:", items[1])
                print("Item Quantity:", items[2])
                print("Item Price:", items[3])

    def searchByName(self, name):
        for items in self.inventory:
            if items[1] == name:
                print("Item Id:", items[0])
                print("Item Quantity:", items[2])
                print("Item Price:", items[3])
    def getInventory(self):
        for goods in self.inventory:
            print(goods)

if __name__=="__main__":
    market=SuperMarket()
    while 1:
        print("1.Inventory\n2.Buy From Vendor\n3.Sell To Customer\n4.Search By Id\n5.Search By Name\n6.Exit")
        num = int(input())
        if num == 1:
            market.getInventory()
        elif num == 2:
            market.buyFromVendor()
        elif num==3:
            print("Mini-Statement:")
            market.sell()
        elif num==4:
            market.searchById(int(input("Enter Item Id:")))
        elif num==5:
            market.searchByName((input("Enter Item Name:")))
        elif num==6:
            break