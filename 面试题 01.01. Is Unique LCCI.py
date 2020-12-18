'''
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isUnique(self, s: str) -> bool:
        if s == '':  return  True

        for i in range (len(s)):
            if i == len(s) -1: return True
            if s[i] in s[i+1:]: return False
