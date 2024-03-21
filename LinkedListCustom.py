class Node:
    def __init__(self, num=0):
        self.num = num
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def appendNode(self, data=0):
        nn = Node(data)
        if self.head is None:
            self.head = nn
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = nn
        self.size += 1

    def show(self):
        temp = self.head
        while temp is not None:
            print(temp.num, "->", end="")
            temp = temp.next
        print("NONE")

    def delete(self, num):
        if self.head == None:
            return
        if self.head.num == num:
            self.head = self.head.next
        if self.head.next == None and self.head.num == num:
            head = None
            self.size -= 1
            return
        curr = self.head
        next = curr.next

        while next != None:
            if next.num == num:
                curr.next = next.next
                return
            curr = next
            next = next.next
        self.size += 1

    def deleteAtPosition(self, pos):
        if self.head == None:
            return
        if self.head.next == None and pos > 1:
            print("Index Out of range")
            return
        if pos == self.size:
            self.deleteLast()
        if pos > self.size:
            print("Position Out Of Bound")
            return
        index = 0
        temp = self.head
        while temp.next != None and index != pos - 1:
            temp = temp.next
            index += 1
        # reached the node to be deleted
        if (temp.next == None):
            temp = None
        else:
            temp.num = temp.next.num
            temp.next = temp.next.next

    def deleteLast(self):
        if self.head == None:
            return
        if self.head.next == None:
            head = None
            return
        prev = None
        curr = self.head
        while curr.next != None:
            prev = curr
            curr = curr.next
        prev.next = None

    def insertAtPosition(self, pos, val):
        if self.head == None:
            self.appendNode(val)
            return
        if pos > self.size:
            print("Out of Bound")
            return
        nn = Node(val)
        if pos == 1:
            nn.next = self.head
            self.head = nn
            return
        index = 1
        prev = self.head
        while prev.next != None and index != pos - 1:
            prev = prev.next
            index += 1
        # reached before node
        nn.next = prev.next
        prev.next = nn

    def sortLLBubble(self):
        slow = self.head
        for i in range(self.size):
            fast = slow.next
            while fast:
                if slow.num > fast.num:
                    slow.num, fast.num = fast.num, slow.num
                fast = fast.next
            slow = slow.next

    def selectionSort(self):
        slow = self.head
        while slow:
            minI = slow
            fast = slow.next

            while fast:
                if minI.num > fast.num:
                    minI = fast
                fast = fast.next
            slow.num, minI.num = minI.num, slow.num
            slow = slow.next

    def getMaxDiff(self):
        if self.size<2:
            print(0)
            return
        slow = self.head
        maxDiff = 0
        while slow.next is not None:
            if slow.next.num - slow.num > maxDiff:
                maxDiff = slow.next.num - slow.num
            slow = slow.next
        print(maxDiff)
    def findMajority(self):
        ele = self.head.num
        count = 0
        slow = self.head
        while slow:
            if count == 0:
                ele = slow.num
            if ele == slow.num:
                count += 1
            else:
                count -= 1
            slow = slow.next
        print(ele)

if __name__ == '__main__':
    ll = LinkedList()
    l = list(map(int, input().split()))
    for ele in l:
        ll.appendNode(ele)
    # ll.sortLLBubble()
    # ll.getMaxDiff()
    ll.show()
    ll.findMajority()
