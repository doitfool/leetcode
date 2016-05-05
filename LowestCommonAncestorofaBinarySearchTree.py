# coding: utf-8
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchPath(self, root, t, path=[]):
        if root is None:
            return path
        else:
            path.append(root.val)
            if root.val == t:
                return path
            elif t > root.val:
                path = self.searchPath(root.right, t, path)
            elif t < root.val:
                path = self.searchPath(root.left, t, path)
            return path


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p1 = self.searchPath(root, p.val, [])
        p2 = self.searchPath(root, q.val, [])
        if len(p1) > len(p2):
            p1, p2 = p2, p1
        result = None
        for i in xrange(len(p1)-1, -1, -1):
            if p1[i] in p2:
                result = p1[i]
                break
        return result

if __name__ == '__main__':
    s = Solution()
    nodes = []
    for i in range(10):
        nodes.append(TreeNode(i))
    nodes[6].left = nodes[2]
    nodes[6].right = nodes[8]
    nodes[2].left = nodes[0]
    nodes[2].right = nodes[4]
    nodes[8].left = nodes[7]
    nodes[8].right = nodes[9]
    nodes[4].left = nodes[3]
    nodes[4].right = nodes[5]
    root = nodes[6]
    print s.lowestCommonAncestor(root, nodes[2], nodes[8])
