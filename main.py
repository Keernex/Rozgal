q = int(input())
w = int(input())
print("+: 1, -: 2,Середне арифметичне: 3, *: 4")
e = int(input("Введіть від 1 до 4:"))
if e == 1:
  print(q + w)
if e == 2:
  print(q - w)
if e == 3:
  print((q + w) / 2)
if e == 4:
  print(q * w)
