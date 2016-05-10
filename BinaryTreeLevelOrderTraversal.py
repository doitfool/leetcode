"""
	@Project: leetcode
	@file: BinaryTreeLevelOrderTraversal.py
	@author: AC
	@time: 2016/5/10
	@Description: Given a binary tree, return the level order traversal of its nodes' values.
	(ie, from left to right, level by level).
    For example:
    Given binary tree {3,9,20,#,#,15,7},
        3
       / \
      9  20
        /  \
       15   7
    return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        result = [[root.val]]
        while queue:
            pop_nodes, pop_nums = [], []
            for i in xrange(len(queue)):
                pop_nodes.append(queue.pop(0))
            for i in xrange(len(pop_nodes)):
                if pop_nodes[i].left is not None:
                    queue.append(pop_nodes[i].left)
                    pop_nums.append(pop_nodes[i].left.val)
                if pop_nodes[i].right is not None:
                    queue.append(pop_nodes[i].right)
                    pop_nums.append(pop_nodes[i].right.val)
            result.append(pop_nums)
        result = result[:-1]
        return result