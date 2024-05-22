# initialize node structure
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# initialize LinkedList structure
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert node at beginning
    def insertNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            new_node.next = self.head
            self.head = new_node
        return

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

    def removeDuplicateNodeFromSortedList(self):
        temp = self.head
        if temp is None or temp.next is None:
            return self.head
        else:
            while(temp and temp.next):
                if(temp.data==temp.next.data):
                    temp.next = temp.next.next
                    temp = temp.next
                else:
                    temp = temp.next


    def removeDuplicateNodeFromUnsortedList(self):

        if self.head is None or self.head.next is None:
            return self.head

        temp = self.head
        visited = set()
        visited.add(temp.data)
        # run the loop
        while(temp.next!=None):
            if temp.next.data in visited:
                temp.next = temp.next.next
            else:
                visited.add(temp.next.data)
                temp = temp.next
        return


l = LinkedList()

'''
l.insertNode(5)
l.insertNode(5)
l.insertNode(4)
l.insertNode(3)
l.insertNode(3)
l.insertNode(2)
l.insertNode(2)
l.insertNode(1)
l.insertNode(0)
l.insertNode(0)
l.traverse()
l.removeDuplicateNodeFromSortedList()
print("after removing duplicates list becomes ")
l.traverse()
'''

#OUTPUT
'''
0->0->1->2->2->3->3->4->5->5->

after removing duplicates list becomes 
0->1->2->3->4->5->
'''


l.insertNode(5)
l.insertNode(2)
l.insertNode(4)
l.insertNode(0)
l.insertNode(3)
l.insertNode(2)
l.insertNode(1)
l.insertNode(0)
l.insertNode(5)
l.insertNode(3)
l.traverse()

print()

l.removeDuplicateNodeFromUnsortedList()
print("after removing duplicates list is")
l.traverse()

'''
3->5->0->1->2->3->0->4->2->5->

after removing duplicates list is
3->5->0->1->2->4->
'''