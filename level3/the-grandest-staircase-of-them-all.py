#                                            inf                                
# generator function for partition => G(x) = PI (1+x^n) = (1+x)(1+x^2)...(1+x^n-1) = 1 + x + x^2 + 2x^3 + 2x^4 + 3x^5...
#                                            n=1
#                                                                               [1] [2]  [3]   [4]    [5]    [6]
# coefficient of x^(n-1) = number of distinct partitions of n so Gcoef[i] + 1 => 1 + x + x^2 + 2x^3 + 2x^4 + 3x^5..
# Gcoef[0:3] never used due to constraints being 3 <= n <= 200
def solution(n):
   # initialize coefficients of generator G(x) with special case Gcoef[0] = 1 (there is no x^-1 in the expanded polynomial)
   Gcoef = [int(i==0) for i in range(n+1)] # only need the n-1 coefficents for up to n terms of G(x)
   for j in range(1,n):
      # essentially adds +j index of G to G
      Gcoef = [Gcoef[k] if k-j<0 else Gcoef[k-j] + Gcoef[k] for k in range(n+1)] # contains coeffecient of x^(n-1) from 0 to n
        
   return Gcoef[n]