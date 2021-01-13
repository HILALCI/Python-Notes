"""

                                                                        PYTHON DERS NOTLARI      



Bu kodlar pyhton v3 icindir.Diger surumlerde farklilik gosterebilir.
!!!!!!   Jython,Cython farkli dilleride destekliyor ayrinti icin https://en.wikipedia.org/wiki/Python_(programming_language) bakmayi unutma !!!!!!!
"""
"""
https://www.python.org/ #Kurulum yapmak icin python resmi web sitesinden indirebilirsiniz.
https://docs.python.org/3/  #Bu siteden dokumanlara ulasabilirsiniz.Ayni zamada arama yaparak yine sizlere asagidaki pydoc sorgulara alternatif bir sorgu yapabilirsiniz iyi hazirlanmis bir dokumandir.
https://docs.python.org/3/tutorial/index.html #Python kendi tutorial'dir.Yine guzel hazirlanmis yine bu tutorial'a bakabilirsiniz.
"""

""" Dokuman yazilari icin kullanilir.""" #help() metodu kullanildiginda yorumlar gozukur.
''' Buda cok satirli yorum icin kullaniliyor.''' #Multi line comment'tir yukaridaki ile benzer sekilde belirtilen alan icerisi yorumdur.Alanin disindaki kodlarlar calistirilir.Alanin icindekiler atlanir.
#Bu tek satir yorumdu (single line comment) #Satir bittiginde yine sonraki satirdaki kod calisir.Fakat satir bitene kadar yorumdur bu yorumlar calisirken atlanir.Hata ayiklama icin kullanabilirsin.
## #Bu  sekilde de gordum fakat farklarını bilmiyorum.
python -m pydoc #cmd calistirdiginda metadocumentation calistirir.
python -m pydoc math #Kutuphane veya methodlarin  ismini direkt yazabilirsin.
python -m pydoc -k ssl # -k keyword arastirmasi yapmak icin ekleniyor bu sayede konu ile alakali method ve kutuphaneler gosteriyor.
python -m pydoc setuptools.ssl_support #Fakat ayrinti bakmak icin -k yazmadan  yaziyoruz.
python -m pydoc -p 1000 #-p port kisaltmasi istenilen portta daha sonra b enter ladigimizda browserdan lazilan portta dokumantasyon aciliyor.
python -m pydoc -b #Yukarida port girmistik burada portu kendi ayarliyor browserda dokumantasyon aciyor. !!!! Fakat her ikisindede q enter layip islemleri bitirmen lazim server acık kalir. !!!!
python -m pydoc -w json #-w write islemi icin ilgili dosyada bir html dokumantasyon olusturuyor bu ornekte json alakali bir dokumantasyon yazilacak.
pyhton dosyaadi.py  #cmd de PYTHON codelari calistirliyor.
#Kutuphane ve modulleri arastirmak icin dir() ve help() fonksiyonlarini kullanabilirsin.Fakat bazi kutuphaneleri veya methodlari sorgulamadan once importlamaniz gerekir. 
import math #math kutuphanesi kullanmak icin import etmemiz gerekiyor.
help(math) #Bu sorguyla yine math kutuphanesi hakkinda bilgi edinebiliriz.
dir(math) #math kutuphanesindeki methodlari gormek icin kullanabiliriz.
print(dir(math)) #Python shell sorgulama yapiliyor dir() fakat bu sekilde ekrana yazdirabilir.
help(math.log2) #Bu setilde math kutuphanesindeki log2 methodu hakinnda bilgi icin bu sekiyde yazilabilir.Bunu diger methodlarda da ve dir() icin de yapabiliriz.
from math import * #Alt satirdada goruldugu gibi math. gosteriminden kurtulmak icin bu sekilde import etmeliyiz.
help(log2)
#Sunu yapabilirsiniz shell yazildiginda calisiyorsa print() islemini unutmussunuz demektir. !!!  Bazi kodlarda  print yazmamis olabilirim siz eger bu durumu yasarsaniz print() ekleyin. !!!

python #Console sadece python yazarsak python shell calisiyor ve dosyadan degil direkt olarak yine python kodlari yazip calistirabiliriz.
exit() #Python Shell cikmak icin kullanilir.
python calistir.py #Tek bir surum varsa v3 de olsa calistirinca hata veriyor bu sekilde calistiriniz.
python3 calistir.py #Console ile calistrimak icin python yazarsak python v2 calistiriliyor. v3 icin python3 kullaniyoruz.

#Hello World
print("Hello World") #Ekrana yazdirma islemi yapmak icin adettendir ilk yazilan kod Hello Worlddur.
ad = input("Lutfen Adinizi  Giriniz: ") #Girdi islemi icin input() kullaniriz.
print(ad) #Su bir on tanim yapiyoruz bazi islemler icin simdilik bilmeniz icin.
türkçeYazı = "Bu utf-8 test etmek içindir."
print(türkçeYazı)#Python v3 ile utf-8 destekliyor.Kodlarimizda utf-8 encoding eklenmesine gerek kalmadan kullanabilir.

#Operator : Burda bazi matematiksel operatorleri ele aldik sonradan yine operatorler anlatilmaya devm edecek.
s=2 # = Matematikteki gibi denklik icin degil atama(assignment) islemi icin kullanilir.Esitlik kontrolunu == ile yapiyoruz.Esit olmadigi durumu != (not equal) bu yuzden esitlik hep sonra yazilir.
a=3 #Degiskenleri isledigimizde bircok tipte atama yapildigini gosterecegiz.
s *= 1  #Islemden sonra = getirldiginde once islem yapiliyor sonra atama yapiliyor.  
s += 1  #Matematiksel olarak yaptigimiz tum islemlerle yine ayni formda islemler yapilabilir. /= , %= ...
S ** 3  #Us alma islemi iki tane carpma ** ile yapilir.
s**0.5  #Karekok icin 0.5 
s**(1/3) #Kupkok icin parantezli 1/3 yapilir
x % y  #Kalan Bulmak icin % kullanilir.Mod operatorudur.Matematikteki gosterimi x mod y dir.
a // s  #Kalnsiz degerli tam bolme islemi icin // kullanilir.Virgulden sonrasini gostermez.Katsayıyı bulur.
21//5 #Bu islemi yaptigimizda sonucu ekrana yazdigimizda 4 yazar.Yani 21 bolunen , 5 bolen ,4 bolum , 1 kalan  yani bu islemle bolumu buluruz.

#Variable
import keyword
print(keyword.kwlist) #Reserved keywords yani onceden tanimli olan kelimeleri yazdirmak icin bu iki satiri kullaniyoruz.
#Degisken tanimlarken reserved keywords verilmiyor ayni zamanda _ haricinde operatorler yazilmiyor.Bu karisiklik olmamasi icin bu sekilde tasarlanmis.Sayiyla basliyamaz fakat sonradan sayi yazilabilir.
#Degiskenler genelde kucuk harfle baslar bu genel yazim kulturunde boyledir.Bir baska yazim kulturude ilk kelimeden sonraki ilk harf buyuk yazilir.Virgulden sonra bir satir bosluk yazilir.Daha bircok yazim kultur vardir arastirabilirsiniz.Fakat bunlari yapip yapmamak size kalmis ben bir standart olmasi icin kulture uyuyorum.

He= 'Salih'
Yo= 'Taze'  
He+" "+Yo   #Bu islem gibi carpma da  yapilabilir.Yazilari birbirine eklemek icin.He+Yo= 'Salih Taze' olarak gozukecek." " bosluk icin eger eklemessek bitisik yazar.
s= flout(s) #Bu islem tam sayiyi ondalikli sayiya donusturuyor.Tip donusumudur(Typecasting).  
int (5.5)   #Bu islemde ondalikli sayiyi tam sayiya donusturuyor. 
str (112)   #Bu islem sayiyi string e donusturuyor.Onu bir karakter gibi algiliyor
x = "258963247"
int (x)     #Stringe bir tam sayiya ceviriyor.
x= "35.14"
str (x)     #Stringe bir ondalikli sayiya ceviriyor.Yukaridaki duzeltme ancak ondalikli ise ondalikli sayiya cevrilebilir.Tam sayiyiyida cevirir.
j == i #Pythonda kok -1 degeri olan i degeri j ile gosterilir.
a= 3+5j
print(a.real) #Real kismini ekrana yazdirmak istersek.Ornege gore 3.0 yazcak.
print(a.imag) #Imaginer kismi yazdirmak icin kullaniyoruz.Ornege gore 5.0 yazacak.
type(a) # Sorguyu attigimizda bu <class 'complex'> sekilde cikar yani tipi komplextir.int float degil farklidir.
#Complex sayilari float a ceviremessin hata cverir.
a=100
complex(a) #Complex tihine donusturmek icin sonuc  (100+0j) bu sekilde cikar.
hex(x) # int girilen sayiyi Hexadecimal civirir.
a=None #Degeri daha belirlenmemis degisken olarak belirtilir.
a = True #Boolean deger buyuk harfle ilk basliyor.C de kucuk harfle true yanlis yazilmasin pyhton True veya False olarak yaziliyor.

