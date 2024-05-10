
# defines node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define link list structure
class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert node at beginning
    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return self.head

    # insert node at last
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

    # insert node at particular position
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

    def compareList(self, l2):
        # assign the head of both the list
        a = self.head
        b = l2.head
        # if both list are empty then return
        if (l1 is None or l2 is None):
            return "list are empty"
        # run the loop until the linkedlist
        while(a != None and b!=None):
            # check the data of both the node's
            if (a.data==b.data):
                # traverse both the list
                a = a.next
                b = b.next
                return True
            else:
                # if data does not match then return
                return False


l1 = LinkList()
l2 = LinkList()
l1.insertAtHead(2)
l1.insertAtTail(7)
l1.insertAtHead(1)
l1.insertAtPos(9,1)
l2.insertAtHead(2)
l2.insertAtTail(7)
l2.insertAtHead(1)
l2.insertAtPos(9,1)
# Output for this is Same
if l1.compareList(l2) == True:
    print("Same")
else:
    print("Not Same")
    
'''
l1 = LinkList()
l2 = LinkList()
l1.insertAtHead(2)
l1.insertAtTail(7)
l1.insertAtHead(100)
l1.insertAtPos(9,1)
l2.insertAtHead(2)
l2.insertAtTail(8)
l2.insertAtHead(1)
l2.insertAtPos(9,3)

# Output for this is "Not Same"
if l1.compareList(l2) == True:
    print("Same")
else:
    print("Not Same")
'''





