class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert node at beginning
    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head

    # insert node at tail
    def insertAtTail(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            return new_node
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
        return

    # insert node at any position
    def insertAtPos(self, data, pos):
        temp = self.head
        new_node = Node(data)
        counter = 1
        if self.head is None:
            self.head = new_node
            return
        if pos == 1:
            self.insertAtHead(data)
        else:
            while(pos - 1 != counter and temp.next != None):
                counter += 1
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    # print the linked list
    def traverse(self):
        temp = self.head
        if temp is None:
            print("Linked List is empty")
            return
        else:
            while(temp):
                print(temp.data, end="->")
                temp = temp.next
            print()
        return

    # it will chek the value in the entire list
    def findNode(self, value):
        temp = self.head
        if temp is None:
            print("Linked list is empty")
            return
        else:
            while(temp):
                if(temp.data==value):
                    print(f"{value} is present in this Linked List")
                temp = temp.next
        return

    # it will check the value at specific position
    def findNodeAtPos(self, pos, value):
        temp = self.head
        count = 1
        if temp is None:
            print("Linked List is empty")
            return
        if pos==1:
            if temp.data == value:
                print(f"data {value} is present at the {pos} node in this linked list")
            else:
                print(f"data {value} is not present at the {pos} node in this linked list")
        else:
            while(temp!=None and pos-1!=count):
                count += 1
                temp = temp.next
            if(temp.next.data == value):
                print(f"data {value} is present at the {pos} node in this linked list")
                return
            else:
                print(f"data {value} is not present at the {pos} node in this linked list")
                return

l = LinkedList()

l.insertAtHead(1)
l.insertAtPos(2,2)
l.insertAtTail(3)
l.insertAtPos(4,8)
l.insertAtHead(0)
print("Linked List: ", end="")
l.traverse()
print()
l.findNode(3)
print()
l.findNodeAtPos(1,0)
print()
l.findNodeAtPos(3, 2)
print()
l.findNodeAtPos(4, 1)

# OUTPUT
'''
3 is present in this Linked List

data 0 is present at the 1 node in this linked list

data 2 is present at the 3 node in this linked list

data 1 is not present at the 4 node in this linked list

'''