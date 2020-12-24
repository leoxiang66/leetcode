'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        def rec_impl(i,j,costACC):
            # check  if it's already finished

            # if it can already be finished from  i, then  choose min of cost[i],cost[j]
            if i + 2  >=  length:
                return  costACC + min(cost[i],cost[j])
            else:
                #target = None

                # if  cost[j] <  cost[j+1], choose  cost[j]
                if cost[j] < cost[j+1]: target = j

                # else choose min
                else: target = i if cost[i] < cost[j] else j

                #print(target)

                # if target + 2 is out of bound => finished
                if target + 2 >= length: return costACC + cost[target]

                # otherwise go to next call
                return rec_impl(target+1,target+2,costACC+cost[target])


        return rec_impl(0,1,0)

#print(Solution().minCostClimbingStairs([0,0,0,0]))
