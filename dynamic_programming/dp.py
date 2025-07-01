## matrix
def matrix_chain(d):
  n = len(d)-1
  N = [[0]*n for _ in range(n)]
  for b in range(1, n):
    for i in range(n-b):
      j = i + b
      N[i][j] = min(N[i][k]+N[k+1][j]+d[i]*d[k+1]*d[j+1] for k in range(i, j))
  return N



## lcs
def LCS(X, Y):
  n, m = len(X), len(Y)
  L =  [[0] * (m+1) for _ in range(n+1)]
  for j in range(n):
    for k in range(m):
      if X[j] == Y[k]:
        L[j+1][k+1] = L[j][k]+1
      else:
        L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
  return L

