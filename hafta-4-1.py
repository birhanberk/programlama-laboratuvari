# 2 matrisi toplayan fonksiyon
def matrix_addition(m_1,m_2):
  result=[]
  for row in range(len(m_1)):
    result.append([])
    for column in range(len(m_1[0])): #ya da (len(m_1)+1) da olur
      #print(m_1[row][column],end=" ")
      result[row].append(m_1[row][column]+m_2[row][column])
  return result
  
# 2 matrisi çıkaran fonksiyon
def matrix_substraction(m_1,m_2):
  result=[]
  for row in range(len(m_1)):
    result.append([])
    for column in range(len(m_1[0])):
      #print(m_1[row][column],end=" ")
      result[row].append(m_1[row][column]-m_2[row][column])
  return result

# matrisi skaler çarpan fonksiyon
def matrix_scalar_product(alpha,m_1):
  result=[]
  for row in range(len(m_1)):
    result.append([])
    for column in range(len(m_1[0])):
      #print(m_1[row][column],end=" ")
      result[row].append(m_1[row][column]*alpha)
  return result

matrix_1=[[1,2,3], [4,5,6]]
matrix_2=[[7,3,9], [1,10,8]]
alpha=10
print(matrix_scalar_product(alpha,matrix_1))
print(matrix_addition(matrix_1,matrix_2))
print(matrix_substraction(matrix_1,matrix_2))

# i inci satırı döndüren fonksiyon
def f_1(matrix_1,i):
  return matrix_1[i]

print(f_1(matrix_1,1))

# j inci sütunu döndüren fonksiyon
def f_2(matrix_1,j):
  j_th_col=[]
  for row in matrix_1:
    for indis in range(len(row)):
      if(indis==j):
        j_th_col.append(row[indis])
  return j_th_col

print(f_2(matrix_1,0))

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

# matris çarpımı
def matrix_multiply(m_1,m_2):
  result=[]
  for row in range(len(m_1)):
    result.append([])
    for column in range(len(m_2[0])):
      a=f_1(m_1,row)
      b=f_2(m_2,column)
      c=vector_inner_product(a,b)
      result[row].append(c)
  return result

matrix_1=[[1,2,3], [4,5,6]]
matrix_2=[[7,3], [1,10],[0,2]]
print(matrix_multiply(matrix_1,matrix_2))
