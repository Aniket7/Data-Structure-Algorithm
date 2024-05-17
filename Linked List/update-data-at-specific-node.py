class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head

    def insertAtTail(self, data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            while(temp.next!=None):
                temp = temp.next

            temp.next = new_node
        return self.head

    def insertAtPos(self, data, pos):
        temp = self.head
        c = 1
        new_node = Node(data)
        if temp is None:
            self.head = new_node
            return self.head
        if pos == c:
            self.insertAtHead(data)
        else:
            while(temp.next != None and pos-1!=c):
                c +=1
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        return self.head

    def getLength(self):
        temp = self.head
        c = 0
        while(temp):
            temp = temp.next
            c +=1
        print("length of list is", c)
        return c

    def updateValueAtPos(self, value, pos):
        temp = self.head
        c = 1
        length = self.getLength()
        if temp is None:
            print("list is empty")
            return
        if pos > length:
            print("position is beyond the list")
            return
        else:
            while(temp.next!=None and pos-1!=c):
                temp = temp.next
                c += 1
            temp.next.data = value
        return self.head



    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data, end="->")
            temp = temp.next
        print()



l = LinkedList()
l.insertAtHead(1)
l.insertAtTail(2)
l.insertAtPos(1.5, 2)
l.insertAtPos(1.9, 3)
l.insertAtTail(3)
l.traverse()
l.updateValueAtPos(1.7, 3)
l.traverse()
l.updateValueAtPos(4, 6)

'''
OUTPUT ->
1->1.5->1.9->2->3->
length of list is 5
1->1.5->1.7->2->3->
length of list is 5
position is beyond the list

'''



