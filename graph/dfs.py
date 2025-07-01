def DFS(g, u, visited):
  for e in g.incident_edges(u):
    v = e.opposite()
    if v not in visited:
      visited[v] = e
      DFS(g, v, visited)