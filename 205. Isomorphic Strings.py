'''Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False
        dic = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            print(c1, c2)
            if c1 not in dic.keys():
                dic[c1] = c2
            else:
                if c0 := dic[c1] != c2: return False
        print(dic)

        return True






