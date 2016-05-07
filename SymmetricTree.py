# coding:utf-8
"""
	@Project: leetcode
	@file: SymmetricTree.py
	@author: AC
	@time: 2016/5/8 0:09
	@Description: Given a binary tree, check whether it is a mirror of itself
	(ie, symmetric around its center).
    For example, this binary tree is symmetric:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following is not:
        1
       / \
      2   2
       \   \
       3    3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue = [root]
        flag = True
        while queue:
            pop_nodes, pop_nums = [], []
            for i in xrange(len(queue)):
                pop_nodes.append(queue.pop())
            for i in xrange(len(pop_nodes)):
                if pop_nodes[i].left is not None:
                    queue.append(pop_nodes[i].left)
                    pop_nums.append(pop_nodes[i].left.val)
                else:
                    pop_nums.append(0)
                if pop_nodes[i].right is not None:
                    queue.append(pop_nodes[i].right)
                    pop_nums.append(pop_nodes[i].right.val)
                else:
                    pop_nums.append(0)
            for i in xrange(len(pop_nums)/2):
                if pop_nums[i] != pop_nums[len(pop_nums)-1-i]:
                    flag = False
                    break
            if not flag:
                break
        return flag



s = Solution()
nodes = []
nodes.append(TreeNode(1))
nodes.append(TreeNode(2))
nodes.append(TreeNode(2))
nodes.append(TreeNode(3))
nodes.append(TreeNode(4))
nodes.append(TreeNode(4))
nodes.append(TreeNode(3))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
print s.isSymmetric(nodes[0])

nodes = []
nodes.append(TreeNode(1))
nodes.append(TreeNode(2))
nodes.append(TreeNode(2))
nodes.append(TreeNode(3))
nodes.append(TreeNode(3))

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].right = nodes[3]
nodes[2].left = nodes[4]
print s.isSymmetric(nodes[0])