liste= ["Merhaba",3.14,...] #listeleme stringlerden farki degistirilebilmesi 
liste=list() #Bos bir liste olusturur.
len(liste) #Bu komut listenin kac elemani oldugunu gosterir.
list[1] #Bu komutla ikinci elemani gostermis oluruz.Sirlama 0 dan baslar.
list[-1] #Son elemani getirir.
list(::-1) #Listeyi sondan basa sirala.
liste1+liste2 #Birlesim kumesi mantigi oluyor.
liste[1]= 2 #Bu ikinci elemanin yerine yazilan karakterle degistiriyor.
liste[:2] #Bu 3. elemana degil liste elemaninda 2`ye kadar al demek.Ornek list=[1,2,3,4,5]  olsun cikan deger [1,2] olacak
liste[3:] #Bu liste elemaninda 3`e kadar al.
liste[:2]= [6,8] #Elemani degisecek Ornekteki gibi cikan liste [6,8,3,4,5] olacak.
liste.append("Salih") #Bu komut listeye eleman ekler.
liste= [11,5,6,7,8,9,4,5,6]
liste += [1,2,3,100] #append gibi elemanlari boylede ekleyebilirsin.Sonuc [11, 5, 6, 7, 8, 9, 4, 5, 6, 1, 2, 3, 100] olcak.
liste.pop() #Bu kodla parantez bossa son elemani listeden siler.
liste.pop(x) # x. elemani siler.
liste.sort() #Sirlamaya yariyor kucukten buyuge dogru sayilari siralar.Kelimeleri alafabeye gore sirlar.
liste.sort(reverse = True) #Buyukten kucuge sirlar reverse tende anlasilabilecegi gibi.
list[0][0] #Ic ice listelenlerde 1. elmanin 1. elemanini gosterir.
liste.insert(2,"Salih'in listesi") #İlk eklenecek sira 2 elemandan sonra ne eklemek istiyorsak onu yapiyoruz.str de sayida girilebilir.
liste.remove(x) #Listeden x bulup siliyor.Eger birden fazlaysa ilk buldugunu siliyor digeri kaliyor dikkat!
liste.index(x) #Listede x kacinci elamda oldugunu bulur.
liste.count(x) #Listede x kac tane varsa gosterir.
liste.extend(liste2) #Listeleri birlestirir eleman olarak.append tek 1 eleman olarak ekler yani l1.extend(l2)=[1,2,3,4,5,6] --- l1.append(l2)=[1,2,3,[4,5,6]] farki bu
liste.clear() #Listedeki tum elemanlari siler.
liste=liste2.copy()  #Listeyi kopyalar ama deep copy(Derin copyalama) yapıyor 2 olan degisiklik 1 etkilemiyecek. l1=l2 dersek shadow copy(Sig kopyalama) degisiiklikler ikisinide etkileyecek.
liste.reverse() #Adindanda anlasilacagi gibi liste tersten beslatip siralar.
del(liste[x]) #listenin x elemanini siler
demet=(1,1,2,3) #Listeden farki bu degerler degismeyez yani immutable 'dir. Tuple olarak adlandirilirlar.
demet.count(1)  #Demet kac kere 1 gectigini gosterir.
demet.index(3)  #Elemanin sirasini gosteriyor.
demet =(10,11,12,14,15)
demet +=(1,2,3,4,5) #Listede oldugu gibi sonuc (10, 11, 12, 14, 15, 1, 2, 3, 4, 5) olacak.
tuple=([1,2,3],[4,5,7])
tuple[0][2]=1  #tuple degismez fakat biz listeyi degistirdik tuple[0]=[1,1,2,3,1] deseydik hata alacaktik.
t= 1,2,3 #Boyle yapsak tuple olarak kaydedecektir.
print(sorted(demet)) #Demet ve tuplelari sortla siralayamiyoruz bu nedenle sorted kullandik. 
print(sorted(demet,reverse = True)) #Tersten siralamak icin.
kume={1,2,3,4,5} #Bu gösterim kümeler yani set olarak adlandiriliyor.
kume={1,1,1,2,2,3,4,5} #Boyle yazilmis olsa bile yukaridaki gibi ayni elemandan bir tane olacak sekilde sirasi onemsiz olarak gosterir printle.
kume= set(liste) # set ile listeyi,tuple,stringleride kumeye cevirebiliriz.
kume.add(x) #Kumeye eleman ekliyoruz.
kume.discard(x) #Kumeden elemani siler.
#kume += {1,2,3,4} boyle bir islemde hata verir.
print(sorted(kume)) #Kume ve setleride ayni sekilde sortedla siraliyoruz.
print(sorted(kume, reverse = True)) #Tersten siralamak icin.
k1=set("bilgisayarkavramlari")
k2=set("salihtaze")
print(k1|k2) # k1 V k2 birlesimini aliyor. or operatoru yani veya.Fakat bu operatorlerde sira onemli
k1.union(k2) # Yukaridaki ayni islem
k1.update(k2) #Birlesimi k1 atar.
print(k1-k2) # k1 - k2 yani k1 / k2 farkini aliyor.
k1.difference(k2) #Yukaridaki ile ayni islemdir.
k1.difference_update(k2) #Farkini alip k1 elemanini farktan cikanla degistiriyor.
print(k1&k2) # k1 ˄ k2 kesisimini aliyor. and operatoru yani  ve
k1.intersection(k2) #Yukaridaki ayni islemi yapar.
k1.intersection_update(k2) #Kesisimi  alip  elemanini kesimden cikanla degistiriyor.
k1.isdisjoint(k2) #Ayrik kume ise kesisimleri yoksa true degilse false doner.
k1.issubset(k2) # k1 k2 nin alt kumesi ise true degilse false
print(k1^k2) # k1 _V_ k2 yada yani exclusive or  dur.
sozluk={"bir":1} #Tanimlama ve karsliginda ne olacagini gostermesi icin.
sozluk["bir":]   #Demetteki elemani gostermek icin tanima karlilik olarak 1 gostercek. key : value 
sozluk["iki"] =2 #Tanim ve deger eklemek icin.
sozluk["bir"]=10 #Karsilik gelen degeri degistiriz ve 10 olur.
sozluk.keys() #Sadece tanimlari
sozluk.values() #Sadece karsilik gelen degerleri gosteri.
sozluk.items() #Tanim ve karsligini ikisini bir gosterir.
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) #dict ile listeyi dictionarie cevirebiliriz. (key,value)
for k, v in sozluk.items(): #Anahtar ve degeri yazdirmak icin 
    print(k,v)
for i, v in enumerate(['tic', 'tac', 'toe']): #index ve deger bastirmak icin. 
    print(i, v)
x in liste #Girilen degerin listede olup olmadigini kontrol ediyor sonucunda Trua , False dondurur.Sadece listede degil demetlerde yapilabiliyor.
from collections import deque
liste2=deque([3,2,5,4,6]) #Bu sekilde listeyi  queue seklinde kaydediyor.
print(liste2)
liste2.popleft() #Bu islem pop(0) ayni fakat stackte LIFO (Last In First Out), queue FIFO (First In First Out) oldugundan kuyrugun basindan elemani cikarmamiz gerekiyor.
print(liste2)

sorted("Python Ogreniyorum") #Stringleride siralayabiliriz.
sorted("150486") #int oldugunda hata veriyor yine string olmali.

#Output : Cikti islemleri icin kullaniyoruz.Default olarak ekrana cikti veriyor.
print(Salih Yazilim Ogreniyor)  #Ekrana yazdirma komutudur.
print(Salih,Ingilizce,"Konusur",11)  #Ekrana birden fazla karakter bastirmak icin virgulle ayrilir.Yazilinca aralarinda bosluk olur
print(Salih\nYazilim\nProgramlar)    #Ekrana yazdirirken alt alta yazdirir.
print(Salih\tKitap\tOkur)            #Ekrana yazdirirken yan yan aralarinda 4 satir bosluklu yazadirir.
type(3.14)  #Parantez icindekinin hangi tur oldugunu gosterir.Ornekte ondalik{float} olarak gosterir.
print(01,01,1974, sep = "/")           #Ekrana yazilirken bosluk olan yere sep = "" degerin icine ne yazdiysak aralarinda o olacak.
print(Salih,Ingilizce,"Konusur",11, sep = "\n") #Kisa bir sekilde ayrilan karakterlere \n ekliyor.Yazdirirken yine alt alta yazilacak.
print(*"PYTHON")        #Degerin onune eklenen yildiz{*} degeri tek tek 1 bosluk birakarak ayirir.Fakat string olarak yazilmali {""}
print(*"TC ", sep".")   
print(" {} {} ` nin carpimi {}`dir" .format(100,0,0)) #Format degisiiklik icin kullanilir.Parntez icindekiler onceden yazilmis({}) yerine yazilir.
print(" {1} {0} {2}" ..format(11,10,12) ) #Onden yazilmis ({}) icine yazdigimiz degerler formatin parantezindeki yazilacak sirayi gosterir.Sira 0 dan baslar.Biz  bu ornekte kucukten buyuge siralamis olduk.
"{:.1f} {:.2f} {:.3f} " .format(2.24,1.50,4.45)  # (:. f) da virgulden son kac basamak alinacagini yazdik.f in onundeki sayi ile kac basamak alincaksa yazilir.
type(x) #Yazilan kodun ne turde oldugunu gosterir.

#Input : Girdi islemleri icin kullaniyoruz.Default olarak klavyeden girdi aliniyor.
input() #Kullanicinin girdilerini gormeye yariyor.
int(input("Lutfen Sayi Giriniz:")) #Girdiyi sayi olarak gormek icin 
float(input()) #Bu komutla tam sayi olmayan degerlerde ondalililarda yazilabilir.
a = input("Lutfen bir Deger Giriniz.") 
type(a) ##Default olarak string olarak okuma yapilir.Yukaridaki satirlarda tip donusumu yapmamizin nedeni budur.type() fonksiyonu kullandigimizda  str olarak goruruz.

#Logical Operator ve kontrol yapilari
#Mantik operatorleri matematikte gordugumuz mantik gibi  dogruluk  aynidir.Bu dogruluk tablosuna asina iseniz zorlanmiyacaksiniz.Tablo icin : https://en.wikipedia.org/wiki/Truth_table
a==b #A B es.Esitse True degilse False
a!=b #A B Esit degil Esitsede False farkli ise True. not equal   oldugundan once ! sonra = gelir.Yine alttakilerdede = sonra dikkat edersen.
a>b #Bu ve alttaki 3 tanede mat mantik sagliyorsa True saglamiyorsa False
a<b #Dipnot stringlerde ise alafabeye bak. 
a>=b #Bu yine hatali yazimin cok  yapildigi bir koddur hata yapmamak icin su sart kabul edebilir = hep sonradan gelir diger kullanimlarda da ornek += gibi.
a<=  
2==3 and 2==2 #False cikar cunku hepsi dogruysa dogru cikiyor.
2==3 or  2==2 #Bir tane dogru varsa True.Ikisi False ise False
not 2==2      #True ise False ,False ise True cevirir.
not(2==3 !=  2==2) #Bu sekilde xor yapabiliyoruz.
bool(0) #False doner diger tum sayilar True ayni C deki gibi.float tutulmus olsa bile 0.0 dada False doner.
print(int(True)) # 1 sonucu cikar.
print(int(False)) #0 sonucu cikar.
print(9+True) # 10 sonucu yazar.
print(9 * False) # 0 sonucu yazar.
bool("") #False doner bos degilse  True doner.bool(" ") bosluk karakteri de olsa bir karakterdir bu yuzden True doner.
l1=[1,2,3,4,5] 
l2=[1,2,3,4,5]
print(id(l1)) #Cikti 1780674395840 .Bu, bellekteki nesnenin adresidir. !!!( Pointer yani daha ayrinti icin CPython bakacagım. )!!!
print(id(l2)) #Cikti 1780723682816 
l1 == l2 #True deger doner.
l1 is l2 #False deger doner.Ustte gorumdugu fibi id yani ram adresleri  farkli oldugu icin false donuyor.
"Salih" is "Salih" #True deger doner.
10 is 10 #True deger doner.
"aa" is "a" * 2 #True deger doner.
a= "a" * 2
"aa" is a  #True deger doner.
a = "a"
"aa" is a * 2 #False deger doner.

#if-elif-else Kontrol yapilari bunlar belirli bir kosul altinda kod blogunun calismasini saglarlar.Yapisal programlamanin bir ozelligidir.

if (sayi>0):          #Kosul belirtir fakat gerkce True ise calisir False ise calismaz.
	print("Pozitif Sayi")   #Bu boslugu tab tusuyla yapabilirsin.

else:                    #Iki nokta koyarsak kosul gerkmeden If False ise calisir.Kosul eklersek oda True olunca calisir.
	print("Negatif Sayi")  	
