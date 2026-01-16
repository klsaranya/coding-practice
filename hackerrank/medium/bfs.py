def bfs(n, m, edges, s):
   d = defaultdict(set)
   for [key, value] in edges:
       d[key].add(value)
       d[value].add(key)
   res = [-1] * n
   que = deque()
   que.append(s)
   multiplier = 1
   while que:
       for _ in range(len(que)):
           root = que.popleft()
           if root in d:
               for c in d[root]:
                   if res[c-1]==-1:
                       res[c-1] = 6 * multiplier
                       que.append(c)
       multiplier+=1
   res.pop(s-1)
   return res
