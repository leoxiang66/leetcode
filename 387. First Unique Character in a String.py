class Solution:
    def firstUniqChar(self, string111: str) -> int:
        def rec(s1):
            #print(s1)
            if s1 is None or s1 =='': return None
            if len(s1) == 1: return s1

            peek = s1[0]
            rest = s1[1:]

            if peek not in rest: return peek
            return rec(rest.replace(peek,''))

        ret_char = rec(string111)

        if ret_char: return string111.find(ret_char)
        return -1

print(Solution().firstUniqChar("loveleetcode"))
