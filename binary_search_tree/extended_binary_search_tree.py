class BST:
    class _Node:
        __slots__ = ('_key', '_value', '_left', '_right', '_parent')
        def __init__(self, k, v):
            self._key = k
            self._value = v
            self._left, self._right, self._parent = None, None, None
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def _subtree_search(self, node, k):
        if node is None:
            return None
        if node._key == k:
            return node
        elif node._key < k and node._right:
            return self._subtree_search(node._right, k)
        elif node._key > k and node._left:
            return self._subtree_search(node._left, k)
        return node
    
    def _add_root(self, k, v):
        self._root = self._Node(k, v)
        self._size += 1
    
    def _add_left(self, node, k, v):
        newnode = self._Node(k, v)
        node._left = newnode
        newnode._parent = node
        self._size += 1
    
    def _add_right(self, node, k, v):
        newnode = self._Node(k, v)
        node._right = newnode
        newnode._parent = node
        self._size += 1
    
    def __setitem__(self, k, v):
        if self.is_empty():
            self._add_root(k, v)
            return
        node = self._subtree_search(self._root, k)
        if node._key == k:
            node._value = v
        elif node._key < k:
            self._add_right(node, k, v)
        else:
            self._add_left(node, k, v)
    
    def __getitem__(self, k):
        if self.is_empty():
            raise Exception('Tree is empty')
        node = self._subtree_search(self._root, k)
        if node._key != k:
            raise Exception('Key Error' + repr(k))
        return node._value
    
    def __delitem__(self, k):
        if self.is_empty():
            raise Exception('Tree is empty')
        node = self._subtree_search(self._root, k)
        if node._key != k:
            raise Exception('Key Error' + repr(k))
        if node._left and node._right: ## has tow children
            current = node._left
            while current._right:
                current = current._right
            node._key, node._value = current._key, current._value
            parent = current._parent
            if parent._left == current:
                parent._left = current._left
            else:
                parent._right = current._left
            if current._left:
                current._left._parent = parent
        else:
            child = node._left if node._left else node._right
            parent = node._parent
            if child:
                child._parent = parent
            if parent: ## node is not root
                if parent._left == node:
                    parent._left = child
                else:
                    parent._right = child
            else: ## node is root
                self._root = child