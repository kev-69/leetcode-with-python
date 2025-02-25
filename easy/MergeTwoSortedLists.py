from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the logic
        dummy = ListNode()
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If there are any remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list, which starts from dummy.next
        return dummy.next


# Creating sample input lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merging the lists
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Printing the merged list
current = merged_head
while current:
    print(current.val, end=" -> ")
    current = current.next