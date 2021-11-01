class BST:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    # avg time= O(logN) | O(1) space
    # worst case time= O(N) | O(1) space
    def insert(self,value):
        currentNode=self
        while True:
            if value<currentNode.value:
                if currentNode.left is None:
                    currentNode.left=BST(value)
                    break
                else:
                    currentNode=currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right=BST(value)
                    break
                else:
                    currentNode=currentNode.right
    # avg time= O(logN) | O(1) space
    # worst case time= O(N) | O(1) space
    def constains(self,value):
        currentNode=self
        while currentNode is not None:
            if value<currentNode.value:
                currentNode=currentNode.left
            elif value>currentNode.value:
                currentNode=currentNode.right
            else:
                return True
        return False

    def remove(self,value,parentNode=None):
        currentNode=self
        while currentNode is not None:
            if value<currentNode.value:
                parentNode=currentNode
                currentNode=currentNode.left
            elif value>currentNode.value:
                parentNode=currentNode
                currentNode=currentNode.right
            else:
                #Case 1 when the node has both left and right children
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value=currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value,currentNode)
                # when we are removing root node
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value=currentNode.left.value
                        currentNode.right=currentNode.left.right
                        currentNode.left=currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value=currentNode.right.value
                        currentNode.right=currentNode.right.right
                        currentNode.left=currentNode.right.left
                # when we are removing node with only 1 child
                elif parentNode.left==currentNode:
                    parentNode.left=currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right==currentNode:
                    parentNode.right=currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self
    
    def getMinValue(self):
        currentNode=self
        while currentNode.left is not None:
            currentNode=currentNode.left
        return currentNode.value



    
