"""
Created on Mon Jan  4 20:25:38 2021

@author: Mercan
"""
def tl_cevirici (secim1, secim2, miktar, pariteler):
    if (secim2 == 2):
        carpan = float(pariteler['tl-dolar'])
        sonuc = miktar * carpan
        print (sonuc)
    elif (secim2 == 3):
        carpan = float(pariteler['tl-euro'])
        sonuc = miktar * carpan
        print (sonuc)
    elif (secim2 == 4):
        carpan = float(pariteler['tl-sterlin'])
        sonuc = miktar * carpan
        print (sonuc)
    else :
        print("Geçersiz seçim !")

            
def dolar_cevirici (secim1, secim2, miktar, pariteler):
    if (secim2 == 1):
        carpan = float(pariteler['tl-dolar'])
        sonuc = miktar / carpan
        print (sonuc)
    elif (secim2 == 3):
        carpan = float(pariteler['dolar-euro'])
        sonuc = miktar * carpan
        print (sonuc)
    elif (secim2 == 4):
        carpan = float(pariteler['dolar-sterlin'])
        sonuc = miktar * carpan
        print (sonuc)
    else :
        print("Geçersiz seçim !")

def euro_cevirici (secim1, secim2, miktar, pariteler):
    if (secim2 == 1):
        carpan = float(pariteler['tl-euro'])
        sonuc = miktar / carpan
        print (sonuc)
    elif (secim2 == 2):
        carpan = float(pariteler['dolar-euro'])
        sonuc = miktar / carpan
        print (sonuc)
    elif (secim2 == 4):
        carpan = float(pariteler['euro-sterlin'])
        sonuc = miktar * carpan
        print (sonuc)
    else :
        print("Geçersiz seçim !")
        
def sterlin_cevirici (secim1, secim2, miktar, pariteler):
    if (secim2 == 1):
        carpan = float(pariteler['tl-sterlin'])
        sonuc = miktar / carpan
        print (sonuc)
    elif (secim2 == 2):
        carpan = float(pariteler['dolar-sterlin'])
        sonuc = miktar / carpan
        print (sonuc)
    elif (secim2 == 3):
        carpan = float(pariteler['euro-sterlin'])
        sonuc = miktar / carpan
        print (sonuc)
    else :
        print("Geçersiz seçim !")


pariteler = {'tl-dolar': 0.14,
             'tl-euro': 0.11,
             'tl-sterlin': 0.10,
             'dolar-euro': 0.80,
             'dolar-sterlin': 0.75,
             'euro-sterlin': 0.90}
print("""
      Parabirimi Çeviri Programına Hoş Geldiniz.
      Programda TL, Dolar, Euro ve Sterlin para birimlerini kullanabilirsiniz.
      TL        -->>    1
      Dolar     -->>    2
      Euro      -->>    3
      Sterlin   -->>    4
      """)

secim1 = int(input("Elinizde bulunan para birimini seçiniz: "))
miktar = int(input("Elinizde bulunan para miktarını giriniz: "))
secim2 = int(input("Hangi para birimine çevireceğinizi seçiniz: "))


if (secim1 == 1):
    tl_cevirici(secim1, secim2, miktar, pariteler)
elif (secim1 == 2):
    dolar_cevirici(secim1, secim2, miktar, pariteler)
elif (secim1 == 3):
    euro_cevirici(secim1, secim2, miktar, pariteler)
elif (secim1 == 4):
    sterlin_cevirici(secim1, secim2, miktar, pariteler)
else :
    print("Tanımlanmayan seçim...")
