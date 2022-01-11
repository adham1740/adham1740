
sinif_listesi = {'isimler':['AHMET','CANAN','ESMA','MUHAMMET','AYSE'],
'cinsiyet':['E','K','K','E','K'],
'matematik':[78,45,17,56,63],
'turkce':[86,72,53,70,89]}
print(sinif_listesi['isimler'])
print(sinif_listesi['cinsiyet'])
print(sinif_listesi['matematik'])
print(sinif_listesi['turkce'])
#Listeyi Kontrol Ettim.
kizlarin_turkce_notlari = []
erkeklerin_turkce_notlari = []
count_k = 0
count_e = 0
k_mat = 0
e_mat = 0
k_turk = 0
e_turk = 0
for x in range(len(sinif_listesi['cinsiyet'])):
    if sinif_listesi['cinsiyet'][x] == 'K':
        count_k +=1
        k_mat = k_mat + sinif_listesi['matematik'][x]
        k_turk = k_turk + sinif_listesi['turkce'][x]
        kizlarin_turkce_notlari.append(sinif_listesi['turkce'][x])
    else :
        count_e += 1
        e_mat = e_mat + sinif_listesi['matematik'][x]
        e_turk = e_turk + sinif_listesi['turkce'][x]
        erkeklerin_turkce_notlari.append(sinif_listesi['turkce'][x])
print(f"Erkek Matatematik Ortalamasi: {e_mat/count_e}\n\
Kizlarin Matematik Ortalamasi: {k_mat/count_k}\n\
Turkce Dersin Ortalamasi : {(k_turk + e_turk)/(count_e + count_k)}")
print("kizlarin En Yuksek Turkce Notu : ", max(kizlarin_turkce_notlari))
print("Erkeklerin En Yuksek Turkce Notu : ", max(erkeklerin_turkce_notlari))