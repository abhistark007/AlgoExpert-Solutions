

# recursive method
# avg time= O(logN)
# worst time= O(N)
def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    if tree is None: #it means that we are at leaf node
        return closest
    if abs(target-closest)> abs(target-tree.value):
        closest=tree.value
    if target<tree.value:
        return findClosestValueInBstHelper(tree.left,target,closest)
    elif target>tree.value:
        return findClosestValueInBstHelper(tree.right,target,closest)
    else:
        return closest


# Iterative method
# avg time= O(logN)
# worst time= O(N)
def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    currentNode=tree
    while currentNode is not None:

        if abs(target-closest)> abs(target-currentNode.value):
            closest=currentNode.value
        if target<currentNode.value:
            currentNode=currentNode.left
        elif target>currentNode.value:
            currentNode=currentNode.right
        else:
            break
    return closest


