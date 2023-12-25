def form(n):
   res = (4*(n**2))-6*(n-1)
   return res


def spiral(m):
   res = 1
   for i in range(3,m+1,2):
       res += form(i)
   return res


print(spiral(1001))
