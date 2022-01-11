kisiler=["ahmet","EL Edhem","cesim"]

blacklist=[]
print(kisiler)

for i in range(4):
 blacklist=input("yeni isimler")

 kisiler.append(blacklist)
 print(kisiler)

uzunluk =len(kisiler)
print("listenini uzunlugu",uzunluk)
print(kisiler[1])

kisiler.pop(-1)
print(kisiler)