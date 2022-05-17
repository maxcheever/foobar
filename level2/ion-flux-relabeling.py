# finds the parent of a node in a binary tree with nodes values being post-order
def solution(h,q):
   p = []
   for n in q:
      # search space is 1-(2^n-1)
      root = 1
      furthest = 2**h - 1
      if furthest == n:
         p.append(-1)
      else:
         while n>0:
            furthest-=1
            half = root + (furthest-root)//2
            # each node has child of x/2 or x-1
            if half == n or furthest == n:
               p.append(furthest+1)
               break
            elif n > half:
               root = half
            else:
               furthest = half
   return p