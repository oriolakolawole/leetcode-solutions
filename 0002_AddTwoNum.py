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

