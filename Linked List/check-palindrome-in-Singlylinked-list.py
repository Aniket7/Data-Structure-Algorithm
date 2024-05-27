# Palindrome exist if you read the linked list in same order from Start and End.

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

    # print the linked list and return it's length
    def traverse(self):
        temp = self.head
        c = 0
        if temp is None:
            print("Linked List is empty")
            return
        else:
            while (temp):
                print(temp.data, end="->")
                temp = temp.next
                c+=1
            print()
        # return the length of linked list
        return c

    # this approach has:- Time_complexity: O(n), Space_complexity: O(n) where n is number of nodes.
    def checkPalindrome(self):
        if self.head is None or self.head.next is None:
            return True
        temp = self.head
        list_array = []
        while(temp):
            list_array.append(temp.data)
            temp = temp.next

        n = len(list_array)
        first = 0
        last = n-1

        while(first<=last):
            if(list_array[first]==list_array[last]):
                #print("Palindrome exist in Linked list ")
                return True
            first+=1
            last -=1

        return False

    # it reverse the linked list
    def reverse(self, root):
        #print("in rev")
        if root is None or root.next is None:
            return root
        prev = None
        curr = root
        while(curr):
            forward = curr.next
            curr.next = prev
            prev =curr
            curr = forward

        return prev

    # compare 2 linked list
    def compareList(self, list1, list2):
        tmp = list1
        reverse_list = list2
        while (tmp != None and reverse_list != None):
            if (tmp.data == reverse_list.data):
                tmp = tmp.next
                reverse_list = reverse_list.next
            else:
                return False
        if (tmp==None and reverse_list==None):
            return True

        return True

    # this approach has:- Time_complexity: O(n), Space_complexity: O(1) where n is number of nodes
    def checkPalindromeUsingOptimalSolution(self):
        if self.head is None or self.head.next is None:
            return True
        # get the length of list
        length = self.traverse()
        middle = length // 2
        middle_node = None
        #print("middle is",middle)
        temp = self.head
        for _ in range(middle-1):
            temp = temp.next

        middle_node = temp
        #print("middle node is", temp.data)

        reverse_list = self.reverse(temp.next)
        tmp = self.head
        compare = self.compareList(tmp, reverse_list)
        original_half = self.reverse(reverse_list)
        if(middle_node!=None):
            middle_node.next = original_half
        return compare


l = LinkedList()

l.insertAtHead(1)
l.insertAtHead(2)
l.insertAtHead(1)
l.insertAtHead(3)
l.insertAtHead(1)
l.insertAtHead(2)
l.insertAtHead(1)


l.traverse()
'''
if(l.checkPalindrome()):
    print("Palindrome exist in Linked list ")
else:
    print("Palindrome Does not exist in Linked list ")
'''

if(l.checkPalindromeUsingOptimalSolution()):
    print("Palindrome exist in Linked list ")
else:
    print("Palindrome Does not exist in Linked list ")

print("original List is")
l.traverse()

#OUTPUT
'''
1->2->1->3->1->2->1->
1->2->1->3->1->2->1->
Palindrome exist in Linked list 
original List is
1->2->1->3->1->2->1->
'''


#OUTPUT
'''
4->1->2->1->3->1->2->5->
4->1->2->1->3->1->2->5->
Palindrome Does not exist in Linked list 
original is
4->1->2->1->3->1->2->5->
'''

#OUTPUT
'''
1->
Palindrome exist in Linked list 
original List is
1->
'''