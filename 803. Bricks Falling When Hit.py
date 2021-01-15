'''
You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bricks-falling-when-hit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import numpy as np
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        m = len(grid)
        n = len(grid[0])

        stables = np.zeros(shape=(m,n),dtype=int)
        # set top bricks stable
        for j in range(n):
            if grid[0][j] == 1: stables[0][j] = 1


        num1 = None
        ret = []
        # for each hit
        for [row,col] in hits:
            # 1. compute number of stable bricks
            if num1 is None:
                num1 =  sum(stables[0])
                for i in range(0,m):
                    for j in range(n):
                        if grid[i][j] + stables[i][j] == 2:
                            # spreading stable
                            # left
                            if j != 0:
                                if grid[i][j-1] and not stables[i][j-1]:
                                    stables[i][j-1] = 1
                                    num1 += 1

                            # right
                            if j != n-1:
                                if grid[i][j+1] and not stables[i][j+1]:
                                    stables[i][j+1] = 1
                                    num1 += 1

                            # bottom
                            if i != m-1:
                                if grid[i+1][j] and not stables[i+1][j]:
                                    stables[i+1][j] = 1
                                    num1 += 1

            # 2. remove the brick
            if grid[row][col] == 0: ret.append(0)
            elif stables[row][col] == 0:
                grid[row][col] = 0
                ret.append(0)
            else:
                num2 = 1
                grid[row][col] = 0
                stables = np.zeros(shape=(m, n), dtype=int)
                # set top bricks stable
                for j in range(n):
                    if grid[0][j] == 1:
                        stables[0][j] = 1
                        num2 += 1


                for i in range(0,m):
                    for j in range(n):
                        if grid[i][j] + stables[i][j] == 2:
                            # spreading stable
                            # left
                            if j != 0:
                                if grid[i][j-1] and not stables[i][j-1]:
                                    stables[i][j-1] = 1
                                    num2 += 1

                            # right
                            if j != n-1:
                                if grid[i][j+1] and not stables[i][j+1]:
                                    stables[i][j+1] = 1
                                    num2 += 1

                            # bottom
                            if i != m-1:
                                if grid[i+1][j] and not stables[i+1][j]:
                                    stables[i+1][j] = 1
                                    num2 += 1
                ret.append(num1-num2)

                # 3. update num1
                num1 = num2

        return ret




print(Solution().hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]])==[2])




