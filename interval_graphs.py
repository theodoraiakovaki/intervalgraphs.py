from collections import deque
import sys
method=sys.argv[1]
filename = sys.argv[2]
with open(filename, 'r') as f:
   edges = [list(map(int, line.strip().split())) for line in f.readlines()]
edges.sort()

def lexbfs():
 nodes = set(sum(edges, []))
 bfs_ordering= []
 S = deque([nodes])
 while S:
   u = S[0].pop()
   bfs_ordering.append(u)
   if not S[0]:
      S.popleft()
   new_sv = set()
   indexes = []
   neighbors = set()
   neighbors = [v for edge in edges for v in edge if u in edge and v not in bfs_ordering]
   f = False
   for s in list(S):
      new_neighbors = s.intersection(neighbors) #check for neighbours in sv
      new_neighbors = sorted(set(new_neighbors))
      if s.issubset(new_neighbors): #skip creating a new set if there is already in the S
         f = True
      else:
         new_sv = set()
         s.difference_update(new_neighbors) #remove neighbours from sv
         new_sv.update(new_neighbors)
         index = S.index(s) 
      if new_sv not in S: 
         S.insert(index, (new_sv))
   S = deque([s for s in S if s])
 return (bfs_ordering)

def chordal():
   bfs_ordering = lexbfs()
   bfs_ordering.reverse()
   is_valid = True
   while not is_valid:
    for u in bfs_ordering:
       neighbors = [v for edge in edges for v in edge if u in edge and v!=u]
       neighbors.reverse()
       v= neighbors[0]      
       rn_u = {next_u for next_u in neighbors if bfs_ordering.index(next_u)>bfs_ordering.index(u)}
       rn_v= {next_v for next_v in neighbors if bfs_ordering.index(next_v) > bfs_ordering.index(v)}
       rn_u = rn_u - {v}
       if not rn_u.issubset(rn_v):
          is_valid = False
   return (is_valid)
       

def interval():
    nodes = set(sum(edges, []))
    n = len(nodes)  # Number of nodes
    c = [['unknown'] * n for _ in range(n)]
    for u in nodes.copy():  
      neighbours = {v for edge in edges for v in edge if u in edge}
      nodes.difference_update(neighbours)
      new_edges= [[v1, v2] for v1, v2 in edges if not any(x in neighbours for x in (v1, v2))] #remove all neighbours from the edges
      components = bfs(new_edges, nodes)
      nodes = set(sum(edges, []))
    for u in nodes:
      neighbours = {v for edge in edges for v in edge if u in edge}
      for v in nodes: 
         if u in neighbours and v in neighbours:
            c[u][v]=0
         else:
            c[u][v] = components.pop(0)
    f= True
    for edge in edges:
       for u in edge:
         for v in edge:
          for w in edge:
             if u!=v and w!=u and v!=w:
              if c[u][v]== c[u][w] and c[v][u] == c[v][w] and c[w][u] == c[w][v]:
                f = False
    interval_graph = False
    if f == True and chordal():
       interval_graph = True
    return (interval_graph)

last_letter = ord('a')
components = []
def bfs(new_edges, nodes):
   global last_letter
   queue = deque()
   visited = {}
   node_edges= {node: [edge for edge in new_edges if node in edge] for node in nodes}
   for node in nodes:
    visited[node] = False
   nodes_copy = nodes.copy()
   node = nodes_copy.pop()
   queue.appendleft(node)
   while not (len(queue)==0):
      c = queue.pop()
      visited[c]=True
      for v in node_edges[c]:
         for i in v:
            if not visited[i] and i not in queue:
                queue.appendleft(i)
   for node in nodes:
      if visited[node]:
          components.append(chr(last_letter))
      else:
         last_letter +=1
         components.append(chr(last_letter))
   last_letter +=1
   return (components)

if method == 'lexbfs':
   bfs_ordering = lexbfs()
   print (bfs_ordering)
elif method == 'chordal':
  is_chordal = chordal()
  print (is_chordal)
elif method == 'interval':
   is_interval= interval()
   print (is_interval)
