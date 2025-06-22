"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        headNode = ListNode() #headNode is the dummy i can use to access my list
        current = headNode #current will keep on updating as more nodes are add to the list
        carry = 0
        
        #while there still nodes or carry isn't 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumVal = val1 + val2 + carry
            carry = sumVal // 10
            
            #current => Head -> sumVal1 -> sumVal2 -> ...
            current.next = ListNode(sumVal % 10)
            current = current.next
            
            #move to next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # returns only => sumVal1 -> sumVal2 -> ...
        return headNode.next
            

"""
TO TEST 
"""        
# Helper to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper to convert linked list to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
l1 = list_to_linkedlist([2, 4, 3])  # represents the number 342
l2 = list_to_linkedlist([5, 6, 4])  # represents the number 465

solution = Solution()
result_node = solution.addTwoNumbers(l1, l2)
result_list = linkedlist_to_list(result_node)

print(result_list)  # Expected output: [7, 0, 8] which represents the number 807
