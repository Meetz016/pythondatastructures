class ShopItems:
    def __init__(self):
        self.inventory = []

    def addItem(self, name, price, brandName):
        self.inventory.append([name, price, brandName])

    def show(self):
        for item in self.inventory:
            print(item)
    def findItem(self,name):
        flag=0
        for item in self.inventory:
            if item[2]==name:
                flag=1
                break
        if flag:
            print("YES")
        else:
            print("No")
    def total(self):
        s=0
        for item in self.inventory:
            s+=item[1]
        print(s)

if __name__ == "__main__":
    keeper = ShopItems()
    l1 = ["legion 5", "Oneplus Nord", "Geyser", "Fridge", "Washing Machine", "AC", "Heater", "Chocolate", "IceCream",
          "Paracetamol"]
    l2 = [100000,30000,2400,35000,20000,19000,26000,2300,1500,230,100]
    l3 = ["Lenovo","Oneplus","Bajaj","Panasonic","Panasonic","Lloyd","Bajaj","Dairy Milk","Havemore","Dolo-650"]
    for i in range(0,10):
        keeper.addItem(l1[i],l2[i],l3[i])
    keeper.total()
    keeper.findItem(input("Enter Item to find:"))

