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

    def traverse(self):
        print("original list is")
        temp = self.head
        output = []
        while(temp):
            # get he plane list
            output.append(temp.data)
            print(temp.data, end="->")
            temp = temp.next
        print()
        return output


    def sortTheUnsortedList(self):

        output_list = self.traverse()
        # sort the list
        sorted_list = sorted(output_list)
        #print(sorted_list)

        new_node = Node(-1)
        temp_node = new_node
        for i in sorted_list:
            temp_node.next = Node(i)
            temp_node = temp_node.next

        new_node = new_node.next
        print("after sorting the list becomes")
        while(new_node):
            print(new_node.data, end="->")
            new_node = new_node.next

l = LinkedList()

l.insertAtHead(1)
l.insertAtHead(0)
l.insertAtHead(20)
l.insertAtHead(4)
l.insertAtHead(90)
l.insertAtHead(2)
l.sortTheUnsortedList()