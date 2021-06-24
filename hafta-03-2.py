# Kendisine atanan bir listenin frekans tablosunu bulup return eden bir fonksiyon yazınız.

# Çözüm 1.1
def frekans_bul_1_1(liste):
  frekans = {} 
  for i in range(len(liste)):
    if(liste[i] in frekans):
      frekans[liste[i]] = frekans[liste[i]] + 1
    else:
      frekans[liste[i]]=1
  return frekans

# Çözüm 1.2
def frekans_bul_1_2(liste):
  frekans = {} 
  for i in liste:
    if(i in frekans):
      frekans[i] = frekans[i] + 1
    else:
      frekans[i]=1
  return frekans


# Çözüm 2
def frekans_bul_2(liste):
  frekans = []
  for i in range(len(liste)):
    s=False
    for j in range(len(frekans)):
      if(liste[i]==frekans[j][0]):
        frekans[j][1] = frekans[j][1]+1
        s=True
    if(s==False):
      frekans.append([liste[i],1])
  return frekans


liste = [0,1,7,3,8,1,1,4,0,2]

print(frekans_bul_1_1(liste))
print("\n")
print(frekans_bul_1_2(liste))
print("\n")
print(frekans_bul_2(liste))