elif (sayi==0):    #Baska bir kosul eklemek icin kullanilir.Elif ile cok fazla kosul yazilabilir.
	print("Notr Sayi")
if: elif: else:   #Siralama bu seklide olmali yoksa hata veriyor.Else ve elif kosullari tek basina calismaz.Parantez kullanmayabilirsin.

if 0: #False kabul etmek icin 0 haricinde tum sayilar True
a.find('Sa') #Degiskenin icinde arama yapmaya yariyor.
a[0]=0 # a daki degisen listeyi yazdiraca esitledik.Degisiklik her ikisinide etkileyecek.
a=b[:] #Liste ilk basta ayni olacak degisiiklikler kendi degiskenleriyle sinirli kalacak etkilemiyecek
a in 4 #True yazicak listede eleman var mi kontrolunu yapiyor.


#Loop : Donguler yine belirli bir kosul dahilinde kodlarin tekrar etmesini sağlar.Yine yapisal programlamanin bir ozelligidir.
while True: #Sonsuz dongu olur.Istersek True yerine kosul ekleyebiliriz. : while blokunun basladigini belirtmek icin kullaniyoruz. : for def kullaniyoruz : altindaki tab ile bosluk biraktigimiz blogu buna gore calistiriyor.  
#Sonsun songu bazen istenmeyen bir durumdur.Bazi hatali kontrolden dolayi surekli calisir bu sonsuz calismayi durdurmak icin Ctrl+C ile durdurabiliriz.
range(1,11,2)  #1 den hahil  11 kadar dahil degil ikiser artarak liste olusturuyoruz.
for i in range(): # i printlersek listeydeki elemanlari bastirmis olacagiz.for akis saglamasi icin liste,demet,sozluk,string gibi degerler ihtiyac duyar.range() bu yuzden var. 
#range(baslangic,bitis,adim) fakat sadece range(11) derseniz 11 bitis degeri olarak kabul eder 11 kadar olan 11 dahil degildir.Default baslangic degeri = 0 , adim degeri = 1 birer birer artar.Baslangic degeri dahildir.Adim degeri ne kadar atlama yapacagini belirtir.Adim degeri negatif olarabilir bu sefer azalan bir durum olur.
continue #Donguyu devam ettirir.
break  #Donguyu sonlandirir.
pass #Bu komut gec komutu.
import math # Kutuphane veya fonksiyon cagirmak icin.
dir(math)  # Ne calisabilir yazdirmak icin.
math.log10() # fonksiyonu kullunmuk icin . kullunmulı sadece import edildiyse
from time import sleep # Eger fonksiyon bu sekilde carildiysa sleep() seklinde direk calisibilir.(,)virgul ile time kutuphanesindeki diger fonksiyonlari ekleyebilirin.
x mod y #Sayının modunu bulmak için kullanilir.
x<>y #Esit değildir.
sgrt(x) #Karkok alir.
abs(x)  #Mutlak değerini alır.
random #0 ile 1 arasında rastgele bir sayı verir.
left(a,x) #Soldan x e kadar alır.
right(a,x) #Sağdan x e kadar alır.
value(a) #degiskeni sayiyi cevirir.
average(list) #Ortalamasini bulur.
sum(list) #Listedeki elemanlari toplamar.
date #Tarih gosterir.
time #Zamani gosterir.
exp(x) # E sayisinin x kadar kuvvetini alir. math.exp() import ettikten sonra calistirmak icin.
cos(x) #Cos x degerini alir.
pow(x,y) # x**y yani us alir.
degress(x) #Dereceyi radyana cevirir.
radians(x) #Radyani dereceye cevirir.
fabs(x)  #Fonksiyonun mutlak degerini  alir.
from time import clock #Kutuphane yukleyip clock() ilede kullanilir.
math.floor() #Ondalikli degerden onceki en buyuk tam sayi bulur.
math.ceil()  #Ondalikli degerden sonraki en buyuk tam sayi bulur.
import math as matematik #Kutuphaneyi matematik olarak tanimli calisir yapmak icin.math olarakta kullunmaya devam edebilirsin.
from math import * #Kutuphaneyi importlamis gibi olacak fakat from old icin kullanırken math.log10() yerine  direkt log10() calistirabilicem kolaylik saglayabilir.

import random
random.randrange(start, stop, step)  #PYTHON doc aldım. https://docs.python.org/3/library/random.html
random.random() #0 il 1 arasinda degerleri verir.
random.choice(a) #Parantez ici bos olamaz.Secim yapar liste olusturup secem yapilabilir.
def fonksiyon(parametre): #Kendimiz bir fonksiyon yapilabiliriz.
print("rastgele" .upper()) #Karakterleri büyük harfle yazadirir.
print("ABCD" .lower()) #Karakterleri kucuk harfle yazadirir.
print("      rastgele     "  .strip()) #Sağdan ve soldan boslugu siler.

#Functions or Method :  Yapisal porgramlamanin bir ozelligidir.
def fonksiyonadi(parametre,parametre2 .....): #Parametre girmedende yapabilirsin.İki noktadan anlasilabilecegi uzere alt satirlirdi bloklar olacak.
fonksiyonadi() #Fonksiyonu cegirmak icin.Parantez ici deger alabilir.
def top(a,b,c):    #Kac parametreyse o kader girdi girilmeli.
    return a+b+c   #return ile foksiyondaki islemi baska bir zamanda kullunmumizi sagliyor.Return fonksiyonu sonlandirir bu yuzden returnden sonra yazma.
def isim(ad="Salih"): #isim() deger girmeden yazarsak Salih olarak cıkacak.Eger deger verirsek o yazilcak.
isim(ad="Salih") #Fonksiyonda soyad old varsayarsak sadece ad degistirecek sirali girildigi icin bu islem ise yarayabilir.
def top(*a):  #İstedigimiz kadar degisken atayabiliyor.Fakat bunu liste olarak tutuyor dikkat.for ili kullunirkan a yani degiskeni al.
def fon(*args) #Yukaridaki ayni islem yapiyor.
def fon(**kwargs) # *args demet olarak **kwargs sozluk olarak arguman aliyor.
ef top():
    global a  #Onceden tanimli degisekni degisterdimizde her yerde degisecek cunku global dedik.Nomalde fonksiyonlar local kayitli ve sadece fonksiyon calisinci degisiyor sonrasindi oncedeh tanimli ne isi o kaliyor.
liste2=[x*2 for x in liste1] #Tek satirda listedeki her elemani 2 carpabilirirz.
   
def top(a,b): yerine top= lambda a,b: a+b #Blokla tanimlamak yerini tek satirda tanimlayabiliyoruz.Calistirirken yine fonksiyon gibi top(x,y). *a calismaz.Lambda tek satirda biter blok olarak komplike degil basit calisir.
a=list(map(lambda a,b: a+b,liste1,liste2)) #map fonksiyonu ile listede gezinmemize olanak sagliyor aynen for gibi.Asilinda  
x**2 for x in range(999) #Boylede tek satirda for kullunubiliriz.

#OOP (Object-oriented programming) : Nesne Yonelimli Programlama 
#Nesne yonelimli programlamada fonksiyon degil method olarak adlandirilirlar.
class Araba():
    mark="Volvo"
    model="S90"
    color="White"
    tork= 1500
    
        
araba1=Araba()
print(araba1) // pointerda gosterdiği adresi yazdiriyor boyle 
print(araba1.mark) // . deyip istediğimiz fonksiyonları çağırabiliriz.

class Araba():
    def __init__(self,mark,model,color,tork): #self ilk başta yazılmak zorunda. mark="Volvo" tanimi onceden yapabilirsin. 2  "_" (alt cizgi) init 2  "_" (alt cizgi) olarak yapiyoruz.
        self.mark=mark
        self.model=model
        self.color=color
        self.tork=tork
    def info(self):
        print("Marka: {} \nModel: {} \nRenk: {} \nTork: {}".format(self.mark,self.model,self.color,self.tork))
    
araba1=Araba("Volvo","S90","White",1500) #Sirayla girilmeli hata vermiyor fakat fonksiyonlari sirasiyla cagirdigi icin tork degirini bjk yazabilir
araba2=Araba("Volvo","S60","Black",1100) #Eksik girildiginde hata veriyor.
araba1.info()
araba2.info()

class Driver(Araba): 
    def __init__(self,mark,model,color,tork,haveto):#Eger sadece kalitimla bire bir aktarip baska fonksiyon eklemiyeceksek pass yazabiliriz
        super().__init__(mark,model,color,tork) #super ile tekrar self.mark model ... tanimlamadamiza gerek kalmaz ayni fonksiyonlari kullanilirsin.
        self.haveto=haveto 
    def info(self):
        print("Marka: {} \nModel= {} \nRenk: {} \nTork= {} \nAraba Sayisi= {}".format(self.mark,self.model,self.color,self.tork,self.haveto))
    
driver1=Driver("Volvo","S60","Black",1100,5)
driver1.info()

def f5(x):
    return x+5
l2=[2,6,3]
print(list(map(f5,l2)))
#Ayni islem fakat lambda cok daha az satir kod yaziliyor.
fazla5=list(map(lambda y: y+5 ,l2)) # x fonksiyon disindada tanimliyken y sadece lambda da tanimli bu bazi hatalarin yasanmamasi icin kullanulabilir.
print(fazla5) 
# for ilede yapilabilir
faz5=[i+5 for i in l2]
print(faz5)

#Cesitli kutuphaneler ve modullerin bazilarini yine anlatmistik devam ediyoruz.
from math import * #* tum methodlari eklemek icin kullanilir.Tek tek yazmak yerine * eklenir.

#Terminalde calisma yapmak icin
import sys 
sys.argv[1] #komut satirindaki degeri string olarak aliyor. 0 index dosyanin ismi var o yuzden 1 aldik baska index alabiliriz.

#Dosya islemleri 
file = open('dosyaadi', 'w',encoding="utf-8") #Yazma islemi icin acmak istedigimizde dosyayi bu sekilde yapiyoruz. w da yaparken dikkat! ayni isimili dosya varsa o dosyayi siler tekrardan yazar.encoding eklemek zorunlu degil.
file = open('dosyaadi', 'a',encoding="utf-8") #a ile acarsak eger ayni dosya varsa silmiyecek eklemeler yapabilecegiz.
file.write('This is a test\n') #Yazma islemini yapiyoruz.
file.close() #Islemler bittikten sonra kapatmamiz gerekiyor.
file = open('dosyaadi', 'r') #Okuma islemi icin acmak istedigimizde dosyayi bu sekilde yapiyoruz.
print(file.read(x)) #Print demezsek okunur fakat ekranda gostermez. x kadar byte oku.
print(i, end="") #for ile dosyayi yazdirdigimizda  \n silmek icin kullanabilirsin.
with file = open('dosyaadi', 'r',encoding="utf-8") as file: #Otomatik olarak dosyayi kapatacak. mode = 'rb' olursa read binary yani binary dosyalari okumak icin yazilir.
file.readline() # Satir satir okuma yapiyor.
file.seek(x) # x. index kadar ilerlemek icin.
print(file.tell()) #Dosya imlecinin hangi byte da oldugunu bilmek icin kullanabilirsin.
with file = open('dosyaadi', 'r+',encoding="utf-8") as file: # r+ ile hem okuma hem yazma yapabiliyoruz.
liste= satir.split(",") # , ile ayrilanlari bir eleman olaraka alicak.
open("dosyaadi","amac")   #Dosyayi acmamiza yariyor.Amac okuma yazma gibi islemleri belirtmek icin.
    amac= "w" #Yeni bir dosya yazmak icin ayni isimden baska dosya varsa siler dikkit. (write)
          "a" #Dosyanin son karakterden sonra eklemek icin silmeden kullaniliyor. (add)
