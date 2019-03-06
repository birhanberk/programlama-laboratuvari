# array elemanlarını selection sort algoritması ile küçükten büyüğe sıralayan fonksiyon
def selection_sort(my_array):
  swap_count=0                          # kaç swap yapıldığını tutan değişken
  for i in range(len(my_array)-1,0,-1):
    positionOfMax=0
    for location in range(0,i+1,1):
      if(my_array[location]>my_array[positionOfMax]):
        positionOfMax=location
    temp=my_array[location]
    my_array[location]=my_array[positionOfMax]
    my_array[positionOfMax]=temp
    swap_count=swap_count+1
  print("number of exchange :",swap_count)

my_array=[21,12,13,44,25,2,7,16,14,35]
selection_sort(my_array)
print(my_array)
print("\n")

# array içerisinde parametre ile gönderilen değeri binary search algoritması ile arayan fonksiyon 
def binary_search(my_array,item):
  first=0                               # array in ilk elemanı
  last=len(my_array)-1                  # array in son elemanı
  found=False
  step=0                                # aranan sayının kaç adımda bulduğumuzu tutan değişken
  while first<=last and not found:
    midpoint=(first+last)//2
    #print("first - last",first,last)
    step=step+1
    if(my_array[midpoint]==item):
      found=True
    else:
      if(item<my_array[midpoint]):
        last=midpoint-1
      else:
        first=midpoint+1
  return found,midpoint,step

print(binary_search(my_array,25))
