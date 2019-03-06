# n inci fibonacci sayısını döndüren fonksiyon
def fibonacci(n):
  a=0
  b=1
  for i in range(n-1):
    a=b
    b=a+b
  return a

# n inci fibonacci sayısını recursive döndüren fonksiyon
def recursive_fibonacci(n):
  if(n<2):
    return n
  else:
    return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

# n sayısının faktoriyelini döndüren fonksiyon
def factorial(n):
  s=1
  for i in range(1,n+1):
    s=s*i
  return s

# n sayısının faktoriyelini recursive döndüren fonksiyon
def recursive_factorial(n):
  if(n==1):
    return n
  else:
    return n*recursive_factorial(n-1)

# m nin n inci kuvvetini döndüren fonksiyon
def power(m,n):
  s=m
  pow_sayac=0
  for i in range(1,n):
    pow_sayac=pow_sayac+1
    s=s*m
  return s

# m nin n inci kuvvetini recursive döndüren fonksiyon
def recursive_power(m,n):
  rec_pow_sayac=0
  rec_pow_sayac=rec_pow_sayac+1
  if(n==0):
    return 1
  elif(n==1):
    return m
  elif(n%2==0):
    return recursive_power(m*m,int(n/2))
  elif(n%2!=0):
    return recursive_power(m*m,int(n/2))*m

print("\nfibonacci = ",fibonacci(5),"\n")
print("recursive_fibonacci = ",recursive_fibonacci(5),"\n")
print("factorial = ",factorial(5),"\n")
print("recursive_factorial = ",recursive_factorial(5),"\n")
print("Power = ",power(5,3),"\n")
print("recursive_Power = ",recursive_power(5,3),"\n")