file= open("dosyaadi","amac",encoding=("utf-8"))  #File bir degisken baska isimde verilebilir.utf Turkce karakter girilsin die ekleyebilirin.          
file.close() #Dosyayi kapatir.
file.write() #Acilan dosyaya yazi yazar.
icerik=file.read() #Dosya okumaya yariyor.
with open("dosya_adi.uzantisi") as dosya:
    icerik = dosya.read() #Bu sekilde yapilirsin.
print(icerik)

import csv
reader = csv.reader(file)
writer = csv.writer(file)

def scope_test():
    def do_local(): 
        spam = "local spam"  #do_local fonksiyonunda tanimli kalacaktir.

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam" #scope_test fonksiyonunda tanimli kalacaktir.

    def do_global():
        global spam
        spam = "global spam" #tum kodda tanimli kalacaktir.

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

try: #Hatali kodlari denemek icin kullaniyoruz.
    a=5/0
except: #Tum hatalarda calisacak eger ozel bir hatada calismasini istersek belirtmemiz lazim asagida ornegi var.
    print("Hata var")
except ZeroDivisionError : # Birden fazla hata yazilabilir yazim (eror,eror,...) seklinde olmali
    print("Hata sayiyi  0 bolemezsiniz.")

    print("Zoraki calisan kod")
def hatagoster(s): #Bu fonksiyonla kendimiz hata mesaji gonderebilir denemedim ama oyla umuyorum ki kendi hatalarimizi olusturabiliriz.
    if type(s) != str:
        raise ValueError("Lutfen string tipinde deger girin")
print(hatagoster(252))
try: #Calistirilacak kod bu blokda yazilir.
except: #Hata alinirsa calisir.
else: #Hata alinmassa calisir.
finally: #Hata olsada olmasada daima  calisir.

from functools import reduce 
# reduce map gibi liste ve demette gezinir elemanlari toplayarak devam eder. reduce(fonksiyon,liste veya demet ...)
reduce(lambda x,y : x*y ,[1,2,3,4,5]) #Bu sekilde tek satirda faktoriyel hesabi yapilabilir.
filter(lambda x : x%2==0 , liste) #filter(fonksiyon,liste veya demet ...) fakat fonksiyon boolean deger dondurmeli.
zip(liste1,liste2) # listeleri birlestirip (x,y ....) cinsinden tutmamiza yariyor. sozlukleride birlestirebiliriz.
enumerate(liste) #index degerlerini ve liste elemanlarini gostermek icin kullanabilirsin.
all(liste) #Tum degerler true ise true,false var ise false dondurur.
any(liste) # all tam tersi true var ise true , tum degerler false ise false donderir.
bin(x) # onluk tabandaki bir sayiyi ikilik (binary) tabanina ceviriyor.
hex(x) # 16 lik taban cevirmek icin
abs(x) # Mutlak deger alma islemi icin kullanabilirsin.
round(x) #Yuvarlama islemi yapar.
round(2.2226,3) # 2.223 cikar
max(x,y,z, ... ) #En buyuk sayiyi buluyor.Listede veya demetlerde  de calisir.
min(x,y,z, ... ) #En kucuk sayiyi buluyor.
sum(liste) #Liste veya demeteki elemanlari toplar.
pow(x,y) #Us alma islemi icin kullanilir. x taban , y us oluyor.
salih.upper() #Tum string karakterleri buyuk harfle gosterir.
salih.lower() #Tum string karakterleri kucuk harfle gosterir.
"10.1".replace(".",",") # replace ile tum karakter harfleri veya stirnigin bir kismini  degistirebiliyoruz.Bu ornekte Türkçe bir ondalik gosterim yapmis olduk.
"Start this code".startswith("Start") # Hangi karakter veya dizinle baslamasinin kontrolunu yapar sonuc boolean'dir.Buyuk kucuk harfe duyarlidir.
"Finish this code".endswith("Finish") # Hangi karakter veya dizinle bittiginin kontrolunu yapar sonuc boolean'dir.
liste= "Bunlar bizim kodlarimiz".split(" ") #Burda girdigimiz degere gore elemanlari ayirip listeye ekliyecek.
"      Bosluklari siler      ".strip() #Deger vermezsek basindan ve sonundan bosluklari siler.Eger bir karakter verirsek onu siler.
#lstrip() soldakileri rstrip() sagdakileri siler.

liste=[T,B,M,M]
".".join(liste) #String elmanlarin arasina karakter eklemeye yariyor.
.count("x") # x karakteri kac defa var gosterir.
.count("x",i) # x karakteri kac defa i. indexten baslayarak var gosterir.
find("x") #Bastan baslayip ilk buldugu x degerinin indexini verir.
rfind("x") #Sondan baslayip ilk buldugu x degerinin indexini verir.Eger deger yoksa -1 der.

import time
def zaman_hesapla(fonksiyon):
    def wrapper(sayılar):
        
        
        baslama = time.time()
        sonuç =  fonksiyon(sayılar)
        bitis =  time.time()
        print(fonksiyon.__name__ + " " + str(bitis-baslama) + " saniye sürdü.")
        return sonuç
    return wrapper
 
#Bu sekilde bir kere tanimladigimiz fonksiyonu istedigimiz bir calismadan once ekleyip sonucun gosteresiliyoruz.
 
@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 2)
    return sonuç
@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 3)
    return sonuç
    
 
print(kareleri_hesapla(range(100000)))
 
print(küpleri_hesapla(range(100000)))

it=iter(liste) #iterator olusturmak icin iter() kullaniyoruz.
next(it) #listenin sonraki elemanini almak icin kullanabilirsin.

def hesap():
    for i in range(11):
        yield i**3    #bu generator ozelligi tasiyor bellekte saklamyior kullandiktan sonra isi bitiyor.
            
from datetime import datetime
print(datetime.now()) #Now dan anlasilacagi gibi suan ki zamani ve tarihi gosterir.Degiskene atanabilir. Ornek: 2020-06-12 15:08:36.811028
zaman = datetime.now()
print(zaman.year) # adindanda anlasilacagi gibi sadece yili ekrana bastirir.
print(zaman.month)
print(zaman.hour)
print(zaman.minute)
print(datetime.strftime(zaman,"%Y")) # Yukaridaki islemlerin anisisni yapar.
# "%Y" = Yil icin , "%B" = Ay icin , "%A" = Gun ismi icin Ornek: Friday , "%X" = Saat icin , "%D" = Gun bilgisi icin Ornek: 06/12/20 . Ayrintili liste icin : https://docs.python.org/3/library/time.html?#module-time
print(datetime.ctime(zaman)) #Farkli bir formatta zamani gosterir. Ornek: Fri Jun 12 15:08:36 2020
import locale
locale.setlocale(locale.LC_ALL, '') #Localden zaman cekmeye yariyor.
ileri_tarih = datetime(2050,10,10) #Bir tarih atayabiliriz
print(ileri_tarih - zaman) # Ne kadar fark oldugunuda gosterebiliriz.
saniye = datetime.timestamp(zaman) #Saniye degerini aliyoruz
tarih = datetime.fromtimestamp(saniye) #Saniyeyi tarihe ceviriyoruz
datetime.date(year,month,day) 
datetime.time(hour,minute,second) 
datetime.datetime(year,month,day,hour,minute,second) 
now = datetime.datetime.today()
print(now) # 2020-06-28 16:55:06.378933
print(now.microsecond) # 378933
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing , "%m/%d/%Y" ) # string parse time  strptime() fakat "" icine yazdigin ayni olacak yoksa bosluklar hataya sebep veriyor.

import os  #os modulunu import etmek icin
print(os.getcwd()) #os modulunu dosya konumunu ekrana yazdirir.
os.chdir(".../dosya_konumu") #os modulunun dosya konumunu degistirir.
print(os.listdir()) #os modulunun oldugu klasordeki dosyalari yazdirir.
os.mkdir("dosya_adi") #os modulunun dosya konumuna yeni bir dosya acar.
os.makedirs("dosya_adi/yeni_dosya") #os modulunun dosya konumuna iki tane dosya aciyor ve yeni_dosya alt klasorde dosya_adi 'nin altinda kaliyor.
os.rmdir("dosya_adi/yeni_dosya") #sadece yeni dosyayi yada tek olarak yazidigimiz bir dosyayi siler.
os.removedirs("dosya_adi") #Tum dosyalari  alt dosyalari dahil siler.
os.rename("dosya_adi","dosyanin_yeni_adi") # Dosyanin ismini degistirir adindanda anlasilacagi gibi
print(os.stat("dosya_adi")) #Bazi ozelliklerini gosterir ayni saga tiklayip baktigimiz gibi
print(os.stat("dosya_adi").st_mtime) # sn cinsinde degisiklik yapildigi zamani gosterir
from datetime import datetime
print(datetime.fromtimestamp(os.stat("dosya_adi").st_mtime)) #bu sekiyde daha anlasilir bir zaman gosterir.
for i in os.walk("C:/Users/Salih/Desktop"): #dizindeki tum dosyalari konumlariyla yazdirmak icin.Ayni dosya gezgini gibi calisir "" arasina istedigin bir dosya konumunu yazabilirsin yalniz aralainda / olacak dikkat.
    print(i)
for i,j,k in os.walk("C:/Users/Salih/Desktop"): #i = Dosya Konumu , j = Klasor Ismi , k = Dosya Ismi

import sys #sys modulunu import etmemize yariyor.
sys.exit() #Cikis yapmak icin kullanilir.Calistirildiginda diger kodlar calismaz ve sonlanir.
stdin #Bu dosya input islemlerinde kullanilir.
stdout #Bu dosya cikti almak icin kullanilir.
stderr #Bu dosya hata ciktisi almak icin kullanilir.
sys.stderr.write("Bu hata mesaji \n") #Bu sekilde hata mesaji yazabilir.
sys.stderr.flush() #Hatali mesaji ekrana yazdirabiliriz.
sys.stdout.write("Mesaj\n") #Normal bir yazida yazdirabiliriz.
sys.argv[x] #komut satirindan calistirdigimazdaki giridleri almaya yariyor.

