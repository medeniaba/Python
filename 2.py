#!/usr/bin/env python
# coding: utf-8

# In[83]:


# List Comprehension in conditional

#Normaly For

list = [1 , 44 , 55 , 10 , 25 , 40 , 25]
add = []

for i in list : 
    if i % 2 == 1 :
     add.append(i)
print(add)    


#List Comprehension for 

add = [ i for i in list if i % 2 == 1 ]
add


# In[84]:


#Easy For 
def kosul (x) :
    
    if  x % 2  == 0 : 
        return True
   
    else: 
        return False
    

add = [x for x in list if kosul(x)]

add


#Set'ler out da sadece degeri bir kere yazar ! 

#Nested List Comprehension ↓ ↓ iç içe 2 for gibi düşünebiliriz yapısı şu şekilde ; 

m = [[i for i in range (5)]for i in range(6)]
print(m)



# In[85]:


# İç içe 2 forla bir listenin elemanı içerisinde dağınık listeler şeklinde bulunan bir -
# listeyi başak bir listeye düzenli ve tek parça atmak 

m = [[10,11,12],[13,14,15],[16,17,18]]

for i in m : 
    print(i)



# In[115]:


yeni = []
for i in m :
    print(i)

    for j in yeni :
              
        yeni.append(j)
        print(j)
        


# In[ ]:




