import random

# n elemanlı array oluşturan fonksiyon
def generate_an_array(n):
  my_array=[]
  for i in range(n):
    s=random.randint(0,100)     # 0 ile 100 arası random sayı oluştur
    my_array.append(s)          # oluşturalan random sayıyı array e ekle
  return my_array

my_arr_1=generate_an_array(10)
print(my_arr_1)
print("\n")

# array elemanlarını iteratif olarak dictionary biçiminde yazdırma
for i in range(len(my_arr_1)):
  print(i,":",my_arr_1[i])
print("\n")

# array elemanlarını iteratif olarak yanyana yazdıran fonksiyon
def print_an_array(my_arr_1):
  for item in my_arr_1:
    print(item, end=" ")
        
print_an_array(my_arr_1)
print("\n")

# array elemanlarını bubble sort ile küçükten büyüğe sıralayan fonksiyon
def my_bubble_sort(my_array):
  for i in range(len(my_arr_1)-1,0,-1):
    for j in range(i):
      if(my_arr_1[j]>my_arr_1[j+1]):
        t=my_arr_1[j]
        my_arr_1[j]=my_arr_1[j+1]
        my_arr_1[j+1]=t

my_bubble_sort(my_arr_1)
print_an_array(my_arr_1)
print("\n")

# array içerisinde parametre ile gönderilen değeri arayan fonksiyon
def search_an_array(my_array,n):
  found=False
  step=0                          # aranan sayının kaç adımda bulduğumuzu tutan değişken
  for i in range(len(my_array)):
    if(my_array[i]==n):         # aranan sayının kontrol edildiği yer
      found=True
      step=i+1
  if(found==False):
    print("not found")
  else:
    print("found:",found,"step:",step)

search_an_array(my_arr_1,100)
