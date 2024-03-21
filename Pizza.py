class Building:
    def __init__(self,name,floors):
        self.name=name
        self.floors=floors
    def display_info(self):
        return f"{self.name} has {self.floors} floors."


class House(Building):
    def __init__(self,name,floors,bedrooms):
        super().__init__(name,floors)
        self.bedrooms= bedrooms

        def display_info(self):
            base_info=super().display_info()
            return f"{base_info} It's a house with {self.bedrooms} bedrooms."

x=Building("Meet's Villa",10)
y=House(1,x.floors,x.name)
print(y.display_info())