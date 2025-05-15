class AVL:
  class _Node:
    __slots__ = '_key', '_value', '_left', '_right', '_parent', '_height'
    def __init__(self, k, v):
      self._key = k
      self._value = v
      self._parent = None
      self._left = None
      self._right = None
      self._height = 1
  
  def __init__(self):
    self._size = 0
    self._root = None
  
  def _height(self, node):
    if node:
      return node._height
    return 0 

  def _update_height(self, node):
    if node is not None:
      node._height = max(self._height(node._left), self._height(node._right)) + 1
  
  def _balance_factor(self, node):
    if node is None:
      return 0
    return self._height(node._left) - self._height(node._right)
  
  def _right_rotate(self, y):
    x = y._left
    T2 = x._right
    
    x._right = y
    y._left = T2

    x._parent = y._parent
    y._parent = x
    if T2:
      T2._parent = y
    
    if x._parent: ## x가 루트가 아닐경우
      if x._parent._left == y:
        x._parent._left = x
      else:
        x._parent._right = x
    else: # x가 루트임
      self._root = x
    
    self._update_height(y)
    self._update_height(x)

    return x

  def _left_rotate(self, x):
    y = x._right
    T2 = y._left

    y._left = x
    x._right = T2
    y._parent = x._parent
    x._parent = y
    if T2:
      T2._parent = x
    
    if y._parent:
      if y._parent._left == x:
        y._parent._left = y
      else:
        y._parent._right = y
    else:
      self._root = y

    self._update_height(x)
    self._update_height(y)

    return y  

  def is_empty(self):
    return self._size == 0
  
  def _add_root(self, k, v):
    self._root = self._Node(k, v)
    self._size += 1

  def _add_left(self, node, k, v):
    new_node = self._Node(k, v)
    node._left = new_node
    new_node._parent = node
    self._size += 1
    self._update_height(node)
  
  def _add_right(self, node, k, v):
    new_node = self._Node(k, v)
    node._right = new_node
    new_node._parent = node
    self._size += 1
    self._update_height(node)

  def _subtree_search(self, node, k):
    if node is None:
      return None
    if node._key == k:
      return node
    elif node._key < k and node._right:
      return self._subtree_search(node._right, k)
    elif k < node._key and node._left:
      return self._subtree_search(node._left, k)
    return node
  
  def __len__(self):
    return self._size
  
  def _rebalance(self, node):
    current = node
    while current is not None:
      self._update_height(current)
      balance = self._balance_factor(current)
      if balance > 1: 
        if self._balance_factor(current._left) < 0: #LR
          self._left_rotate(current._left)
        self._right_rotate(current)
      elif balance < -1:
        if self._balance_factor(current._right) > 0: #RL
          self._right_rotate(current._right)
        self._left_rotate(current)
      current = current._parent


  def __setitem__(self, k, v):
    if self.is_empty():
      self._add_root(k, v)
    else:
      node = self._subtree_search(self._root, k)
      if node._key == k:
        node._value = v
      elif node._key < k:
        self._add_right(node, k, v)
        self._rebalance(node)
      else:
        self._add_left(node, k, v)
        self._rebalance(node)
  
  def __getitem__(self, k):
    node = self._subtree_search(self._root, k)
    if node._key == k:
      return node._value
    else:
      return -1
  
  def __delitem__(self, k):
    if self.is_empty():
      return
    node = self._subtree_search(self._root, k)
    if node._key == k:
      self._size -= 1
      parent = node._parent
      if not (node._left and node._right): ## 자식노드 한 개 이하
        child = node._left if node._left else node._right
        if parent: ## 제거 대상 노드가 루트가 아닐 경우
          if node == parent._left:
            parent._left = child
          else:
            parent._right = child
          self._rebalance(parent)
        else: ## 제거 대상 노드가 루트일 경우
          self._root = child
        if child:
          child._parent = parent
      else: ## 자식노드 두 개
        walk = node._left
        while walk._right is not None:
          walk = walk._right
        self.__delitem__(walk._key)
        node._key = walk._key
        node._value = walk._value
        self._rebalance(walk._parent)
  
  def _inorder(self, node):
    if node is None:
      return []
    return self._inorder(node._left) + [node._key] + self._inorder(node._right)

  def print_keys(self):
    return self._inorder(self._root)

from random import randint

bst = AVL()

checking = []
for _ in range(1000):
  num = randint(1, 10000)
  bst[num] = 1
  if num not in checking:
    checking.append(num) 
checking.sort()
tree_list = bst.print_keys()
print()
print("-----CHECKING-----")
print("__setitem__ : IT'S WORKING" if checking == tree_list else "IT'S FAILED")

for _ in range(1000):
  num = randint(1, 10000)
  del bst[num]
  if num in checking:
    checking.remove(num)

checking.sort()
tree_list = bst.print_keys()
print("__delitem__ : IT'S WORKING" if checking == tree_list else "IT'S FAILED")
print()