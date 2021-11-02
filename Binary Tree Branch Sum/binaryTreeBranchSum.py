# here we find sum of all the values from root node to each leaf nodes individually
class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
# recursive logic
# O(N) time | O(N) space
def branchSums(root):
    sums=[]
    calculateBranchSums(root,0,sums)
    return sums


def calculateBranchSums(node,runningSum,sums):
    if node is None:
        return
    newRunningSum=runningSum+node.value
    if node.left is None and node.right is None:
        return

    calculateBranchSums(node.left,newRunningSum,sums)
    calculateBranchSums(node.right,newRunningSum,sums)


