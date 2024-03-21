class Employee:
    def __init__(self,eId,eFname,eSname,ePhoneNo):
        self.eId=eId
        self.eFname=eFname
        self.eSname=eSname
        self.ePhoneNo=ePhoneNo

class Node:
    def __init__(self, emp):
        self.eId = emp.eId
        self.eFname=emp.eFname
        self.eSname=emp.eSname
        self.ePhoneNo=emp.ePhoneNo
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def appendNode(self, data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = nn
        self.size+=1

    def show(self):
        temp = self.head
        sId=1
        print("-----------------------------")
        print("s.no  eId    FName     LName       PhoneNo ")
        while temp is not None:
            print(f'{sId}  =  [{temp.eId} ,   {temp.eFname} ,   {temp.eSname} ,   {temp.ePhoneNo}]')

            sId+=1
            temp = temp.next
        print("-----------------------------")
    def delete(self,num):
        if self.head==None:
            return
        if self.head.num==num:
            self.head=self.head.next
        if self.head.next==None and self.head.num==num:
            head=None
            self.size-=1
            return
        curr=self.head
        next=curr.next

        while next!=None:
            if next.num==num:
                curr.next=next.next
                return
            curr=next
            next=next.next
        self.size+=1

    def deleteAtPosition(self,pos):
        if self.head==None:
            return
        if self.head.next==None and pos>1:
            print("Index Out of range")
            return
        if pos==self.size:
            self.deleteLast()
        if pos>self.size:
            print("Position Out Of Bound")
            return
        index=0
        temp=self.head
        while temp.next!=None and index!=pos-1:
            temp=temp.next
            index+=1
        #reached the node to be deleted
        if(temp.next==None):
            temp=None
        else:
            temp.num=temp.next.num
            temp.next=temp.next.next
    def deleteLast(self):
        if self.head==None:
            return
        if self.head.next==None:
            head=None
            return
        prev=None
        curr=self.head
        while curr.next!=None:
            prev=curr
            curr=curr.next
        prev.next=None
    def insertAtPosition(self,pos,val):
        if self.head==None:
            self.appendNode(val)
            return
        if pos>self.size:
            print("Out of Bound")
            return
        nn = Node(val)
        if pos==1:
            nn.next=self.head
            self.head=nn
            return
        index=1
        prev=self.head
        while prev.next!=None and index!=pos-1:
            prev=prev.next
            index+=1
        #reached before node
        nn.next=prev.next
        prev.next=nn
    def sortByfirstName(self):
        slow=self.head
        for i in range(self.size):
            fast=slow.next
            while fast:
                if ord(slow.eFname[0])>ord(fast.eFname[0]):
                    slow.eFname,fast.eFname=fast.eFname,slow.eFname
                    slow.eSname,fast.eSname=fast.eSname,slow.eSname
                    slow.eId,fast.eId=fast.eId,slow.eId
                    slow.ePhoneNo,fast.ePhoneNo=fast.ePhoneNo,slow.ePhoneNo

                fast=fast.next
            slow=slow.next
    def sortByPhoneNo(self):
        slow=self.head
        for i in range(self.size):
            fast=slow.next
            while fast:
                if (slow.ePhoneNo)>(fast.ePhoneNo):
                    slow.eFname,fast.eFname=fast.eFname,slow.eFname
                    slow.eSname,fast.eSname=fast.eSname,slow.eSname
                    slow.eId,fast.eId=fast.eId,slow.eId
                    slow.ePhoneNo,fast.ePhoneNo=fast.ePhoneNo,slow.ePhoneNo

                fast=fast.next
            slow=slow.next


if __name__=='__main__':
    e1=Employee(10,"Meet","Kotadiya",9876543921)
    e2=Employee(20,"Ajay","Malhotra",4982374931)
    e3=Employee(30,"Virat","Kohli",123456789)
    ll=LinkedList()
    ll.appendNode(e1)
    ll.appendNode(e2)
    ll.appendNode(e3)
    print("Unsorted Data")
    ll.show()
    print("Sorting By First Name")
    #sort by firstName
    ll.sortByfirstName()
    ll.show()
    print("sort by Phone No")
    #sort by secondName
    ll.sortByPhoneNo()
    ll.show()
