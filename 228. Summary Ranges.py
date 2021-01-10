'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left =  right = 0
        length = len(nums)
        ret = []
        while left <= right and right < length:
            right += 1
            if right >= length:
                if nums[left] != nums[right-1]: 
                    ret .append(f"{nums[left]}->{nums[right-1]}")
                else:
                    ret.append(f"{nums[left]}")
                break
            else:
                if nums[right] != nums[right-1] +1:
                    if nums[left] != nums[right-1]: 
                        ret.append(f"{nums[left]}->{nums[right-1]}")
                    else:
                        ret.append(f"{nums[left]}")
                    left = right
        return ret

print(Solution().summaryRanges([0,1,2,4,5,7]))