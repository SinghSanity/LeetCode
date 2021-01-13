# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Helper method to turn a linked list into a number
def listToNumber(l: ListNode):
    num = ""
    curr = l
    while(True):
        num = str(curr.val) + num
        if (curr.next is None):
            break
        curr = curr.next
    return num

# Helper method to turn a number into a linked list
def numberToList(num) -> ListNode:
    l = ListNode(int(num[0]), None)
    for i in range(1, len(num)):
        curr = ListNode(int(num[i]), l)
        l = curr
    return l

class Solution:    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = int(listToNumber(l1))
        num2 = int(listToNumber(l2))
        num = num1+num2
        
        return numberToList(str(num))
