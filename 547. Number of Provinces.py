'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import numpy as np
class Solution:
    class Solution:
        def findCircleNum(self, isConnected: List[List[int]]) -> int:
            def find(index: int) -> int:
                if parent[index] != index:
                    parent[index] = find(parent[index])
                return parent[index]

            def union(index1: int, index2: int):
                parent[find(index1)] = find(index2)

            provinces = len(isConnected)
            parent = list(range(provinces))

            for i in range(provinces):
                for j in range(i + 1, provinces):
                    if isConnected[i][j] == 1:
                        union(i, j)

            circles = sum(parent[i] == i for i in range(provinces))
            return circles
        
'''
    作者：LeetCode - Solution
    链接：https: // leetcode - cn.com / problems / number - of - provinces / solution / sheng - fen - shu - liang - by - leetcode - solution - eyk0 /
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''


