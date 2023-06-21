


#Enumerated'i for kısmına yazdıgımızda output çıktının index sırasını yazdırmaya yarar .

adlar = ['Tyler','Blake','Copy','Cameron']
for e in adlar : 
    print(e)





for i,e in enumerate(adlar):
    print(i,"indisinde --> ",  e)





for i , e in enumerate(adlar , start = 1):
    print(i , " . lokasyonunda bulunan eleman:",e )




# zip() 2 farklı listeyi birşeltirmeye yarayan bir fonksiyondur 

keys = ['isim','soyad','ülke','is']
values = ['Deniz','Ötekıvılcım','Azerbaycan','Nİkah Memuru']
d ={}

for k,v in zip(keys,values):
    
    d[k] = v 

d    




#Exercies 3 

a = [] and 2 
print(not a)






