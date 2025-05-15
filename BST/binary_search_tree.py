class BST:
  class _Node:
    def __init__(self, e):
      self.element = e
      self.left = None
      self.right = None
  
  def __init__(self):
    self.size = 0
    self.root = None
  
  def _insert(self, node, e):
    if node is None:       
      self.size += 1
      return self._Node(e)
    if node.element <= e:
      node.right = self._insert(node.right, e)
    else:
      node.left = self._insert(node.left, e)
    return node
  
  def _remove(self, node, e):
    if node is None: ## 대상 노드가 없음
      return None
    self.size -= 1
    if node.element == e: ## 대상 노드임
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      ## 2 childs
      walk = node.left
      while walk.right is not None:
        walk = walk.right
      node.element = walk.element
      node.left = self._remove(node.left, walk.element)
    elif node.element < e:
      node.right = self._remove(node.right, e)
    else:
      node.left = self._remove(node.left, e)
    return node
  
  def _inorder(self, node):
    if node is None:
      return []
    return self._inorder(node.left) + [node.element] + self._inorder(node.right)
    
  
  def print_nodes(self):
    return self._inorder(self.root)

  def add(self, e):
    self.root = self._insert(self.root, e)
  
  def delete(self, e):
    self.root = self._remove(self.root, e)

from random import randint


tree = BST()

checking = []
for _ in range(10000):
  num = randint(1, 10000000)
  tree.add(num)
  checking.append(num)

for _ in range(10000):
  num = randint(1, 100000)
  tree.delete(num)
  if num in checking:
    checking.remove(num)


checking.sort()
tree_list = tree.print_nodes()
print(tree_list)
print(len(tree_list))
print("IT'S WORKING" if checking == tree_list else "IT'S FAILED")