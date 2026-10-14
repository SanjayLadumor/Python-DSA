# QUESTION :

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
            if head is None or head.next is None:
                return head

            temp = head

            while temp is not None and temp.next is not None:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next

            return head