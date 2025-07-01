class RedBlackTree:
  class _Node:
    def __init__(self, k, v):
      self._red = True
      self._key = k
      self._value = v
      self._left = None
      self._right = None
      self._parent = None
  
  def __init__(self):
    self._root = None
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def _search(self, node, k):
    if node is None:
      return None
    if node._key == k:
      return node
    elif node._key < k and node._right:
      return self._search(node._right, k)
    elif node._key > k and node._left:
      return self._search(node._left, k)
    return node
  
  def __getitem__(self, k):
    node = self._search(self._root, k)
    if node and node._key == k:
      return node._key
    raise KeyError('Key Error'+repr(k))
  
  def _right_rotate(self, y):
    x = y._left
    T2 = x._right
    x._right = y
    y._left = T2
    x._parent = y._parent
    y._parent = x
    if T2:
      T2._parent = y
    
    if x._parent:
      if x._parent._left == y:
        x._parent._left = x
      else:
        x._parent._right = x
    else:
      self._root = x
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
    return y

  def _sibling(self, node):
    if node._parent is None:
      return None
    if node._parent._left == node:
      return node._parent._right
    return node._parent._left
  
  def _remedying_double_red(self, node):
    if node._parent is None:
      self._root = node
      return
    if not(node._red and node._parent._red):
      return
    parent = node._parent
    uncle = self._sibling(parent)
    grandpa = parent._parent
    if uncle is None or not uncle._red: # case1
      grandpa._red = True
      if parent == grandpa._right:
        if node == parent._left:
          self._right_rotate(parent)
          node._red = False
        else:
          parent._red = False
        self._left_rotate(grandpa)
      else:
        if node == parent._right:
          self._left_rotate(parent)
          node._red = False
        else:
          parent._red = False
        self._right_rotate(grandpa)
    else: # case2
      grandpa._red = False if self._root else True
      uncle._red = False
      parent._red = False
      self._remedying_double_red(grandpa)

  def __setitem__(self, k, v):
    if self.is_empty():
      self._size += 1
      self._root = self._Node(k, v)
      self._root._red = False
      return
    node = self._search(self._root, k)
    if node._key == k:
      node._value = v
    elif node._key < k:
      self._size += 1
      newnode = self._Node(k, v)
      newnode._parent = node
      node._right = newnode
      ## red 중복 처리
      self._remedying_double_red(newnode)
    else:
      self._size += 1
      newnode = self._Node(k, v)
      newnode._parent = node
      node._left = newnode
      ## red 중복 처리
      self._remedying_double_red(newnode)

  def _fix_delete(self, parent):
    sibling = parent._left if parent._left else parent._right
    if sibling is None:
      return
    red_child = None
    if sibling._left and sibling._left._red:
      red_child = sibling._left
    elif sibling._right and sibling._right._red:
      red_child = sibling._right
    if red_child: ## case1
      if parent._left == sibling:
        if sibling._right == red_child:
          red_child._red = parent._red
          sibling._red = False
          self._left_rotate(sibling)
        else:
          sibling._red = parent._red
          red_child._red = False
        parent._red = False
        self._right_rotate(parent)
      else:
        if sibling._left == red_child:
          red_child._red = parent._red
          sibling._red = False
          self._right_rotate(sibling)
        else:
          sibling._red = parent._red
          red_child._red = False
        parent._red = False
        self._left_rotate(parent)
    elif not sibling._red and not red_child:
      parent._red = False
      sibling._red = True
    else:
      parent._red = True
      sibling._red = False
      if sibling == parent._left:
        self._right_rotate(parent)
      else:
        self._left_rotate(parent)
      self._fix_delete(parent)
  
  def __delitem__(self, k):
    if self.is_empty():
      Exception('Tree is empty')
    node = self._search(self._root, k)
    if node._key != k:
      raise KeyError('Key Error ' + repr(k))
    ## 제거노드의 자식노드가 2개인 경우 직전노드의 키, 값을 덮어씌운 후 
    ## 자식이 1개 이하인 노드를 제거하는 문제로 변형
    self._size -= 1
    if node._left and node._right:
      walk = node._left
      while walk._right:
        walk = walk._right
      node._key = walk._key
      node._value = walk._value
      node = walk
    ## 자식이 1개 이하인 노드를 색깔에 따라 제거
    
    child = node._left if node._left else node._right
    parent = node._parent
    is_red = node._red
    if parent: ## 루트노드가 아님
      if parent._left == node:
        parent._left = child
      else:
        parent._right = child
    else:
      self._root = child
    if child:
      child._parent = parent
      child._red = False ## 검은노드를 제거했을 때의 easy case
    if not is_red and child is None: ## 자식이 없는 검은색이 제거됨
      self._fix_delete(parent)
  def _inorder(self, node):
    if node is None:
      return []
    return self._inorder(node._left) + [node._key] + self._inorder(node._right)
  def print_keys(self):
    return self._inorder(self._root)
  
  def test(self, node):
    if node is None:
      return 
    if not node._red:
      return self.test(node._right if node._right else None), self.test(node._left if node._left else None)
    else:
      if node._left and node._left._red:
        raise Exception("Two red")
      if node._right and node._right._red:
        raise Exception("Two red")
      return self.test(node._right if node._right else None), self.test(node._left if node._left else None)

rbt = RedBlackTree()
from random import randint
keys = []
for _ in range(1000):
  num = randint(1, 10000)
  keys.append(num)
  rbt[num] = 1
ll = rbt.print_keys()
print(len(ll))
keys = list(set(keys))
for i in range(len(keys)//2):
  del rbt[keys[i]]
ll = rbt.print_keys()
print(len(ll))
print(ll == sorted(ll))
rbt.test(rbt._root)