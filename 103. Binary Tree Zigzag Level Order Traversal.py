'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。
即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
'''
#Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        ret = [[root]]

        def rec(last_level):
            if  len(last_level)==0: return

            this_level = []
            for i in  last_level:
                if i is None: continue
                if i.left is not None :
                    this_level.append(i.left)
                if i.right is not None:
                    this_level.append(i.right)


            if this_level is not None and len(this_level)>0: ret.append(this_level)
            rec(this_level)

        # run the algorithm
        rec([root])


        f = lambda list: [i.val for  i in list if i is not None]


        temp= list(map(f,ret))
        for i in range(1,len(temp),2):
            temp[i] =list(reversed(temp[i]))

        return temp

