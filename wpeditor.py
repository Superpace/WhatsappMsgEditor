
ISIM = "Batuhan" #Sohbet ismini seçtik
whatsappTxt = open("deneme1.txt","r+",encoding="utf8") 
cumleler = list()
kelimeler = list()
# Aynı klasörde olan dosyamızı hem okuma hem de yazma olanağı sunan
# W+ modunda açıyoruz
veri=whatsappTxt.read()
satirlar=veri.split("\n") #veri değişkenindeki \n lere göre parçalayıp
                         #veriler değişkenine atar ve veriler değişkeni
                         #artık dizi olur
                         
for i in range(len(satirlar)): #Sat�rlar�n i�inde dolan�yoruz
   
    if satirlar[2] == ".":             #Burada iki haneli ve tek haneli tarihleri ay�rd�k
        satirlar[i] = satirlar[i][19:] #Ve bunlara g�re sat�rlar�m�z� isime kadar k�rpt�k
                                       #14.02.2020 11:35 - 
    else :
        satirlar[i] = satirlar[i][18:] #1.04.2020 13:45 - 
    
    if satirlar[i][0:len(ISIM)] == ISIM and satirlar[i][0:len(ISIM)+8] != ISIM+": <Medya" :
        #�nce arad���m�z isimdeki sat�rlar� bulduk VE 
        #Sonra Medya dahil edilmedi yaz�lar�n� se�im d��� b�rakt�k
        #( �rn: 1.04.2020 13:32 - Batuhan: <Medya )
        cumleler.append(satirlar[i][len(ISIM)+2:]) #�sim k�sm�n� ve : l� k�sm� k�rparak 
                                                   #as�l c�mleyi listeye ekledik
            
for x in range(len(cumleler)): # C�mlelerin i�inde geziyoruz
    for y in range(len(cumleler[x].split())): #2. 
        if cumleler[x][0:4] != "http" and len(cumleler[x].split()[y])<17 and not cumleler[x].split(" ")[y][0].isdigit():
            kelimeler.append(cumleler[x].split(" ")[y].lower())


whatsappTxt.close()
#Son olarak dosyam�z� kapat�yoruz