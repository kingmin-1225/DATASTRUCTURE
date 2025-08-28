class AVL:
    class _Node:
        __slots__ = ('_key', '_value', '_left', '_right', '_parent', '_height')
        def __init__(self, k, v):
            self._key = k
            self._value = v
            self._parent = None
            self._left = None
            self._right = None
            self._height = 1
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0    
    
    def __len__(self):
        return self._size
    
    def _height(self, node):
        if node is None:
            return 0
        return node._height
    
    def _update_height(self, node):
        if node is not None:
            node._height = 1 + max(self._height(node._left), self._height(node._right))
    
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
        if T2 is not None:
            T2._parent = y
        
        if x._parent is not None:
            if x._parent._left == y:
                x._parent._left = x
            else:
                x._parent._right = x
        else:
            self._root = x
        
        self._update_height(y)
        self._update_height(x)
    
    def _left_rotate(self, x):
        y = x._right
        T2 = y._left
        y._left = x
        x._right = T2
        y._parent = x._parent
        x._parent = y
        if T2 is not None:
            T2._parent = x
        if y._parent is not None:
            if y._parent._left == x:
                y._parent._left = y
            else:
                y._parent._right = y
        else:
            self._root = y
        self._update_height(x)
        self._update_height(y)
    
    def _add_root(self, k, v):
        self._root = self._Node(k, v)
        self._size += 1
    
    def _add_left(self, node, k, v):
        newnode = self._Node(k, v)
        node._left = newnode
        newnode._parent = node
        self._size += 1
        self._update_height(node)
    
    def _add_right(self, node, k, v):
        newnode = self._Node(k, v)
        node._right = newnode
        newnode._parent = node
        self._size += 1
        self._update_height(node)
    
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
    
    def _rebalance(self, node):
        current = node
        while current is not None:
            balance = self._balance_factor(current) ## balance_factor : left-right
            if balance > 1: ## left_height > right_height
                if self._balance_factor(current._left) < 0:
                    self._left_rotate(current._left)
                self._right_rotate(current)
            elif balance < -1: ## left_height < right_height
                if self._balance_factor(current._right) > 0:
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
        if self.is_empty():
            raise Exception('Tree is empty')
        node = self._subtree_search(self._root, k)
        if node._key != k:
            raise Exception('Key Error ' + repr(k))
        return node._value
    
    def __delitem__(self, k):
        if self.is_empty():
            raise Exception('Tree is empty')
        node = self._subtree_search(self._root, k)
        if node._key != k:
            raise Exception('Key Error ' + repr(k))
        self._size -= 1
        if node._left and node._right: ## node has two children
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
            self._rebalance(parent)
        else: ## node has fewer than two children
            parent = node._parent
            child = node._left if node._left else node._right
            if parent: ## node is not root
                if parent._left == node:
                    parent._left = child
                else:
                    parent._right = child
                self._rebalance(parent)
            else: ## node is root
                self._root = child
            if child:
                child._parent = parent