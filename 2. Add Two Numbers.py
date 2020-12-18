'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def list2int(l:ListNode):
            sum = 0
            if l is None: return 0

            sum += l.val

            temp = 10

            while l.next is not None:
                sum += l.next.val * temp
                l = l.next
                temp *= 10

            return sum

        def int2list(a:int):
            s = str(a)
            length = len(s)

            l = ListNode(int(s[-1]),None)
            ret = l

            for i in range(1,length):
                c = int( s[length-1-i])
                l.next = ListNode(c)
                l = l.next

            return ret

        return int2list( list2int(l1) + list2int(l2))
