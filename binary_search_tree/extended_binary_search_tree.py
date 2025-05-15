class BST:
  class _Node:
    __slots__ = '_key', '_value', '_left', '_right', '_parent'
    def __init__(self, k, v):
      self._key = k
      self._value = v
      self._parent = None
      self._left = None
      self._right = None
  
  def __init__(self):
    self._size = 0
    self._root = None
  
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
  
  def _add_right(self, node, k, v):
    new_node = self._Node(k, v)
    node._right = new_node
    new_node._parent = node
    self._size += 1

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
  
  def __setitem__(self, k, v):
    if self.is_empty():
      self._add_root(k, v)
    else:
      node = self._subtree_search(self._root, k)
      if node._key == k:
        node._value = v
      elif node._key < k:
        self._add_right(node, k, v)
      else:
        self._add_left(node, k, v)
  
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
  
  def _inorder(self, node):
    if node is None:
      return []
    return self._inorder(node._left) + [node._key] + self._inorder(node._right)

  def print_keys(self):
    return self._inorder(self._root)