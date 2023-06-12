import xml.etree.ElementTree as ET
urun_tree = ET.parse('urun.xml')
urun_root = urun_tree.getroot()
urun_list = []
import getdata as g
import json

for stri in urun_root:
    urun_list.append(dict(urun_kodu  = stri[0].text,
                    urun_grubu  = stri[1].text,
                    urun_fiyati = stri[2].text))

stok_tree = ET.parse('stok_hareketleri_kisa.xml')
stok_root = stok_tree.getroot()
stok_list = []
for stri in stok_root:
    stok_list.append(dict(status      = stri[0].text,
                        fyear        = stri[1].text,
                        fmon         = stri[2].text,
                        evrak_tarihi = stri[3].text,
                        rec_id       = stri[4].text,
                        cari_kod     = stri[5].text,
                        urun_kodu    = stri[6].text,
                        urun_grubu   = stri[7].text,
                        miktar       = stri[8].text))


def en_son_satin_alinan_20(id):
    kisi_satin_alinan = []
    for i in stok_list:
        if i['cari_kod']== str(id):
            kisi_satin_alinan.append(i)
    kisi_satin_alinan.sort(key = lambda x:x['evrak_tarihi'])
    kisi_satin_alinan.reverse()
    last_20 = []
    if len(kisi_satin_alinan)<20:
        for i in kisi_satin_alinan:
            last_20.append(i['urun_kodu'])
    else:
        for i in range(0,20):
            last_20.append(kisi_satin_alinan[i]['urun_kodu'])
    return last_20



def en_cok_satilan_20():
    toplam_satis = []
    most_20 = []
    for urun in urun_list:
        miktar = 0
        for i in stok_list:
            if i["urun_kodu"] == urun["urun_kodu"] :
               miktar += int(i["miktar"])
        toplam_satis.append(dict(urun_kodu = urun["urun_kodu"],satis_mik = miktar))
    
    toplam_satis.sort(key = lambda x:x['satis_mik'])
    toplam_satis.reverse()
    for i in range (20):
        most_20.append(toplam_satis[i]['urun_kodu'])
    return most_20

def tum_urunler():
    list = []
    for urun in urun_list:
        list.append(urun['urun_kodu']+"+"+urun['urun_fiyati'])
    return list


def clients_Most_Purchased_Items(id):
    #müşterinin en çok aldığı 20 ürünü tespit eder ve sıralar.
    encok=[]
    liste =[]
    urun_liste =[]
    for i in stok_list:
        if i['cari_kod'] == id:
            if i['urun_kodu'] not in urun_liste:
                liste.append(dict(urun_kodu = i['urun_kodu'], miktar = int(i['miktar']) ))
                urun_liste.append(i['urun_kodu'])
            else:
                for j in liste:
                    if j['urun_kodu'] == i['urun_kodu']:
                        j['miktar'] = j['miktar']+int(i['miktar'])
    liste.sort(key = lambda x:x['miktar'],reverse=True)
    if len(liste)<20:
        for i in liste:
            encok.append(i['urun_kodu'])
    else:
        for i in range (20):
            encok.append(liste[i]['urun_kodu'])

    return encok


def clients_Least_Purchased_Items(id):
    #müşterinin en az aldığı 20 ürünü tespit eder ve sıralar.
    enaz=[]
    liste =[]
    urun_liste =[]
    for i in stok_list:
        if i['cari_kod'] == id:
            if i['urun_kodu'] not in urun_liste:
                liste.append(dict(urun_kodu = i['urun_kodu'], miktar = int(i['miktar']) ))
                urun_liste.append(i['urun_kodu'])
            else:
                for j in liste:
                    if j['urun_kodu'] == i['urun_kodu']:
                        j['miktar'] = j['miktar']+int(i['miktar'])
    liste.sort(key = lambda x:x['miktar'])
    
    if len(liste)<20:
        for i in liste:
            enaz.append(i['urun_kodu'])
    else:
        for i in range (20):
            enaz.append(liste[i]['urun_kodu'])
    return enaz

users_tree = ET.parse('users.xml')
users_root = users_tree.getroot()
users_list = []

for stri in users_root:
    users_list.append(dict(user=stri[0].text,password=stri[1].text,price_factor=stri[2]))
def get_pf(user_id):
    for i in users_list:
        if i['user'] == user_id :
            return i["price_factor"].text
        
    