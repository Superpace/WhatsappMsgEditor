# -*- coding: utf-8 -*-

ISIM = input("Aramak istediğiniz ismi giriniz : ") #Sohbet ismini seçtik
cumleler = list()
kelimeler = list()

whatsappTxt = open("deneme1.txt","r+",encoding="utf8") 

# Aynı klasörde olan dosyamızı hem okuma hem de yazma olanağı sunan
# W+ modunda açıyoruz
veri=whatsappTxt.read()  
satirlar=veri.split("\n") #veri değişkenini \n lere göre parçalayıp
                          #veriler değişkenine atarız ve veriler değişkeni
                          #artık bir dizi olur

satirlar = [x for x in satirlar if x != ""] # Boş olan satırları yokettik
                         

for i in range(len(satirlar)): #Satırların içinde dolanıyoruz
    try: # Arama yaparken bazen null değerlere rastladığımız için try/except bloğuna aldık
        if satirlar[i][0].isdigit(): # Tarihle başlayıp başlamadığına baktık
                                     # İnsanlar bazen konuşma içinde enter kullanabiliyorlar
            
            if satirlar[i][2] == ".":             #Burada iki haneli ve tek haneli tarihleri ayırdık
                satirlar[i] = satirlar[i][19:]    #Ve bunlara göre satırlarımızı isime kadar kırptık
                                                  #14.02.2020 11:35 - 
            else :
                satirlar[i] = satirlar[i][18:] #1.04.2020 13:45 - 
            if satirlar[i][0:len(ISIM)] == ISIM and satirlar[i][0:len(ISIM)+8] != ISIM+": <Medya" :
                #Önce aradığımız isimdeki satırları bulduk VE 
                #Sonra Medya dahil edilmedi yazılarını seçim dışı bıraktık
                #( Örn: 1.04.2020 13:32 - Batuhan: <Medya )
                cumleler.append(satirlar[i][len(ISIM)+2:]) #İsim kısmını ve : lı kısmı kırparak 
                                                           #asıl cümleyi listeye ekledik
    except:
        pass

for x in range(len(cumleler)): # Cümlelerin içinde geziyoruz
    for y in range(len(cumleler[x].split())): #2. for'u açtık
        if cumleler[x][0:4] != "http" and len(cumleler[x].split()[y])<17 and not cumleler[x].split()[y][0].isdigit():
                 # Eğer bir     link  ve     harf uzunluğu 17 üzeri       ve    kelime diye aldıklarımız bir sayı değilse
            kelimeler.append(cumleler[x].split()[y].lower()) # Kelimeler dizimize ekledik


whatsappTxt.close()
#Son olarak dosyamızı kapatıyoruz
