def evenForest(t_nodes, t_edges, t_from, t_to):
   counter = [1]*t_nodes  
   d = defaultdict(list)
  
   def dfs(node, parent_node):
       depth = 1
       for child in d[node]:
           if child!=parent_node:
               depth+=dfs(child, node)
       counter[node-1] = depth
       return depth
      
   def findedges(node, parent_node):
       ans=0
       for child in d[node]:
           if child!=parent_node:
               if (counter[child-1]%2)==0:
                   ans+=1
               ans+=findedges(child, node)
       return ans
      
   for i in range(len(t_from)):
       d[t_from[i]].append(t_to[i])
       d[t_to[i]].append(t_from[i])
   dfs(1, None)
   return findedges(1, None)

