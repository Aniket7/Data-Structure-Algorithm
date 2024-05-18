
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

    # function to merge two linked list
    def merge2SortedList(self,ll2):
        vector = []
        # assign both l1 & l2 to the head of the list
        l1 = self.head
        l2 = ll2.head

        # chcek 1st list empty or not
        while(l1!=None):
            vector.append(l1.data)
            l1 = l1.next

        # chcek 2nd list empty or not
        while(l2!=None):
            vector.append(l2.data)
            l2 = l2.next

        #print(vector)
        # create temporary temp_node for reference
        temp_node = Node(-1)
        temp1 = temp_node
        # add these values as nodes to the temp_node
        for i in range(len(vector)):
            temp_node.next = Node(vector[i])
            temp_node = temp_node.next

        # Node(-1) is not required so just forward the pointer to
        temp1 = temp1.next
        # print the merged list
        while(temp1):
            print(temp1.data, end="->")
            temp1 = temp1.next

        return

l = LinkedList()
l2 = LinkedList()

l.insertAtHead(1)
l.insertAtPos(2,2)
l.insertAtTail(3)
l.insertAtPos(4,8)
l.insertAtHead(0)
print("this is Linked List1 : ", end="")
l.traverse()

l2.insertAtHead(15)
l2.insertAtPos(20, 2)
l2.insertAtTail(25)
print("this is Linked List2 : ",end="")
l2.traverse()
print()
print("this is the output merged list : ", end="")
l.merge2SortedList(l2)


#OUTPUT
'''
this is Linked List1 : 0->1->2->3->4->
this is Linked List2 : 15->20->25->

this is the output merged list : 0->1->2->3->4->15->20->25->
'''