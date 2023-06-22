

"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] 
gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

"""



a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


flatten_list = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)  # İç içe geçmiş listeler için tekrarlayan çağrı yapılır
        else:
            flatten_list.append(item)

flatten(a)
print(flatten_list)





""""
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da 
liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

"""



def tersine_cevir(liste):
    ters_liste = []
    for eleman in liste[::-1]:
        if isinstance(eleman, list):
            ters_liste.append(tersine_cevir(eleman))
        else:
            ters_liste.append(eleman)
    return ters_liste

# Örnek kullanım
input_liste = [[1, 2], [3, 4], [5, 6, 7]]
output_liste = tersine_cevir(input_liste)
print(output_liste)

