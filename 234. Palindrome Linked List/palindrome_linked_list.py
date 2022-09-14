# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        arr = [head.val]
        node = head.next
        while node:
            arr.append(node.val)
            node = node.next
        return self.compare_palindrome(arr)

    def compare_palindrome(self, head):
        r_head = head[: int(len(head) / 2) - 1 : -1]
        for i in range(len(r_head)):
            if head[i] != r_head[i]:
                return False
        return True
