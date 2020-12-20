'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a,
that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

9 1 4 5 6  1  2 3 7
'''
from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        sum, res = 0, 0
        # exist 记录该元素是否出现过
        exist = []
        # 每次开始计算的左指针
        left = 0
        for i in range(length):
            # 如果元素第一次出现，计入exist，计算sum
            if nums[i] not in exist:
                sum += nums[i]
                exist.append(nums[i])
                res = max(res, sum)
                #print(res)
            # 如果该元素已出现过
            else:
                # 不断右移左指针，找到重复元素，舍弃掉左边部分
                while nums[left] != nums[i]:
                    sum -= nums[left]
                    exist.remove(nums[left])
                    left += 1
                # 找到重复元素后，左指针也要右移一位，重新开始计算
                left += 1
        return res


#print(Solution().maximumUniqueSubarray([9,1,4,5,6,1,2,3,7]))