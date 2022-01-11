sinav_sonuc = {'isimler':['ayse.k','ahmet.m','nuri.c','nawar.t','suzan.t','ala.b'],
               'cinsiyet':['k','e','e','e','k','k'], 'matematik':[60,40,97,45,56,95],
               'turkce':[70,30,23,80,78,46] }
print(sinav_sonuc['isimler'])
print(sinav_sonuc['cinsiyet'])
print(sinav_sonuc['matematik'])
print(sinav_sonuc['turkce'])
def yeni_kayit():
  yeni_isim=[]
  cinsiyeti=[]
  yeni_mat_notu=[]
  yeni_turk_notu=[]
  yeni_isim1=[]
  for i in range(2):
     isim =input("yeni isim giriniz:")
     cinsiyet =input("cinsiyeti giriniz:")
     mat_notu=input("matematik notu gir:")
     turk_notu=input("turkce notu gir:")

     yeni_isim.append(isim)
     cinsiyeti.append(cinsiyet)
     yeni_mat_notu.append(mat_notu)
     yeni_turk_notu.append(turk_notu)

     print(yeni_isim)
     print(cinsiyeti)
     print(yeni_mat_notu)
     print(yeni_turk_notu)
 
     sinav_sonuc['isimler'].append(yeni_isim[i])
     sinav_sonuc['cinsiyet'].append(cinsiyeti[i])
     sinav_sonuc['matematik'].append(yeni_mat_notu[i])
     sinav_sonuc['turkce'].append(yeni_turk_notu[i])

     print(sinav_sonuc['isimler'])
     print(sinav_sonuc['cinsiyet'])
     print(sinav_sonuc['matematik'])
     print(sinav_sonuc['turkce'])

yeni_kayit()
 

