#!/usr/bin/env python
# coding: utf-8

# In[45]:


#Fonksiyonlar

def karsilastirma(a,b) : 
    if a < b : 
        print(a ,"---> büyüktür <---",b)
    elif b < a :
        print(b , " ---> büyüktür <---",a)
    else:
        return "Sayılar eşittir."    

print(karsilastirma(5,3))

""" yukarıdaki şekilde çalıştırırsak kodumuz çalışır fakat None hatası alırız , hata almak istemiyorsak 
aşağıdaki şekilde yazmamız gerekir kodu """


def karsilastir(a,b) :
    if a < b :
        return str(a) + " ---> büyüktür <--- " + str(b)
    elif a > b : 
        return str(b) + " ---> büyüktür <--- " + str(a)
    else:
        return " sayilar esittir ."
    
    
print(karsilastir(5,3))

""" Yukarıdaki örnek kod da eğer "str" yerine "int" kullansaydık aynı satırda string ifade olduğundan 
ve (+) operatörü kullanıldığından TypeError hatası alırız . """ 


# Sayı karesini alma fonksiyonu 

def kareal (x) :
    return x**2  # ---> x*x şeklinde de gösterebilirdik . 

kareal(10)


sayilar = [*range(1,10)]
print(sayilar ) 
for i in range(len(sayilar)):
    sayilar[i] = kareal(sayilar[i])
    
print(sayilar)

#Bu fonksiyonu daha pratik bir yoldan yapmak için ise "map" kullanırız

sayilar = [*range(1,10)]
[*map(kareal,sayilar)]    # ----> aynı görevde farklı yazılım şekli >> list(map(kareal,sayilar))


# In[57]:


def ciftsayi(x):
    if x % 2  == 0 : 
        return x
    else:
        return "girilen değer tek sayi "

print(ciftsayi(4))

"Yukarıdaki fonksiyonun daha kolay yazılmış hali "

def ciftsay(x):
    return x if x%2==0 else None
ciftsay(4)



#Bu fonksiyonu daha da pratik bir yoldan yapmak için ise "filter" kullanırız 


sayi = [*range(1,6)]
[*filter(ciftsay, sayi)]


# In[59]:


#lambda kullanımı 

list(map(lambda x : x**2 , sayilar )) # ---> or [*map(lambda x : x**2 , sayilar)]


# In[62]:


list(filter(lambda x : x if  x % 2 == 0 else None , sayilar))

# or ---> [*filter(lambda x : x if x %2 == 0 else None , sayilar)]

