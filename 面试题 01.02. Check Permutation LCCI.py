'''
Given two strings,write a method to decide if one is a permutation of the other.



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if s1  == s2: return True

        l1 = list(s1)
        l2 = list(s2)
        for i in range(len(s1)):
            c1 = l1[i]
            if c1 not in l2:return False

            l1[i]  = None
            l2[l2.index(c1)] = None

        return True


