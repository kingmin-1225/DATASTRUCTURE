## quick sort
class Queue:
  class _Node:
    def __init__(self, e):
      self._element = e
      self._next = None
  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0
  
  def is_empty(self):
    return self._size == 0
  
  def __len__(self):
    return self._size
  
  def top(self):
    if self.is_empty():
      raise Exception("Queue is Empty")
    return self._head._element
  
  def enqueue(self, e):
    newnode = self._Node(e)
    if self.is_empty():
      self._head = newnode
    else:
      self._tail._next = newnode
    self._tail = newnode
    self._size += 1
  
  def dequeue(self):
    if self.is_empty():
      raise Exception("Queue is Empty")
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():
      self._tail = None
    return answer

def quick_sort(S):
  if len(S) == 0:
    return
  p = S.top()
  L, E, G = Queue(), Queue(), Queue()
  while len(S) > 0:
    if S.top() < p:
      L.enqueue(S.dequeue())
    elif S.top() > p:
      G.enqueue(S.dequeue())
    else:
      E.enqueue(S.dequeue())
  
  quick_sort(L)
  quick_sort(G)
  while len(L) > 0:
    S.enqueue(L.dequeue())
  while len(E) > 0:
    S.enqueue(E.dequeue())
  while len(G) > 0:
    S.enqueue(G.dequeue())

from random import randint

q = Queue()
checking = []
for _ in range(1000):
  num = randint(1, 10000)
  q.enqueue(num)
  checking.append(num)
checking.sort()

quick_sort(q)
ans = []
while len(q) > 0:
  ans.append(q.dequeue())
print(ans == checking)


## inplace quick sort

def quick_sort_inplace(S, a, b):
  if a >= b:
    return
  p = S[b]
  left = a
  right = b-1
  while left <= right:
    while left <= right and S[left] < p:
      left += 1
    while left <= right and S[right] > p:
      right -= 1
    if left <= right:
      S[left], S[right] = S[right], S[left]
      left += 1
      right -= 1
  S[left], S[b] = S[b], S[left]
  quick_sort_inplace(S, a, left-1)
  quick_sort_inplace(S, left+1, b)

ll = []
checking = []
for _ in range(1000):
  num = randint(1, 10000)
  checking.append(num)
  ll.append(num)

quick_sort_inplace(ll, 0, len(ll)-1)
checking.sort()
print(checking == ll)