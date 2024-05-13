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

    # remove node from the tail using 2 pointer approach
    def removeFromLast(self, pos):
        slow = self.head
        fast = self.head
        if fast is None or fast.next is None:
            temp = None
            return
        else:
            # move fast pointer to the nth position
            for _ in range(pos):
                fast = fast.next
            print(fast.data)
            if not fast:
                return self.head.next
            # increment both the pointers and
            while(fast.next):
                slow = slow.next
                fast = fast.next
            # remove nth node here from tail
            slow.next = slow.next.next
        return self.head




l = LinkedList()

l.insertAtHead(1)
l.insertAtPos(2,2)
l.insertAtTail(3)
l.insertAtPos(4,8)
l.insertAtHead(0)
l.traverse()
print()
l.removeFromLast(4)
l.traverse()
print()
l.removeFromLast(2)
l.traverse()
print()


'''
Below is the output
0->1->2->3->4->

0->2->3->4->

0->2->4->
'''
