# Binary Tree
=============


Binary Tree is a non linear data structure.
* It has only one root node
* Except for root node all the node have parents
* It can have as many children as you want

## Creating Root
```python
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
root.PrintTree()
```

```
Output
10
```

## 
