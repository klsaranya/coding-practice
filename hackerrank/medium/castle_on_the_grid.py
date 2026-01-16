def minimumMoves(grid, startX, startY, goalX, goalY):
   q = deque([(startX, startY,0)])
   N = len(grid)
   visit = set((startX, startY))
   while q:
       x,y,depth = q.popleft()
       directions = [(-1,0),(1,0),(0,-1),(0,1)]
       for dx,dy in directions:
           i, j = x, y
           while True:
               i+=dx
               j+=dy
               if i==goalX and j==goalY:
                   return depth+1
               if i>=N or j>=N or i<0 or j<0 or grid[i][j]=='X':
                   break
               if grid[i][j]=='.' and (i,j) not in visit:
                   visit.add((i,j))
                   q.append((i,j,depth+1))
   return -1

