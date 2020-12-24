'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        ret = [1] * length

        finished = True

        while True:
            finished = True

            for i in range(length-1):
                curr = ratings[i]
                right = ratings[i+1]

                if curr < right and ret[i] >= ret[i+1]: ret[i+1] =ret[i]+1
                elif curr > right and ret[i] <= ret[i+1]: ret[i] = ret[i+1]+1
            
            for i in range(length-1,0,-1):
                curr = ratings[i]
                left = ratings [i-1]

                if left > curr and ret[i-1] <= ret[i]: ret[i-1] = ret[i] + 1
                if left < curr and ret[i] <= ret[i-1]: ret[i] = ret[i-1] + 1

            #* check if ret meets the requirements
            for i in range(length-1):
                if ratings[i] < ratings[i+1] and ret[i] >= ret[i+1]:
                    finished = False
                    break
                if ratings[i] > ratings[i+1] and ret[i] <= ret[i+1]:
                    finished = False
                    break
            
            if finished: break
            

        return sum(ret)


'''
#* recommended idea to solve the problem
https://leetcode-cn.com/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/
'''