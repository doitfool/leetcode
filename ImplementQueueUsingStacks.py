"""
	@Project: leetcode
	@file: ImplementQueueUsingStacks.py
	@author: AC
	@time: 2016/5/7 23:42
	@Description: Implement the following operations of a queue using stacks.
    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.
    Notes:
    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top, self.tail = 0, 0
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        self.tail += 1

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop(self.top)
        self.tail -= 1

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[self.top]


    def empty(self):
        """
        :rtype: bool
        """
        if self.tail == self.top:
            return True
        else:
            return False

q = Queue()
print q.empty()
q.push(1)
q.push(2)
print q.peek()
q.pop()
print q.peek()