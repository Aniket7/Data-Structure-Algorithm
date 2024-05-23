class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return new_node

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def traverse(self):

        temp = self.head
        while (temp):
            print(temp.data, end="<->")
            temp = temp.next

        # to print it in reverse order
        '''
        while(temp.next!=None):
            temp = temp.next
        
        while(temp):
            print(temp.data, end="<->")
            temp = temp.prev
        '''

        print()

    
    def removeDuplicateFromSortedList(self):

        if self.head is None or self.head.next is None:
            return self.head

        temp = self.head
        while(temp and temp.next):
            if (temp.data == temp.next.data):
                temp.next = temp.next.next
                temp.next.next.prev = temp
            else:
                temp = temp.next


l1 = LinkedList()

l1.addNode(5)
l1.addNode(4)
l1.addNode(3)
l1.addNode(3)
l1.addNode(2)
l1.addNode(1)
l1.addNode(1)
l1.addNode(0)
l1.addNode(0)
print("original list")
l1.traverse()
print("after removing duplicates")
l1.removeDuplicateFromSortedList()
l1.traverse()

# OUTPUT
'''
original list
0<->0<->1<->1<->2<->3<->3<->4<->5<->
after removing duplicates
0<->1<->2<->3<->4<->5<->
'''

