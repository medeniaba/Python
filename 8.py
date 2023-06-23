

# try - except ile kodumuzda hata varsa hatanın o kısmını ayıklayıp bize geri döndüren ve kodu çalıştıran bir yapı kurarız . 

def tam_sayi_cevirme():
    girdi = input("Yuvarlama işlemi için bir ondalık sayı giriniz : ")
    try : 
        girdi = float(girdi)
        print('Yuvarlama işleminin sonucu {}'.format(round(girdi)))
    except : 
        print('{} << hatalı karakter << Yuvarlama işleminiz başarısızlıkla sonuçlandı lütfen ondalık bir sayı giriniz !'.format(girdi))
        


# In[30]:


tam_sayi_cevirme()


# In[44]:


# Soruya dogru cevabı verene kadar bize soruyu döndüren bir sonsuz döngüde try - except kuralım 

def tam_sayi_cevirme2():
    
    while True :
        girdi = input("Yuvarlama işlemi için bir ondalık sayı giriniz : ")
        try :
            girdi = float(girdi)
            print('Yuvarlama işleminin sonucu {}'.format(round(girdi)))
            break 
        except : 
            print('{} << hatalı karakter << Yuvarlama işleminiz başarısızlıkla sonuçlandı lütfen ondalık bir sayı giriniz !'.format(girdi))
            pass




tam_sayi_cevirme2()





tam_sayi_cevirme2()





# try - except ile kodumuzda hata varsa hatanın o kısmını ayıklayıp bize geri döndüren ve kodu çalıştıran bir yapı kurarız . 


def tam_sayi ():
    x = (input('Bir ondalık sayi değeri giriniz : '))
    status = ''
    try :
        x = float(x)
        print(' girdiginiz sayıya en yakın tam sayı -->> {} '.format(round(x)))
        status ='İşleminiz başarıyla gerçekleştirildi'
    except:
        print('Hatalı bir değer girdiniz lütfen ondalıklı bir sayı giriniz ')
        status = 'İşleminiz Başarısız'
    finally:
        print(' Tam sayıya çevirme işlemi {} olarak gerçekleştirildi'.format(status))
        
    





tam_sayi()

