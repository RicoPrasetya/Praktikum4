i=-2
for baris in range(10):
  i=i+1
  for kolom in range(10):
    i=i+1
    if i<10:
      print(i,end='  ')
    elif i>9:
      print(i, end=' ')
  else:
    i=i-10
    print('')
