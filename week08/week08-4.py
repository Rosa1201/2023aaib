a = [3,0,1,8,7,2,5,4,6,9]
N = len(a)
print(a)
for i in range(1,N):
  if a[i] < a[i-1]:
    a[i], a[i-1] = a[i-1], a[i]
print(a)