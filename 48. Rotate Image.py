'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
         a,b -> b,len-1-a
        """
        length = len(matrix)


        def rec(depth,matrix):
            if depth  == 0:
                target_col = length-1-depth
                copy_ = matrix[depth].copy()
                for j in  range(length):
                    matrix[j][target_col]  = copy_[j]
            else:
                copy_ = matrix[depth].copy()
                rec(depth-1,matrix)

                target_col = length - 1 - depth
                for j in range(length):
                    matrix[j][target_col] = copy_[j]

        rec(length-1,matrix)




