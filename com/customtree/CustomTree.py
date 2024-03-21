class BinTree:
    def __init__(self,val=0):
        self.data=val
        self.left=None
        self.right=None
    def insert(self,val):
        if self.data is None:
            self.data=val