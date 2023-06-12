import xml.etree.ElementTree as ET
tree = ET.parse('stok_hareketleri_kisa.xml')
root = tree.getroot()
list = []

def getList():
    for str in root:
        list.append(dict(status      = str[0].text,
                        fyear        = str[1].text,
                        fmon         = str[2].text,
                        evrak_tarihi = str[3].text,
                        rec_id       = str[4].text,
                        cari_kod     = str[5].text,
                        urun_kodu    = str[6].text,
                        urun_grubu   = str[7].text,
                        miktar       = str[8].text))
    return list

kisi = "16925"

def faturalar(id):
    innerlist = getList()
    #kişinin faturalarını döndürür
    if(len(innerlist)==0):
        print("Satis islemlerinde bulunamadi.")

    fatura_ids =[]
    for i in innerlist:
        if(i["cari_kod"]==id and i["rec_id"] not in fatura_ids):
            fatura_ids.append(i["rec_id"])

    return fatura_ids


def fatura_icerik(fatura_id):
    innerlist = getList()
    #Fatura İçeriğini Döndürür
    urun_ids =[]
    for i in innerlist:
        if(i["rec_id"]==fatura_id):
            if(i["urun_kodu"] not in urun_ids and i["urun_kodu"] != None):
                urun_ids.append(i["urun_kodu"])
    if(len(urun_ids)==0):
        print("İçerik Bulunamadı")
    return urun_ids





    #env/Scripts/activate.ps1
    #set FLASK_ENV=development
    #flask run

