# 3x3 lük bir matrisin m nin satır ve n inci sütununu silen fonksiyon
def delete_row_col_from_matrix(matrix,m,n):
  result=[]
  size_1=len(matrix)                        #satır sayısı
  size_2=len(matrix[0])                     #sütun sayısı
  for i in range(size_1):
    if(i==m):
      continue
    row_1=[]
    for j in range(size_2):
      if(j==n):
        continue
      row_1.append(matrix[i][j])
    result.append(row_1)
  return result

# 2x2 lik bir matrisin determinantını bulan fonksiyon
def matrix_det_2x2(matrix):
  s_1=matrix[0][0]*matrix[1][1]
  s_2=matrix[0][1]*matrix[1][0]
  return(s_1-s_2)

# 3x3 lük bir matrisin determinantını bulan fonksiyon
def matrix_det_3x3(matrix):
  a_1=matrix[0][0]
  a_2=delete_row_col_from_matrix(matrix,0,0)
  a_3=matrix_det_2x2(a_2)
  a_4=a_1*a_3
   
  b_1=matrix[0][1]                            #-1
  b_2=delete_row_col_from_matrix(matrix,0,1)
  b_3=matrix_det_2x2(b_2)
  b_4=b_1*b_3

  c_1=matrix[0][2]
  c_2=delete_row_col_from_matrix(matrix,0,2)
  c_3=matrix_det_2x2(c_2)
  c_4=c_1*c_3

  return a_4-b_4+c_4

# 4x4 lük bir matrisin determinantını bulan fonksiyon
def matrix_det_4x4(matrix):
  a_1=matrix[0][0]
  a_2=delete_row_col_from_matrix(matrix,0,0)
  a_3=matrix_det_3x3(a_2)
  a_4=a_1*a_3
   
  b_1=matrix[0][1]                            #-1
  b_2=delete_row_col_from_matrix(matrix,0,1)
  b_3=matrix_det_3x3(b_2)
  b_4=b_1*b_3

  c_1=matrix[0][2]
  c_2=delete_row_col_from_matrix(matrix,0,2)
  c_3=matrix_det_3x3(c_2)
  c_4=c_1*c_3

  d_1=matrix[0][3]                            #-1
  d_2=delete_row_col_from_matrix(matrix,0,3)
  d_3=matrix_det_3x3(d_2)
  d_4=d_1*d_3

  return a_4-b_4+c_4-d_4

matrix_1=[[1,2],[3,4]]
matrix_2=[[1,2,3],[4,5,6],[7,8,9]]
matrix_3=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

sonuc=matrix_det_2x2(matrix_1)
print(sonuc)

sonuc=matrix_det_3x3(matrix_2)
print(sonuc)

sonuc=matrix_det_4x4(matrix_3)
print(sonuc)
