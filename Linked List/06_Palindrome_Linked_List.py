# QUESTION :

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        ans = []

        temp = head

        while temp is not None:
            ans.append(temp.val)
            temp = temp.next

        rev_ans = ans[::-1]

        if rev_ans == ans:
            return True
        return False