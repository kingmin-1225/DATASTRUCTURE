def BFS(g, start, visited):
  level = [start]
  while len(level) > 0:
    next_level = []
    for u in level:
      for e in g.incident_edges(u):
        v = e.opposite()
        if v not in visited:
          visited[v] = e
          next_level.append(v)
    level = next_level
