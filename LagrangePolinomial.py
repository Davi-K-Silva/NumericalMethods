import numpy as np



x = [-1,0,1,2]
y = [-5,6,19,30]

x1 = [1,0]
y1 = [6,19]

x2 = [-1,0,1]
y2 = [-5,6,19]

xt = 0.5
l1 = (xt - x[2])/(x[1]-x[2])
l2 = (xt - x[1])/(x[2]-x[1])
print (y[1]*l1 + y[2]*l2)

g = xt**2 + 12*xt + 6
print(g)

def L(xt,x,i):
    result = []
    for j in range(len(x)):
        if(j != i):
            result.append((xt-x[j])/(x[i]-x[j]))
    return np.prod(result)
         

def Lagrange(x,y,xt):
    result = []
    for i in range(len(x)):
        result.append(y[i]*L(xt,x,i))
    return np.sum(result)

print(Lagrange(x1,y1,0.5))


xe2 = [0,2,4,6]
ye2 = [1,7,17,71]

print(Lagrange(xe2,ye2,7))
print(Lagrange(xe2,ye2,5))
print(Lagrange(xe2,ye2,3))