"""
store values in an array
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array[::] == array[::-1]

"""
思路
两个指针都从头出发，快指针每次两步，慢指针每次一步，这样快指针的下一个或下下个为空时，慢指针就在链表正中间那个节点了
（如果链表有偶数个节点则在靠近头那侧的）。然后我们从慢指针的下一个开始，把后面的链表都反转（Reverse Linked List），
然后我们再从头和从尾同时向中间前进，就可以判断该链表是不是回文了。
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True