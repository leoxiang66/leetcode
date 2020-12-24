'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/assign-cookies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #* sort g and s
        g.sort()
        s.sort()

        #* two pointers
        curr_child = 0
        curr_cookie=0

        #* other data
        ret = 0
        len_g = len(g)
        len_s = len(s)

        while curr_child < len_g and curr_cookie < len_s:
            if g[curr_child] <= s[curr_cookie]:
                ret += 1
                curr_child += 1
                curr_cookie += 1
            else:
                curr_cookie += 1
          
        return ret
                