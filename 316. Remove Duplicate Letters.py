'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

答案解析: https://leetcode-cn.com/problems/remove-duplicate-letters/solution/qu-chu-zhong-fu-zi-mu-by-leetcode-soluti-vuso/
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        stack = []
        for c in s:
            if c in stack:
                freq[ord(c)-ord('a')] -= 1
                continue


            freq[ord(c)-ord('a')] -= 1
            while stack and stack[-1] > c and freq[ord(stack[-1])-ord('a')] > 0:
                stack.pop()
            stack.append(c)
        return ''.join(stack)