from urllib import request
resp = request.urlopen("www.co")
print(resp.code)
data =  resp.read()
html = data.decode("UTF-8")
from urllib import parse
params = {"v": "LosIGgon_KM", "t": "0m0s"}
querystring = parse.urlencode(params)
url = "https://wwww.youtube.com/watch" + "?" + querystring
resp= request.urlopen(url)
resp.isclosed()
html = resp.read().decode("utf-8")
#Kaynak:https://www.youtube.com/watch?v=LosIGgon_KM

#Consoleda bu asagidaki iki kodu yazarak indirmemiz gerekiyor.
pip3 install requests
pip3 install beautifulsoup4
import requests
from bs4 import BeautifulSoup
url= "www..co"
response = requests.get(url)   
html_icerigi  = response.content 
soup = BeautifulSoup(html_icerigi,"html.parser")
print(soup.prettify()) #Sayfa kaynagini goruntule yada view page source da gozuktugu gibi tamamini html tagleriyle ekrana yazdiracagiz.
print(soup.find_all("a")) #a etiketli olanlari ekrana yazdiriyoruz.
for i in soup.find_all("a"): #Yukaridaki islemin daha guzel ekrana yazdirmak icin kullanabilirsin.
    print(i)
    print(i.get("href")) #Sadece linkleri almak istersek bu sekiyde yapabilirsin.
    print(i.text) #Metinleri almak istersek 
print(soup.find_all("div",{"class":"tarih"})) #Bu sekilde class olarak aldiklarimizi ekrana bastiririz.
#Bilgi olsun die var guvenliligi bilmedigimden yapmadim.

#SMTP modulu guvenlik gerekcesiyle ele alinmadi fakat tekrar videsona bakabilirsin.

pip3 install Pilow #Pilow kutuphanesini kurmak icin
from PIL import Image #Pilow kutuphanesini desteklemek icin.
img = Image.open("resim.png")  #Resimi acmak icin kullaniyoruz.
img.show() #Resmi gormek icin 
img.save("resim2.png") #Resmi kaydetmek icin.
img.rotate(x).save("resim2.png") #x derece resmi dondurmek ve kaydetmek istersek.
img.convert(mode = "L") #Resmi siyah-beyaz BJK ceviriyor.
img.thumbnail(x,y) #x,y bir degiskende yazabilirsin bu islem resmin boyutunu degistirmek icin
kirp_alan = (x,y,z,t)
img.crop(kirp_alan).save("resim3.png")  #Resmin girilen kordinatlariyla kirpmaya yariyor.Kordinatlari photoscape gibi programlarla bulabilirsin.

import logging
logging.basiclog(filename = "E:\\python\\reg.log", level = logging.DEBUG, format = LOG_FORMAT , filemode= 'w')
logger = logging.getLogger()
logger.debug("This debug message.")
logger.info("This info ")
logger.warning("This warning")
logger.error("This error")
logger.critical("This critical")

#SQLite databases sqlite3 module 
import sqlite3
conn = sqlite3.connect('verim.db') #Verim adindaki database baglaniyor eger yoksa kendisi olusturyor.
cursor = conn.cursor() #Imlec atamak icin bu islemi yaptik.
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(Isim TEXT,Yazar TEXT, Sayfa_Sayisi INT)") #IF NOT EXISTS eger yoksa olusturmak icin yazdik.Bu sekilde bir tablo olusturuyoruz.
    conn.commit() #Degisiklikleri kaydetmek icin bu islemi kullaniyoruz.
    
def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES('And', 'Omer Seyfettin',100)")
    conn.commit()

cursor.execute("INSERT INTO kitaplik VALUES(?, ?, ?)",(isim,yazar,sayfa_sayisi)) #Bu islem kullanicidan aldigimiz degerler icin bu sekilde yapiyoruz.Foksiyordada bu degiskenleri alinacagini belirtiyoruz tabi
tablo_olustur()
veri_ekle()
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik") #Kutuphanelrde oldugu gibi tum veriyi almak icin * kullandik.
    cursor.execute("SELECT Isim,Yazar FROM kitaplik") #Sadece isim ve yazar degerlerii alir.
    cursor.execute("SELECT * FROM kitaplik WHERE Yazar = 'Omer Seyfettin'") #Sadece yazari Omer Seyfettin olan aliyoruz.
    liste = conn.fetchall()
    print(liste)
    
    for row in conn.execute("SELECT * FROM kitaplik"): #Satir satir yazdirmak icin for kullanabilirsin.
        print(row)
def verileri_guncelle(sayfa_sayisi):
    cursor.execute("UPDATE kitaplik SET Sayfa_Sayisi = sayfa_sayisi WHERE Sayfa_Sayisi = 100 ") #Degisiklik yapmak istedigimizde bu islemi yapiyoruz.
    conn.commit()
def verileri_sil():
    cursor.execute("DELETE FROM kitaplik WHERE Isim = 'And' ") #Istedgimiz ozelliktekini silmek icin bu islemi yapiyoruz.
conn.close() #Baglantiyi sonlandirmak icin kullaniyoruz.

# Pyqt5 Graphic User Interface (GUI) araci ayrintili baska araclar icin: https://docs.python.org/3/faq/gui.html
#Kivy kullanmak istiyorum mobil programlama icinde yine linkten ayrintilarina ulasilabilir.
import sys
from PyQt5 import *
def window():
    app = QtWidgets.QApplication(sys.argv) #Uygulama olusturup sys.argv komut satirindan okuma yapmasi icin ekledik.
    pencere = QtWidgets.QWidget() #Widget olusturduk.
    pencere.setWindowTitle("Ilk Deneme") #Widget baslik ekledik.
    etiket = QtWidgets.QLabel(pencere) #Label ekleme icin 
    etiket2 = QtWidgets.QLabel(pencere) 
    etiket2.setPixmap(QtGui.QPixmap(resim.png)) #Resim eklemek icin kullaniyoruz.
    etiket.setText("Bu alanda yazi") #Yazi eklemek icin kullaniyoruz.
    button = QtWidgets.QPushButton(pencere) #Buton olusturmak icin kullanilir.
    button.setText("Tikla") 
    etiket.move(100,100) #Move ile  harekete ettiriyorsun  fakat widget boyutu degisirse bozulabilir.Responsive bir tasarim degil. 
    pencere.setGeometry(200,200,500,500) #a,b konumu icin girilen degerler.Hangi kordinattan baslayaçagi. c,d ise buyuklugunun en,boy ddegerleri.
    #                    a   b   c   d
    
    
    horizantal_box = QtWidgets.QHBoxLayout() #Yatalda bir layaout olusturmak icin QHBoxLayout kullaniyoruz.
    horizantal_box.addStretch() #Satirin basinda boslukk olmasi icin 
    horizantal_box.addWidget(kabul)
    horizantal_box.addStretch() #Kabul butonundan sonra bosluk birakiyor yanii yapilan islemden sonra bosluk birakiyor.Bu sekilde konumlari sabit kalirken sadce genisliyorlar.
    horizantal_box.addWidget(red)
    pencere.setLayout(horizantal_box) #Yaptimiz pencere widget olmasi icin bu satiri ekliyoruz.
    horizantal_box.addStretch() #Satir sonunda bosluk olmasi icin.
    vertical_box = QtWidgets.QVBoxLayout() #Dikeyde butonlari olusmasi icin QVBoxLayout kullaniyoruz.
    pencere.setLayout(vertical_box) #Ayni sekilde pencere widget olmasi icin kullaniyoruz.    
    #Farki QHBoxLayout olusturlanlar yatayda saginda vela solunda siralanirken.QVBoxLayout dikeyde yani alt alta siralanir.
    
    
    pencere.show() #Adindan anlasilacagi gibi gostermek icin ekledik.
    sys.exit(app.exec_()) #Windowsta X isaretine basana kadar calismasi icin bu satiri yazdik.
window()

def window(): 
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Uygulama")
    pencere.setGeometry(200,200,500,500)
    ha_box = QtWidgets.QHBoxLayout()
    next = QtWidgets.QPushButton("Ileri")
    previous = QtWidgets.QPushButton("Geri")
    ha_box.addWidget(previous)
    ha_box.addWidget(next) #Ekleme sirasi onemli ona gore siraliyor.
    av_box = QtWidgets.QVBoxLayout()
    av_box.addStretch()
    av_box.addLayout(ha_box) #Bu sekilde yatay ve dikeyi birlestiriyoruz.
    pencere.setLayout(av_box)
    pencere.show()
    sys.exit(app.exec_())
window() #Bu kodlarla altta aralarainda bosluk olacak selide ilerleme button olusturduk.
 

 class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def  init_ui(self):
        self.yazı_alanı = QtWidgets.QLineEdit()  #Input alani olusturmak icin QLineEdit kullaniyoruz.
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Goster")
        self.yazi = QtWidgets.QLabel()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.temizle.clicked.connect(self.temizleme) #clicked tiklandi bilgisini aliyoruz. connect ile methoda bagliyoruz.
        self.yazdir.clicked.connect(self.eyaz)
        self.show()
    def temizleme(self):
        self.yazı_alanı.clear() #clear ilede temizleme islemini yapiyoruz.
    def eyaz(self):
        print(self.yazı_alanı.text())
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
#Tek fonksiyonlada yapabiliriz onun ornegi
self.temizle.clicked.connect(self.tiklama)
self.yazdir.clicked.connect(self.tiklama)
def tiklama(self):
    sender = self.sender()  #Yapilan aksiyonu aliyoruz diebiliriz.
    if sender.text() == "Temizle": #Senderdan gelen yaziyi alip kontrol yapiyoruz.
        self.yazı_alanı.clear()
    else:
        print(self.yazı_alanı.text())

self.parola.setEchoMode(QtWidgets.QLineEdit.Password) #Girilen alandaki yazilar gizlenecek ozel karakter olacak bu sekilde.
self.yaziAlani.setText(self.inputYazi.text()) #Girdiyi alip yazdirirken setText dierek yapiyoruz.
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
self.checkbox = QCheckBox("Anlasmayi kabul ediyorum.") #checkbox olusturmak icin yapiyoruz.
self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked())) #isChecked ile checkbox isaretlenip isaretlenmedigini kontor ediyoruz.lambda olmazsa hata verebilir genelde fonksiyon aldigi icin.
def click(self,checkbox,yazi_alani):
    if checkbox:
        yazi_alani.setText("Anlastik")
    else:
        yazi_alani.setText("Sen anlasmayi bozdun kardes")
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout
self.radio_yazisi = QLabel("Hangi dili daha çok seviyorsun ?")
self.java = QRadioButton("Java") #QRadioButton radio button olusturuyoruz.Bunlar tek secim icin kullanilir.checkbox birden fazla secim yapilabilir.
self.python = QRadioButton("Python")
self.php = QRadioButton("Php")
self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))
def click(self,python,java,php,yazi_alani):
    if python:
        azi_alani.setText("Python")
    elif php:
        yazi_alani.setText("Php")
    elif java:
        yazi_alani.setText("Java")
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout
self.yorumAlani = QTextEdit() #Bu sekilde HTML ile textarea yaptigimizin aynisini burada yapiyoruz.

