# calss TreeNode:
# def __init__(self. x)
#     self.val = x
#     self.left = None
#     self.right = None

# class Solution:
#     def PrintFromTopBottom(self, root):
#         outList = []
#         queue = [root]
#         while queue != [] and root :
#             outList.append(queue[0].val)
#             if queue[0].left != None:
#                 queue.append(queue[0].left)
#             if queue[0].right != None:
#                 queue.append(queue[0].right)
#              queue.pop(0)
#      return outList
#

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]
        outList = []
        while queue:
            res = []
            nextQueue = []
            for point in queue:
                res.append(point.val)
                if point.left:
                    nextQueue.append(point.left)
                if point.right:
                    nextQueue.append(point.right)
            outList.append(res)
            queue = nextQueue
        return outList

#当然，完全用队列来做也是没有问题的，不过，其关键在于确认每一层的分割点，因此可以用一个标志位来记录这个分割点的位置

def Print(self, pRoot):
    if not pRoot:
        return []
    queue = [pRoot]
    outList = []
    while queue:
        res = []
        i = 0
        numberFlag = len(queue)
        while i < numberFlag:
            point = queue.pop(0)
            res.append(point.val)
            if point.left:
                queue.append(point.left)
            if point.right:
                queue.append(point.right)
            i += 1
        outList.append(res)
    return outList

