class Stack:
  class _Node:
    __slots__ = '_element', '_next' # __slots__: 클래스가 가진 인스턴스를 고정시킴(메모리 절약)
    def __init__(self, e, next):
      self._element = e
      self._next = next
  
  def __init__(self):
    self._head = None
    self._size = 0

  def __len__(self):
    return self._size
  
  def is_empty(self):
    return self._size == 0
  
  def push(self, e):
    self._head = self._Node(e, self._head)
    self._size += 1
  
  def top(self):
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._head._element
  
  def pop(self):
    if self.is_empty():
      raise Exception('Stack is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    return answer

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.top())
# print(stack.pop())
# print(stack.pop())
# print(len(stack))