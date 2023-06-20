#!/usr/bin/env python
# coding: utf-8

# In[15]:


#excercies-1-

a , b = 20 , 50 
b , a = 60 , 30 

print((a*b/b))


# In[23]:


#excercies-2-

a = [2,3,4]
b = []

b = a.copy()
b.append(6)
b = a.pop()

print(b)
print(a)




# In[22]:


#TEK satırda for döngüsünü kullanarak işlem yaptırma ' List Comprehension '
squares = []
squares = [ i * i for i in range(1,11)]
squares

