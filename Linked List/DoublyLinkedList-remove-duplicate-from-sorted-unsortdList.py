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

    # it removes noew drom sorted list
    def removeDuplicateFromSortedList(self):
        # check for empty list or single node
        if self.head is None or self.head.next is None:
            return self.head

        temp = self.head
        # iterate over list
        while(temp.next!=None):
            # check for the duplicate node
            if (temp.data == temp.next.data):
                # remve duplicate node and change next pointer
                temp.next = temp.next.next
                # change the prev pointer
                if(temp.next!=None):
                    temp.next.next.prev = temp
            # increment the pointer
            else:
                temp = temp.next


    def removeDuplicateNodeFromUnsortedList(self):
        # check for empty list or single node
        if self.head is None or self.head.next is None:
            return self.head

        temp = self.head
        visited = set()

        # iterate over list until it is empty
        while(temp.next!=None):
            visited.add(temp.data)
            # check for the duplicate node
            if temp.next.data in visited:
                temp.next = temp.next.next
                # change the prev pointer
                if (temp.next!=None):
                    temp.next.prev = temp
            else:
                visited.add(temp.next.data)
                temp = temp.next



l1 = LinkedList()

'''
l1.addNode(5)
l1.addNode(5)
l1.addNode(4)
l1.addNode(3)
l1.addNode(3)
l1.addNode(2)
l1.addNode(1)
l1.addNode(1)
l1.addNode(0)
l1.addNode(0)
print("original sorted list")
l1.traverse()
print("after removing duplicates")
l1.removeDuplicateFromSortedList()
l1.traverse()

# OUTPUT
original sorted list
0<->0<->1<->1<->2<->3<->3<->4<->5<->
after removing duplicates
0<->1<->2<->3<->4<->5<->
'''

l1.addNode(5)
l1.addNode(5)
l1.addNode(4)
l1.addNode(3)
l1.addNode(4)
l1.addNode(2)
l1.addNode(0)
l1.addNode(1)
l1.addNode(0)
l1.addNode(2)
l1.addNode(5)
print("original Unsorted list")
l1.traverse()
print("after removing duplicate from unsorted list")
l1.removeDuplicateNodeFromUnsortedList()
l1.traverse()

#OUTPUT
'''
original Unsorted list
5<->2<->0<->1<->0<->2<->4<->3<->4<->5<->5<->
after removing duplicate from unsorted list
5<->2<->0<->1<->4<->3<->
'''