# class which defines node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define a structure of link list
class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return self.head

    # insert node at tail
    def insertAtTail(self, data):
        if self.head is None:
            return self.head
        new_node = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        self.tail = new_node
        return self.head

    def insertAtPos(self, data, pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        counter = 1
        temp = self.head
        if pos == counter:
            self.insertAtHead(data)
        else:
            while(pos-1!=counter and temp.next!=None):
                temp = temp.next
                counter += 1
            new_node.next = temp.next
            temp.next = new_node
        return self.head

    def traverse(self):
        temp = self.head
        c = 0
        while(temp):
            c+=1
            print(temp.data, end="->")
            temp = temp.next
        print()
        print("length of a linkedList is", c)


l1 = LinkList()
l1.insertAtHead(2)
l1.insertAtTail(5)
l1.insertAtHead('A')
l1.insertAtTail(3)
l1.insertAtPos(99,2)
l1.insertAtPos(33,1)
l1.insertAtPos(5, 9)
l1.traverse()





