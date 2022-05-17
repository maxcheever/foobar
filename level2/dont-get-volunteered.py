# original thought was to treat the board like [0...63] and have moves be 17, -17, etc
# could also use oop for nodes
# uses a BFS graph traversal to find the shortest move from src to dest
def solution(src, dest):
   src = [src%8, src//8, 0] # [x, y, cost]
   dest = [dest%8, dest//8]
   visited = []
   q = [src] # FIFO Queue for moves
   # possible moves for knight [up[i],side[i]]
   up = [2,2,1,1,-1,-1,-2,-2]
   side = [-1,1,-2,2,-2,2,-1,1]
   while q:
      n = q.pop(0)
      if n[0] == dest[0] and n[1] == dest[1]:
         return n[2]
      if n not in visited:
         visited.append(n)
         for i in range(8): # length of a column or row on chess board
            nn = [n[0]+side[i],n[1]+up[i],n[2]+1]
            if onBoard(nn):
               q.append(nn)

# checks if a move is on the chess board
def onBoard(n):
   return n[0]>=0 and n[0]<=8 and n[1]>=0 and n[1]<=8
      

