'''You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.

'''
from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        minVals = []
        limit = len(nums)+1

        for i in range(len(nums)):
            if nums[i] == 0: continue

            left = right = i
            dp = [-1]*(k+1)
            dp[0]=dp[1] =0
            copy = list(nums)

            # 2->k
            for tmp in range(2,k+1):
                # min right dist
                min_right_dist = limit
                for j in range(right + 1, len(nums)):
                    if copy[j] == 1:
                        min_right_dist = j - right - 1
                        break

                # min left dist
                min_left_dist = limit
                for j in range(left-1,-1,-1):
                    if  copy[j] == 1:
                        min_left_dist = left-j-1
                        break

                if min_right_dist==limit and min_left_dist==limit:
                    break
                dp[tmp] = dp[tmp-1] + min(min_left_dist,min_right_dist)
                if min_left_dist<=min_right_dist:
                    left -= 1
                    copy.insert(left,copy.pop(left-min_left_dist))
                else:
                    right += 1
                    copy.insert(right,copy.pop(right+min_right_dist))

            if dp[k] != -1: minVals.append(dp[k])
            print(i,dp[k])

        return min(minVals) if len(minVals)>0 else 0


print(Solution().minMoves([1,0,0,1,0,1,1,1,0,1,1],7 ))