import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")
        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
    def yaziyi_temizle(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())
    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
        self.menuleri_olustur()
    def menuleri_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")  #Kisayol tusu eklemek icin kullaniliyor.
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle = QAction("Dosyayı Temizle",self)
        temizle.setShortcut("Ctrl+D")
        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        dosya.triggered.connect(self.response)
        self.setWindowTitle("Metin Editörü")
        self.show()
    def response(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Dosyayı Temizle":
            self.pencere.yaziyi_temizle()
        elif action.text() == "Çıkış":
            qApp.quit()   #Uygulamayi kapatmak icin.
app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())

#Numpy ve veri yapilari
import numpy as np #Bu sekilde kisaltmalida kullanilabilir.Fakat ben bu sekilde ele almiyacagim.
npArray = numpy.array(liste) #Listeyi array seklinede tutuyoruz fakat numpy ile 
npArray = numpy.array([1,2,3,4,5]) #Listede oldugu gibi listeyi onceden tanimlamadan da yapabiliriz.
npArray[2,2] #Listelerde oldugu gibi [] ile elemanlara erisiyoruz fakat ic ice olanlari [][] bu gosterimin yerine ornekteki gibi yapiyoruz.[:::] bu islem yine ayni kullanabliriz.
npArray = numpy.arange(1,     9,      2) #range fonksiyonunu yine kullanabiliriz.
#                     baslangic, bitis, adim  
npArray = numpy.zeros(x) #x tane sifir olan array olusturmak icin kullanilir.
npArray = numpy.ones(x)  #x tane bir olan array olusturmak icin kullanilir.   
#numpy arraylerdeki int degerlerini float cevirir.Bu yuzden 1. veya 0. die ekrana yazilirlar.
npArray = numpy.ones((x,y)) #Bu sekilde iki boyutulu yapabiliriz.x ve y degerlerini esit olmasi zorunlu degil.
npArray = numpy.linspace(0,   10,   3) #linspace es parcaya bolme islemi yapiyor.Bir pastayi boler gibi degil fakat sirayi boler gibi dusunebiliriz.
#                     baslangic, bitis, kaca bolunecegi
npArray = numpy.eye(x) #Diyagon yapmak icin kullaniliyor eye metodu ile kaca kaclik oldunu x yerie yaziyor kare matris olusturuyor.
'''
ornek 4 4 luk bir diyagon
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''
npArray = numpy.random.randint(0,  10,   5) #Random degerleri array olarak saklamak istersekte bu sekilde kullanabiliriz. Ornek ciktisi [3 2 9 0 5]
#                         baslangic, bitis, kac sayi olusturulacagi
npArray = numpy.random.rand(x) #rand fonksiyonunuda kullanabiliriz 0-1 kadar x tane random sayi olusturabiliriz.
npArray = numpy.random.randn(x) # negatif olsun istersek bu sekilde yapabiliriz.Fakat sinirlar farkli tam olarak bilmiyorum.
npArray = npArray.reshape(x,x) #matris olusturmak istersek reshape yapabiliriz.Fakat arraydeki elemanlarin girilen x degeri kadar alani kaplayacak sekildeolmali bosta eleman kalinca kabul etmiyor.
npArray.max() #array deki maximum degeri almak istersek max fonksiyonununu kullaniyoruz.
npArray.argmax() #max degerin kacince indexte oldugunu bulmak icin argmax kullanabiliriz.
npArray.min() #array deki minimum degeri almak istersek min fonksiyonununu kullaniyoruz.
npArray.argmin() #min degerin kacince indexte oldugunu bulmak icin argmin kullanabiliriz.
npArray.sum() #Tum arrayleri toplamak istersek sum fonksiyonunu kullaniyoruz.
npArray.mean() #Tum arraylerin ortlamasini bulmak icinde mean fonksiyonunu  kullanabiliriz.
numpy.linalg.det(npArray) #Determinant islemi icin linalg.det() fonksiyonunu kullaniyoruz.square matrix  olmak zorunda yoksa hata veriyor.
cArray = npArray.copy() #Bu sekilde deep copy yapiyoruz yine cArray = npArray shadow copy yapabiliriz.
npArray[:x,:y] #x kadar satir y kadar stundan eleman almak icin kullanilabilir.
#satir baslangici : satir bitis , stun baslangici : stun bitis
npArray > 50 #arraydeki elemanlari kontrol edip true veya false olarak tekrar dondurur.
gecerNotlar[ gecerNotlar > 50] #True deger donenler ayni zamanda tekrar array olarak tutulacak.
npArray = npArray[npArray % 2 == 0 ] #Farkli kosullarda verilebilir.
npArray1 + npArray2 #Bu islem index sirasiyla toplar.Ornek npArray1 : [1,2,3] npArray2: [4,5,6] sonuc = [5,7,9] .Ornektede ayni eleman sayisina sahip olmalilar.
# + * / % kullanilabilir.
npArray + 5 #Her elmanin 5 fazlasi gibi islemlerde yine yapilabilir artik nasil islem yapmak istersek bircok operatoru kullanabiliriz.
numpy.sqrt(npArray) #Karekok alabiliriz.Deneyerek daha fazla islemleride yapabilriz.math kutuphanesindeki fonksiyonlarida kullanabiliriz.

#Pandas ve veri yapilari
import pandas as pd #Pandas kutuphanesini importlamak icin bu sekilde yapabiliriz.
labelList = ["Ali","Veli","Deli"]
dataList = [10,50,100]
pd.Series(data = dataList, index = labelList) #Pandas serisi olusturmak icin yazilir.
pd.Series(data = dataList) #index degerini kendisi olusturur.
pd.Series(dataList,indexList) #Bu daha kisa gösterimdir ustteki  islemin.Listeler esit sayida olmali  az veya fazla her  ise hata veriyor.
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
pd.Series(d) #Sozlukleride yine pandas serilerilene donusturebiliriz.
labelList = ["Ali","Veli","Deli"]
dataList = [10,50,100]
ps1 = pd.Series(data = dataList, index = labelList)
ps2 = ps1
ps3 = ps1 + ps2 #Yine matematiksel islemler yapilabilir.
labelList2 = ["Ali","Keli","Deli"] 
dataList2 = [10,50,100]
ps4 = pd.Series(data = dataList2, index = labelList2)
ps5 = ps3 + ps4  #ps1...ps3 Keli, ps4 Veli olmayan bir veri olduguu icin  NaN veya nan (not an number kisaltmasi olarak) gösterecektir.
npArray = np.array([10,20,30,40,50])
pd.Series(npArray) #Numpy arraylerini ayni sekilde pandas serisi olarak tutabliriz.
df = pd.DataFrame(data = [(11,5,6),(7,8,9),(4,5,6)], index = ["1.","2.","3."], columns = ["Col1", "Col2", "Col3"]) #DataFrame columns degeri eklenmesi gerekiyor.Bu sekilde bir tablo yapilabilir.
df = pd.DataFrame([(11,5,6),(7,8,9),(4,5,6)],["1.","2.","3."],["Col1", "Col2", "Col3"]) #Yine pandas serilerinde  oldugu gibi siralamayi dogru yapildigi surece direkt bu sekilde de yazilabilir.
df["Col1"] #Col1 altinda siralanan verileri alabilir.Her bir kolonu yazarken yine index degerlerimizde yine yazilacak bu sekilde tablo olarak yine veriyi alabiliriz.
df["Col1"]["1."] #11 degerini gosterecek.
df.loc["1."] #Buda satiri yazdirmak icin yapabiliriz.Bu seferde columns degerlerinide yazdirarak tablo olarak görmemize yardimci oluyor.
df.loc[["1.","Total"],["Col1","Col2","Col3","Col4"]] #Burda yine istenilen tablo kisimlarini almak istersek bu sekilde yapabiliriz.
df.iloc[0] #Yukardaki islemin array index yapisiyla cagirmak istersek bu sekilde yapabiliriz.
df.iloc[0][3] #Bu sekilede yine array index yapisiyla satir ve sutunun ilgili verisini alabiliriz. 1. girdi satir icin 2. girdi stun icin 
df["Col3"] = (df["Col1"] + df["Col2"]) / 2 #Bu sekilde bir aritmetik ortalamasini alabilir.float tipinde tuttugu icin bolme islemi dogru sonuc yazacaktir.
df.loc["3."] = df.loc["1."] + df.loc["2."] #Bu sekilde excel programinda genelde yapilan tabloda toplam degerlerini bu sekilde yine yapabilir.
df[["Col1","Col2"]] #Bu sekilde iki kolonu alabiliriz. 
df["Col4"] = pd.Series(data = [10,5,25], index = ["1.","2.","3."]) #4. kolonu yine bir seri olarak tanitmaliyiz ve index degerleri ayni olmalidir.
df["Col5"] = [10,5,25] #index sayisi kadarlik bir listeyide yeni bir stun olarak ekleyebilirsin.
df["Avg"] = ((df["Col1"] + df["Col2"] + df["Col3"]) / 3) #Bu sekilde yapilabilir.
df.loc["Total"] = df.loc["1."] + df.loc["2."] + df.loc["3."] #Kolon ekledigimiz gibi satirda ekliyebiliriz.
df.drop("Col3",1, inplace = True) #Kolon tablodan silmek icin bu islemi yapabiliriz.1 degeri axis'te y kordinati gibi dusunelim.inplace default olarak false olarak tanimlidir.
df.drop("3.",0, inplace = True) #Satir silmek icin bu islemi yapiyoruz.0 degeri axis'te x kordinati gibi dusunelim.
'''
NOT:
Fakat sunu unutmayalim sadece tablodan silmek icin bunu yaptik.Onceden yaptigimiz Total satiri ve Avg stunu yine ayni degerde kalacaktir.
Veri yapilarinda da gordugumuz bir kavram, inplace değilse  gibi hafizayi harici ayri bir blokta tutuyor.Eger bir algoritma inplace ise bunu kullanilan hafiza blogunda yapiyor.Bu yuzden inplace false ise  tablo degismiyecektir.
Ornek olarak insertion sort,quick sort bakabilrsiniz bu siralama algoritmasi inplace bir yapidadır.Merge sort, counting sort inplace olmayan siralama algoritmalaridir.Daha bircok ornekte inceleyip farkini anlayabilirsiniz.
'''
df["Index"] = [0, 1, 2, 3]
df.set_index("Index", inplace = True) #index stununu degistiriyor ve stun basligi bu ornekge gore Index olarak yaziliyor.
df.index.names #Index stunun baslik ismini gormek icin bu sekilde yapabiliriz.
df.index.names = ["Konum"] #Default olarak None degerdedir tabloda bir index basligi yazmaz.BU islemlede yine index stununa baslik ismi verebiliriz.
booldf = df > 50 #Bu islemle kontrol yapiliyor tum tablodaki verilerde bu sonucu saglayanlar tabloda true saglamayanlar false olarak yazilip tablo olarak gosteriliyor.
df[df > 50] #Bu kosulu saglamayanlar Nan veya nan gosterecek.
df[booldf] #Bu sekilde yazim yine yukaridaki gibi ayni sonucu verecktir.
df["Avg"] > 50 #Bu sekilde ortalama kontrolu yapiyor yine tablo seklide sonucu cikariyor.
boolavg =  df["Avg"] < 50
df[boolavg] 
df[df["Avg"] < 50] #Bu yukaridaki ile ayni islemler gosterim farkli.Bu iki islem birini yaparsaniz kosulu saglayanlar tabloda gozukecek saglamayanlar tabloda yer almiyacak.
df[(df > 50) & (df < 80)] #Bu sekilde bu sekilde and operatoru ile karsilastirilmis gibi yapacak pandas and kabul etmedigi icin bu sekilde yapiyoruz.
df[(df > 50) | (df < 80)] #Bu sekilde or operatoru ile karsilastirilmis gibi yapacak pandas and kabul etmedigi icin bu sekilde yapiyoruz.
df[(df > 50) ^ (df < 80)] #Bu sekilde xor yapabiliriz.
df[ (df["Avg"] > 50) & (df["Avg"] < 80)] #Yİne benzer filtreleme islemleri yapilabilir.
outerIndex = ["Group1", "Group1", "Group1", "Group2", "Group2", "Group2"]  #Bunlar dis grup icin bu sekilde
innerIndex = ["1.","2.","3.","1.","2.","3."] #Icteki grup icin bu sekilde yaziyoruz yazdirilinca nasil gozuktugu anlasilacaktir.
oii = list(zip(outerIndex,innerIndex))
df = pd.DataFrame([(11,5,6),(7,8,9),(4,5,6),(11,50,60),(70,80,90),(40,50,60)],oii,["Col1", "Col2", "Col3"]) #index bolumune oii ekledik sadece digerleri kullandigimiz yontemler.
print(df["Col2"]) #Yine kolonlari yazdimak icin bu sefer tabloda grup ve icteki index degerleride ekrana gelecek bu islemleri klasorlemek gibi dusunebilirz.
print(df.iloc[0]) #Ilk grup1deki ilk satiri gosteriyor.
print(df.iloc[0][0]) #Ilk grubun ilk satirin ilk stun degeri gostermek icin.
print(df.loc["Group2"].loc["2."]["Col1"]) #Yukardaki islemin farkli gosterimi bunuda kullanabilirsin.
print(df.loc["Group2"]) #Group2 sadece gostermek icin bu sekilde yapabiliriz.
print(df.loc["Group2"].loc["2."]) #Group2 nin 2. satirindaki gostermek icin bu sekilde yapabiliriz.
df.index.names = ["Parti","Konum"] #Yine baslik ekleyebiliriz.
df.xs("Group1") #Bu da baska bir group gostermek icin kullanabiliriz.
print(df.xs("Group1").xs("3.")) #Group1 3. satirini gostermek icin kullanabiliriz.
print(df.xs("Group1").xs("3.").xs("Col2")) #Group1 3. satirini gostermek icin Col2 degeri gostermek icin kullanabiliriz.
print(df.xs("2.",level = "Konum")) #Bu sorguda 2. index degerine sahip satirlari grouplarla birlikte gostermek icin yapiyoruz.level yazmazsak hata veriyor.Default olarak None degerde ve erisim icin level belirtmemiz gerekiyor.
np.nan #as np yapmistik numpy kutuphanesini bu sekilde veriyi NaN veya nan olarak tanimlayabiliriz.
df.dropna() #axis degeri default olarak 0 yani x kordinatina gore bakicak.Satirlarda 1 tane NaN varsa o satiri cikaracak.
df.dropna(1,inplace = True) #NaN olanlari silmek icin kullanabilirsin default yine inplace = 0 olarak tanimlidir.
df.dropna(0,thresh = 2,inplace = True) #Girilen thresh degeri kadar tanimli bir sayi varsa onlari kabul ediyor.Eger NaN sayisi fazla ise bu sefer sayi tanimlari az kaldigi icin ilgili axis ile silme islemi yapiyor.
df.fillna(0) #NaN olarak tabloda gosterilen degerin degerini parantez icinde girdigimizle degistiriyor.
df.sum() #Bu islemle stunlardaki tum verileri topluyoruz.Yine tablo olarak gosteriyor.df.sum(0) bu sekilde yapabilir cunku default olarak axis = None tanimlidir.
df.sum(1) #Bu islemle satir satir tum verileri topluyoruz.
df.sum().sum() #Toplanilan stunlarinda toplamini istersek bu sekilde yaziyoruz kisacasi tablodaki tum verileri topluyoruz.Birinci sum 1 veya 0 olmasi sonucu degistirmez.Sirasiyla sum alabilecak degerler ikili gosterim olarak (0,0),(,),(0,),(1,),(,0)(1,0) eger bu ikili disinda bir degerler verirseniz hata alirsiniz.
df.size #Tabloda kac tane veri oldugunu dondurur.NaN olalarda sayilir fillna yapilsin veya yapilmasin.
df.isnull() #Tabloda NaN olanlari true veya false olarak gosterir.
df.isnull().sum(0) #Stunlardaki NaN eleman sayisini toplar gibi dusunebiliriz veya NaN veri sayisini gosterir kolon bazli.
df.isnull().sum(1) #Satirdaki NaN eleman sayisini toplar gibi dusunebiliriz veya NaN veri sayisini gosterir satir bazli.
df.isnull().sum().sum() #Toplamda kac tani NaN verisi varsa onu gosterir.Sirasiyla sum alabilecak degerler ikili gosterim olarak (0,0),(,),(0,),(1,),(,0)(1,0) eger bu ikili disinda bir degerler verirseniz hata alirsiniz.

dataset = {"Alan":["IT","İnsan Kaynaklari","Pazarlama","Pazarlama","IT","IT"],"Calisan": ["Mustafa","Ali","Kenan","Zeynep","Murat","Ahmet"],"Maas":[3000,3500,2500,4500,4000,2000]} #Bir veri seti olusturduk.
df = pd.DataFrame(dataset) #Veri setini DataFrame yaptik.
subGroup =  df.groupby("Alan") #Burda group olusturduk.axis = 0 default olarak tanimlidir.
subGroup.sum() #Olusturdugumuz gruplarda ayni olanlar toplanacak bu ornekte toplam ilgili alanin maas toplami tablo olacak.
subGroup.count() #Grouplanan verilerin sayisi veriyor bu ornekte  kac kisi ayni alanda  calisiyor gorebiliyoruz.
subGroup.max() #Ilgili grouptaki en buyuk degerler gosterilecek.
subGroup.min() #Ilgili grouptaki en kucuk degerler gosterilecek.
subGroup.mean() #Ilgili grouptaki ortalamasini  gosterilecek.
#subGroup.mean().loc["IT"] yukarida satir ve stundaki ilgili blogun alinmasi islemleri burdada yine gecerli tekrar ele alinmadi.
subGroup.mean()["Maas"]["IT"] #Degeri tablodan bagimsiz olarak almak ve kullanmak icin bu sekilde yapilabilir.
dataset1 = {"Alan":["IT","İnsan Kaynaklari","Pazarlama","Pazarlama","IT","IT"],"Calisan": ["Mustafa","Ali","Kenan","Zeynep","Murat","Ahmet"],"Maas":[3000,3500,2500,4500,4000,2000]}
dataset2 = {"Alan":["IT","İnsan Kaynaklari","Pazarlama","Pazarlama","IT","IT"],"Calisan": ["Mahmut","Ali","Furkan","Sila","Murat","Ahmet"],"Maas":[3000,3500,5500,4500,4000,8000]}
df1 = pd.DataFrame(dataset1)
df2 = pd.DataFrame(dataset2)
df3 = pd.concat([df1,df2],0) #concat ile DataFrameleri birlestiriyoruz.axis = 0 default tanimlidir bu listeyi satir olarak ekliyecegini belirtiyor.
df4 = pd.concat([df1,df2],1) #axis = 1 ornekte esitledik.Bu islemle  stun olarak ekleme yapmasini istedigimzi belirtiyoruz.
dataset1 = {"A":["A1","A2","A3","A4"],"B": ["B1","B2","B3","A4"]}
dataset2 = {"X":["X1","X2","X3"],"Y": ["Y1","Y2","Y3"]}
df1 = pd.DataFrame(dataset1)
df2 = pd.DataFrame(dataset2)
df1.join(df2)#Join islemi kumelerdeki A-B ˅ A˄B  gibi dusunebiliriz.Default degerlri how = left bu hangi kumeyi alacagini belirliyor ve sort = False istersek siralayabilirizde.
df3 = pd.merge(df1,df2, on = "B")#merge() islemi A˄B aliyor.Yani ortak olanlar alniyor.Default how = 'inner' inner join kullaniliyor fakat farkli yontemlerde var.Left join,right join,outer join ... var.on esitlik kontrolu yapacagimiz hangi alansa onu yaziyoruz.
df1.head(3) #dead() girilen deger kadar satir basindan baslayarak almamiza yariyor.Default n = 5 yani sadece 5 satir aliyor.
df1["A"].unique() #Adindan anlasilacagi gibi essiz benzersiz olanlari almamiza yariyor.
df1["A"].nunique() #unique olanlarin sayisi icin nunique() kullaniyoruz.
df1["A"].value_counts() #Belirtilen alandaki degerlerin sayisini gosterir.Bunlarda tek stunlarda degil satirda da bu islemleri yapabiliriz.
def karesi(x):
    return x**2
df["Col1"].apply(karesi) #apply() ile bir fonksiyonu calistirabiliyorum DataFrame uzerinde tum fonksiyonlari kullanabiliriz tek fark func() yerine func yaziyoruz.
kare = lambda x : x**2
df["Col2"].apply(kare) #Lambda fonksiyonlarida kullanabiliriz.
df["Col3"].apply(lambda x : x**2) #Yukaridaki iki batir yerine bu sekilde tek satirda tum islemleri yapabiliriz.
print(df.columns) #Tum kolonlarin isimlerini yazdirir.
print(df.index) #Tum satirin index isimlerini yazdirir.
print(len(df.index)) #Tum satirlarin index sayisini yazdirir.
print(len(df.columns)) #Tum stunlarin sayisini yazdirir.
df.sort_values("Col1",0) #Stunlari siralayabiliriz.axis = 0 defailt olarak belirlenmis 0 yazmayabiriz ama fark anlasilmasi icin bu sekilde yazdim.
df.sort_values("1.",1) #Satiri bu sekilde siralayabilir.Default degereri ascending=True bu kucukten buyuge siralama yapmak icin,inplace=False,kind='quicksort'  siralama alforitmasini degistirebiliyoruz.
df.sort_values("1.",1,False) #ascending false yapiyoruz ve buyukten kucuge siralanmasini sagliyoruz.
df.sort_values("1.",1,"insertionsort") #Burda default olarak quicksort vardi bunu biz ayni zamanda stable olsun dedik ve insertionsort algoritmasi kullanarak yapmasi icin bu islemi yaptik.
df = pd.DataFrame({"Ay" : ["Eylul","Temmuz","Temmuz","Ocak","Ocak","Temmuz","Eylul","Ocak","Eylul"],"Sehir":["Konya","Konya","Konya","Istanbul","Istanbul","Istanbul","Ordu","Ordu","Ordu"],"Nem":[10,25,50,21,47,60,30,80,75]})
df.pivot_table(index = "Ay", columns = "Sehir", values = "Nem")
dataset = pd.read_csv("dosya_adi.csv") #csv dosyalarin okumak icin bu sekilde yapiyoruz.
changed.to_csv("dosya_adi.csv") #Kendimiz bir csv dosyasi olusturmak icin bu sekilde yapiyoruz.Degisiklik yapmis olabiliriz ilgili DataFrame to_csv ile csv  dosyasina donusturuyoruz.
changed.to_csv("dosya_adi.csv", index = False) #index degerlerini almadan kaydetmek icin yapiyoruz.
dataset = pd.read_html("url") #Internet sayfasindaki bir tabloyu bu sekilde okuyabiliriz.
dataset = pd.read_html("url", header = 0) #Tablonun basligini bir tablo degeri olarak alabiliyor bu sekilde basligi ilk satir yapip daha dogru bir okuma yapabilirsiniz.

dosya_ok = pd.read_fileFormat("dosya_adi.fileFormat") #Sadece csv degil bircok dosya formatinida okuyabiliyoruz.
dosya_ok.to_fileFormat("dosya_adi.fileFormat") #Yine ayni sekilde okudugumuz gibi bircok yosya formatiyla kaydetmek mumkun.
#Fakat fileFormat yerine ozel bir yazim olabilir arastirmanizda yarar var fakat genel gosterim olmasi adina bu sekilde yazildi.

#Matplotlib ile Veri Gorsellestirme
import matplotlib.pyplot as plt #Matplotlib kutuphanesini import etmek icin.
%matplotlib inline #jupyter notebook kullandigimizda veri gorsellestirmeyi gormek icin ekelememiz gerekiyor.
plt.show() #Dosya kullandigimizda veri gorsellestirmeyi gormek icin ekelememiz gerekiyor.
x = [0,1,2,3,4]
y = [0,1,4,9,16]
plt.plot(x,y,"blue") #plot() cizme islemi icin ornekte x ve y olarak verdigimiz kordinatlarda cizme islemi yapacak.Cizimdeki renk ornekte blue ama istedgimiz bir renk verebiliriz.RGB kodu olarak girebiliriz.
plt.show() #Jupyter notebook bunu eklemesek calisiyor fakat farkli dosyadan okuyan olabilir icin
plt.subplot(2,2,1) #satir,stun.index degeri olarak veriyoruz bu sekilde 4 tane grafik cizebiliyoruz.
plt.plot(x,y,"black")
plt.subplot(2,2,2) #satir ve stun degerleri buyudukce grafik dahada kuculuyor.2 den kucuk satir ve stun degerlerde ondalik sayilarda hata veriyor.
plt.plot(x,y,"blue")
plt.subplot(2,2,3)
plt.plot(x,y,"green")
plt.subplot(2,2,4) 
plt.plot(x,y,"orange")
plt.show()

fig = plt.figure() #Bir figure olusturmak icin yapiyoruz.
fig = plt.figure(figsize = (5,5)) #figsize ile grafigin boyutunu belirleyebiliriz.
axes = fig.add_axes([0.1,0.1,0.5,0.5]) #Bir grafik eklemek icin yapiyoruz.
#      soldan ne kadar icired olacak,asagidan ne kadar iceride olacak,x duzleminde ne kadar buyuklugu olacak,y duzleminde ne kadar buyuklugu olacak.
axes.set_xlabel("X Kordinati") #x kordinatinda bilgi yazisi gibi dusunebiliriz.
axes.set_ylabel("Y Kordinati") #y kordinatinda bilgi yazisi gibi dusunebiliriz.
axes.set_title("Ilk Grafik")   #Grafigin ust kisminda tablonun  bilgi yazisi gibi dusunebiliriz.
fig,axes = plt.subplots(2,2) #4 tane grafik olusturmak icin yaptik.
plt.tight_layout() #Bu islem grafiklerin arasinda bosluk olmasini sagliyor.
fig,axes = plt.subplots(2,1) #2 tane grafik cizdirdik.
axes[0].plot(x,y) #1.Grafik icin cizim yaptik
axes[1].plot(x,y) #2.Grafik icin cizim yaptik
for ax in axes:#Yukaridaki iki islemi bir for dongusuyle yapilabilir.
    ax.plot(x,y)
plt.show()
fig,axes = plt.subplots(2,1,figsize = (10,10)) #Bu sekilde de grafik boyutu belirlenebilir.
fig.savefig("fig1.jpg") #Bu grafikleri kaydetmek istersek yine benzer sekilde istedigimiz formatta kaydetmek mumkun.Burda normal dosya uzantilari seklinde yazmamiz yeterlidir.
plt.plot(x2,y2,"#00ff00") #Ayni grafikte birden fazla cizim yapilabilir.
fig = plt.figure(figsize = (5,5))
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,"yellow",lw = 10,label = "Dogrusal Grafik") #lw cizimin kalinligini ayarlamaya yariyor.lw yerine linewidht yazilabilir biz kisa oldugu icin lw kullandik.
axes.plot(x2,y2,"blue",label ="Dikey Grafik") #label ile isim cizime isim veriyoruz legend ile gozukecek.
axes.plot(x2,y2,"blue",lw = 5, ls = "--",label ="Dikey Grafik") #ls cizimin nasil gozukmesini istedigimizi belirtmek icin kullaniyoruz yine ls yerine linestyle kullanabiliriz.":" noktali cizim icin , "--" cizikli cizim icin, "-." hem kesikli hem noktali bir cizim icin
axes.plot(x2,y2,"blue",lw = 5, ls = "--",marker = "o", label ="Dikey Grafik") #Marker adindan anlasilacagi gibi isaretleme yapiyor x kordinatindaki degerleri "o" daire icine aliyor.
axes.plot(x2,y2,"blue",lw = 5,marker = "o",markersize = 8,markerfacecolor = "black", label ="Dikey Grafik") #markersize ile isaretleri cizim boyutunu istedigimiz bir degerde yapabiliriz.markarcolor ile isaretlmeye renk varabiliriz.Ayni renk olduklari icin tam net gozukmuyor.
axes.plot(x2,y2,"blue",lw = 5,marker = "o",markersize = 8,markerfacecolor = "black",markeredgecolor = "green", markeredgewidth = 5,label ="Dikey Grafik") #markeredgecolor ile kenarin renk verebiliriz.markeredgewidth
axes.legend() #Bu grafigin sol ust kosesinde cizimleri renk olarak ve label ismine gore tanitim icin ekliyor.
plt.tight_layout()
plt.show()
axes.set_xlim(0,10) #x kordinatinin hangi degerler kadar olacagini burda giriyoruz.Bunlari bir cizim farkli bir degerde basliyorsa grafigi buyutmek icin kullanilabilir.Cizimlerin degrelerinden kucuk verilrse bu seferde o degere kadar cizilecek ve orda bitecek.
axes.set_ylim(0,20) #y kordinatinin hangi degerler kadar olacagini burda giriyoruz.Bu sekilde grafik buyutulurse okuma islemi degisebiliyor noktalarin bazilarinin yerine farkli geliyor ayni oranda bir buyume olmasi icin kullanim nasil olacaksa o sekilde duzenleyebilirsiniz.

#Garbage Collector(gc)
gc.enable() #Otomatik gc calismasini etkinlestirmek icin 
gc.disable() #Otomatik gc calismasini devre disi icin bazi özel manuel  islemler icin otomatik secenek kapatilabilir.
gc.get_objects(generation=None) #Toplayıcı tarafından izlenen tüm nesnelerin bir listesini döndürür, döndürülen liste hariçtir. Generation None değilse, yalnızca o nesildeki toplayıcı tarafından izlenen nesneleri döndür.
gc.is_tracked(obj) #Nesne şu anda çöp toplayıcı tarafından izleniyorsa True, aksi takdirde False döndürür.
gc.is_finalized (obj) #Verilen nesne çöp toplayıcı tarafından sonlandırılmışsa True döndürür, aksi takdirde False.
gc.get_stats()
gc.garbage
gc.DEBUG_STATS #Toplama sırasında istatistikleri yazdırın. Bu bilgi, toplama sıklığını ayarlarken faydalı olabilir.
gc.DEBUG_COLLECTABLE
gc.DEBUG_UNCOLLECTABLE
gc.DEBUG_LEAK

#hashlib
import hashlib
hashlib.new(name, [data, ]*, usedforsecurity=True) #Ornek  h = hashlib.new('ripemd160') 
hash.digest_size #Ortaya çıkan karmanın bayt cinsinden boyutu.
hash.block_size #Karma algoritmanın bayt cinsinden dahili blok boyutu.
hash.name #Bu hash'in kanonik adı, her zaman küçük harflidir ve bu türden başka bir hash oluşturmak için new () için bir parametre olarak her zaman uygundur.
hash.update(data) #Hash nesnesini bayt benzeri nesneyle güncelleyin. Tekrarlanan çağrılar, tüm bağımsız değişkenlerin birleştirildiği tek bir çağrıya eşdeğerdir: m.update (a); m.update (b), m.update (a + b) 'ye eşdeğerdir.
hash.digest() #Şimdiye kadar update () yöntemine iletilen verilerin özetini döndür. Bu, Digest_size boyutunda bir bayt nesnesidir ve 0 ile 255 aralığındaki tüm baytları içerebilir.
hash.hexdigest() #Digest () gibi, tek fark, yalnızca onaltılık rakamları içeren, çift uzunlukta bir dize nesnesi olarak döndürülür. Bu, e-posta veya diğer ikili olmayan ortamlarda değeri güvenli bir şekilde değiştirmek için kullanılabilir.Daha cok bu yontem kullanilir.
hash.copy() #Karma nesnenin bir kopyasını ("clone") döndürür. Bu, ortak bir ilk alt dizeyi paylaşan verilerin özetlerini verimli bir şekilde hesaplamak için kullanılabilir.
hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) #Ornek dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
hashlib.scrypt(password, *, salt, n, r, p, maxmem=0, dklen=64)
hashlib.algorithms_available #Python da haslib kutuphanesinin destekledigi algoritmalari gosterir.
hashlib.algorithms_guaranteed #Garanti verilen hash islemi algoritmalarini listeler md5 aciklar nedeniyle yukarida listelensede bu listede yoktur.

h = hashlib.sha256()
h.update(b"Bu sifreli bir mesajdir.")
h.hexdigest()
