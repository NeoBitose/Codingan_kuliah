def dfs_recursive(graph, source, goal, path = []):

  if goal not in graph:
      return path
    
  if goal not in path: 
    path.append(source)
    
    if source not in graph:
      return path
    
    for neighbour in graph[source]:
      path = dfs_recursive(graph, neighbour, goal, path)
  
  return path

graph = {"A":["B", "C", "D"],
"B":["E"],
"C":["G","F"],
"D":["H"],
"E":["I"],
"F":["J"],
"G":["K"]}

dfs_element = dfs_recursive(graph, "A", "D")
print(dfs_element)