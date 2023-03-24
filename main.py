q = int(input())
w = int(input())
r = int(input())
print("max: 1, min: 2, cer: 3")
e = int(input("Введіть від 1 до 3:"))
if e == 1:
  if q >= w and q >= r:
    print(q)
  elif w >= q and w >= r:
    print(w)
  else:
    print(r)
if e == 2:
  if q <= w and q <= r:
    print(q)
  elif w <= q and w <= r:
    print(w)
  else:
    print(r)
if e == 3:
  print((q+w+r)/3)