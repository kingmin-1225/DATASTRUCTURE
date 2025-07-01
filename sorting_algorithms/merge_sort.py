def merge_sort(S):
  n = len(S)
  if n < 2:
    return
  mid = n//2
  S1 = S[:mid]
  S2 = S[mid:]
  merge_sort(S1)
  merge_sort(S2)
  merge(S1, S2, S)

def merge(S1, S2, S):
  i = j = 0
  while i + j < len(S):
    if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
      S[i+j] = S1[i]
      i += 1
    else:
      S[i+j] = S2[j]
      j += 1

from random import randint

ll = []
for _ in range(1000):
  num = randint(1, 10000)
  ll.append(num)

answer = sorted(ll)
merge_sort(ll)
print(answer == ll)

## ---------------------------Linked_list merge_sort-------------------------
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from deque.deque import Deque

def merge_sort_l(S):
  n = len(S)
  if n < 2:
    return
  S1 = Deque()
  S2 = Deque()
  for i in range(n):
    if i < n//2:
      S1.push_right(S.pop_left())
    else:
      S2.push_right(S.pop_left())
  
  merge_sort_l(S1)
  merge_sort_l(S2)
  
  merge_l(S1, S2, S)

def merge_l(S1, S2, S):
  while len(S1)+len(S2) > 0:
    if len(S1) == 0 or (len(S2) > 0 and S1.head() > S2.head()):
      S.push_right(S2.pop_left())
    else:
      S.push_right(S1.pop_left())

S = Deque()
checking = []
for _ in range(1000):
  num = randint(1, 10000)
  checking.append(num)
  S.push_right(num)

checking.sort()
merge_sort_l(S)

is_right = True
while len(S) > 0:
  if checking.pop() != S.pop_right():
    is_right = False
    break

print(True if is_right else False)