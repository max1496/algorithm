n= input()
flag = True
for k in range(len(n)):
    if n[k]==n[len(n)-k-1]:
      continue
    else:
        flag=False
if(flag):
  print("1")
else:
  print("0")