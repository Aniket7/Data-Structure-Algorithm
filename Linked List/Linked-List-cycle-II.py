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

    # detect cycle using Floyd's Cycle detection algo.
    def detectCycle(self):
        slow = fast = self.head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if (slow==fast):
                return True
        return False

    # detect start node of the cycle using Floyd's Cycle detection algo.
    def detectStartNodeOfCycle(self):
        slow = fast = self.head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                # initialize temp variable which starts from head
                start = self.head
                # run the loop
                while(start!=slow):
                    start = start.next
                    slow=slow.next
                print("Cycle starts from node ",start.data)
                return start
        return None

    # remove cycle in a linked list
    def removeCycle(self):

        # get the starting node of the cycle
        start_node = self.detectStartNodeOfCycle()
        temp = start_node
        while(temp.next!=start_node):
            temp = temp.next
        temp.next = None
        print("cycle removed")
        return


l = LinkedList()

l.insertNode(5)
l.insertNode(4)
l.insertNode(3)
l.insertNode(2)
l.insertNode(1)
l.insertNode(0)
l.traverse()
#print(l.head.data)

# it forms cycle
l.head.next.next.next.next.next.next = l.head.next

if (l.detectCycle()):
    print("Cycle present")
    # detect start node of cycle
    l.detectStartNodeOfCycle()
    # remove the cycle
    l.removeCycle()
else:
    print("cycle not present")

print("#"*50)
print("run the function again after removing cycle")
if(l.detectCycle()):
    print("cycle present")
else:
    print("cycle not present")

#OUTPUT
'''
0->1->2->3->4->5->
Cycle present
Cycle starts from node  1
Cycle starts from node  1
cycle removed
##################################################
run the function again after removing cycle
cycle not present
'''