sinav_sonuc = {'names':['ayse.k','ahmet.m','nuri.c','nawar.t','suzan.t','ala.b'],
               'cinsiyet':['k','e','e','e','k','k'], 'matematik':[60,40,97,45,56,95],
               'turkce':[70,30,23,80,78,46] }
print(sinav_sonuc['names'])
print(sinav_sonuc['cinsiyet'])
print(sinav_sonuc['matematik'])
print(sinav_sonuc['turkce'])
def yeni_kayit():
  new_name=[]
  nationality=[]
  new_math_pouan=[]
  new_turkce_pouan=[]
  new_name1=[]
  for i in range(2):
     isim =input("yeni isim giriniz:")
     cinsiyet =input("nationality giriniz:")
     math_poun=input("matematik notu gir:")
     turkce_poun=input("turkce notu gir:")

     new_name.append(isim)
     nationality.append(cinsiyet)
     new_math_pouan.append(math_poun)
     new_turkce_pouan.append(turkce_poun)

     print(new_name)
     print(nationality)
     print(new_math_pouan)
     print(new_turkce_pouan)
 
     sinav_sonuc['names'].append(new_name[i])
     sinav_sonuc['cinsiyet'].append(nationality[i])
     sinav_sonuc['matematik'].append(new_math_pouan[i])
     sinav_sonuc['turkce'].append(new_turkce_pouan[i])

     print(sinav_sonuc['names'])
     print(sinav_sonuc['cinsiyet'])
     print(sinav_sonuc['matematik'])
     print(sinav_sonuc['turkce'])

yeni_kayit()
 

