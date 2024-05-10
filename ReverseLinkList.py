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

    def iterativeReverse(self, head):
        prev = None
        curr = head
        #print(head.data)
        # check for empty list or single node; return the list
        if curr is None or curr.next is None:
            #print(1)
            return curr
        # run the loop
        #print(2)
        while(curr):
            #print(3)
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        #print(prev.data)
        self.head = prev
        return prev

    def recursiveReverse(self, head):

        if head is None or head.next is None:
            return head;

        reverse_head = self.recursiveReverse(head.next)
        head.next.next = head
        head.next = None
        return reverse_head

l1 = LinkList()
l1.insertAtHead(2)
l1.insertAtTail(7)
l1.insertAtHead(1)
l1.insertAtTail(3)
l1.insertAtPos(99,2)
l1.insertAtPos(100,1)
head = l1.insertAtPos(222222, 9)
l1.traverse()
print("calling iterative reverse")
prev = l1.iterativeReverse(head)
temp = prev
while (prev):
    print(prev.data, end="->")
    prev = prev.next
print()
print("calling recursive reverse")
rec_head = l1.recursiveReverse(temp)
while(rec_head):
    print(rec_head.data, end="->")
    rec_head = rec_head.next





