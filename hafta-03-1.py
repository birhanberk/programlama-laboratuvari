# vektörel iç çarpım
def vector_inner_product(v,w):
  size=len(v)
  result=[]
  for i in range(size):
    result.append(0)
  for i in range(size):
    result[i]=v[i]*w[i]
  t=0
  for i in range(size):
    t=t+result[i]
  return t

# skaler çarpım
def vector_scalar_product(alpha,v):
  size=len(v)
  result=[]
  for i in range(size):
    result.append(0)
  for i in range(size):
    result[i]=alpha*v[i]
  return result

# vektörlerin çıkarılması
def vector_substraction(v,w):
  size=len(v)
  result=[]
  for i in range(size):
    result.append(0)
  for i in range(size):
     result[i]=v[i]-w[i]
  return result

def vector_addition(v,w):
  size=len(v)
  result=[]
  for i in range(size):
    result.append(0)
  for i in range(size):
    result[i]=v[i]+w[i]
  return result

v=[3,4,5]
w=[2,0,1]
print(vector_inner_product(v,w))
print(vector_scalar_product(5,v))
print(vector_substraction(v,w))
print(vector_addition(v,w))
