class Stack:

  class _Node:
    def __init__(self, e):
      self._element = e
      self._next = None
  
  def __init__(self):
    self._head = None
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def last(self):
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._head._element
  
  def push(self, e):
    self._size += 1
    node = self._Node(e)
    node._next = self._head
    self._head = node
  
  def pop(self):
    if self.is_empty():
      raise Exception('Stack is empty')
    self._size -= 1
    answer = self._head._element
    self._head = self._head._next
    return answer


stack = Stack()
stack.push(3)
print(stack.pop())