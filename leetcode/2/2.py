# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        a = []
        b = []
        while(l1.val != 0 and l1.next != None):
            print("here")
            a.add(l1.val)
            
            
            
        print("a")
        print(a)
        print("end")
        # a = l1.val
        # print(a)
        # b = l1.next.val
        # print(b)
        # c = l1.next.next.val
        # print(c)
        # abc = (c * 100) + (b * 10) + a
        # print(abc)

