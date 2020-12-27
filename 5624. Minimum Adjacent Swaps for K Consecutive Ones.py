'''You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.

'''

from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        one_ind = []
        length = len(nums)
        for i in range(length):
            if nums[i] == 1:
                one_ind.append(i)


        if k<=1: return 0
        # sliding window
        # left, right, mid
        # mid用来确定应该向做移出窗口的0和应该向右移出窗口的0
        # 不断寻找下一个这样的窗口: 窗口里面恰有k个1，并记录每个窗口对应的move数， 最后返回最小的move数


        # 移动left，right至第一个1处
        right = left = one_ind[0]
        mid = k // 2   # 第$mid+1$个1为中间的1
        l_ind = 0  #! 记录left是第几个1

        count = 1   #计数当前窗口1的数量
        ret = float("inf")
        while right < length-1:

            right += 1
            if nums[right] == 0: continue

            count +=1
            # 这里意味着我们找到了下一个1，检查窗口是否已有k个1


            # 若找到了k个1，则记录当前窗口需要的move数
            if count == k:
                # 确定mid_ind:
                mid_ind = one_ind[l_ind+mid]

                # mid及mid左边的0向左移除窗口，mid右边的0向右移除窗口
                # 算法： 从left到right遍历， 记录每个0当前的index1和移除窗口后的index2，则这个0的交换次数 = |index1-index2|
                # indices := [(index1,index2)...]: a list of two indices of each 0
                # temp1 := left,left+1,left+2... temp2 = right,right-1,right-2
                temp1 = left
                temp2 = right
                indices=[]

                for i in range(left,mid_ind):
                    if nums[i] ==0:
                        indices.append((i,temp1))
                        temp1 += 1
                for i in range(right,mid_ind,-1):
                    if nums[i] == 0:
                        indices.append((i,temp2))
                        temp2 -= 1
                # 求move数
                move_num = sum([abs(a-b) for (a,b) in indices])
                ret = min(ret,move_num)

                #! 此时向右移动right已无意义，应将left右移至下一个1处
                l_ind +=1
                left = one_ind[l_ind]

                count -= 1

            # 若还不够k个1，则继续寻找

        return ret

