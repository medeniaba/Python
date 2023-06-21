

"""" Klavyeden girilen ifadenin tek mi çift mi olduğunu kullanıcıya soran ve daha sonra
kullanıcıya tek mi cift mi oldugunu söyleyen program """

def program():
    
    
    girdi = input('Bir sayı giriniz lütfen : ')
    islem = input("Sayının tek mi veya cift mi olduğunu sorgulamak için tek veya cift yazınız : ")


    if islem =='cift':
        if int(girdi) % 2 == 0 : 
            return "girilen {} sayisi cifttir".format(girdi)
        
        else :
            return "girilen {} sayisi cift değildir".format(girdi)

    elif islem =='tek':
        if int(girdi) %2 == 1 : 
            
            return "girilen {} sayisi tektir .".format(girdi)
        
        else :
               
            return  "girilen {} sayisi tek degildir".format(girdi)
        

program()          

