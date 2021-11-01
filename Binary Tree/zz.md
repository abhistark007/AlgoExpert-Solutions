# Binary Tree
=============


Binary Tree is a non linear and hierarchical organized data structure.
* It has only one root node
* Except for root node all the node have parents
* It can have as many children as you want
* On any subtree, the left nodes are less than the root node

## Creating Root
```python
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data is None:
            self.data=data
        else:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
                
root=Node(10)
root.insert(1)
root.insert(2)
root.insert(7)
root.insert(8)

```

## Binary Tree Inorder Traversal
* we traverse from left to root to right
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# inorder: left, root, right
'''           1
           /  |  \
         /         \
       2            3
    /  |  \      /  |  \
   4       5    6       7
   |       |    |       |      
'''
#Inorder Traversal output [4,2,5,1,6,3,7]

1-> 2 [1] 3         | 1-> 2 [1] 3      | 1-> 2 [1] 3 | 1-> 2 [1] 3  | 1-> 2 [1] 3 | 1-> [4,2,5] [1] 3|1-> [4,2,5,1] 3|                            
2-> 4 [2] 5         | 2-> 4 [2] 5      | 2-> 4 [2] 5 | 2-> [4] [2] 5| 2-> [4,2,5] |                  |               |
4-> None [4] None   | 4-> [] [4] None  | 4-> [4]     |              |             |                  |               |
None-> []           |                  |             |              |             |                  |               |



class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```
![1635780982169](https://user-images.githubusercontent.com/58290134/139698372-610468d6-bf47-4455-ba46-452e91f51761.jpg)

## Binary Tree Level Order Traversal
* we traverse in level order as the name says
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''           1
           /     \
         /         \
       2            3
    /     \      /     \
   4       5    6       7     
'''
# queue = []; next_queue = []; level = []; result = [[1], [2,3],[4,5,6,7]]
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result
```
![1635782318073](https://user-images.githubusercontent.com/58290134/139701804-353bd7b5-34e8-4e89-9de1-98b04ef28c79.jpg)

## 
