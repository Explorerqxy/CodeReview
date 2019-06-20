# calss TreeNode:
# def __init__(self. x)
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def PrintFromTopBottom(self, root):
        outList = []
        queue = [root]
        while queue != [] and root :
            outList.append(queue[0].val)
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
             queue.pop(0)
     return outList
    
