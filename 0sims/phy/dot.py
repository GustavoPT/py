import numpy as np 

v1 = np.array([1,2,3])

v2 = np.array([2,3,4])

def dotProduct(a,b):
    total = a[0] * b[0] + a[1] * a[1] +a[2] * b[2]
    return total

answer = dotProduct(v1,v2)

print(answer)