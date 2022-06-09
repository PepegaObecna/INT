from random import randrange
a = randrange(1, 100)
print(a)
def f(x):
    if x!=4:
        a.append(x)
        if x%2==0:
      while x%2==0:
        x=x/2
        a.append(x)
    x=3*x+1
    f(x)
for i in range(1, 1000000):
  a=[]
  f(i)
  print(i, "gives output" ,a)  