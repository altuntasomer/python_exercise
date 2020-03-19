#Alan ve Hacim Hesaplayıcı - Area and Volume Calculator 

pi=3.141592
dil=input("Türkçe İçin 1- For English 2")
if dil=="1":
    print("Çeviriciye Hoşgeldin")
    while(True):
        print("-"*30)
        secimilk = input("Alan için 1 Hacim için 2 yi tuşlayınız")
        if secimilk=="1":
            secimiki = input("Kare için--------> k\nDikdörtgen için--> dd\nDaire için--------> d\nÜçgen için-------> ü")
            if secimiki =="k":
                karekenar=float(input("kenar uzunluğunu girin"))
                karealan=karekenar*karekenar
                print("karenin alanı:",karealan)
            elif secimiki=="dd":
                dikdörtgenukenar=float(input("bir kenar uzunluğu giriniz"))
                dikdörtgenkkenar=float(input("ilk yazdığınız kenara dik olan kenarın uzunluğunu giriniz"))
                dikdörtgenalan=dikdörtgenukenar*dikdörtgenkkenar
                print("dikdörtgenin alanı:",dikdörtgenalan)
            elif secimiki=="d":
                yarıcap=float(input("yarıçapı giriniz"))
                dairealan=pi*yarıcap*yarıcap
                print("dairenin alanı:",dairealan)
        elif secimilk== "2":
            secimuc= input("Küp için --------->1\nDikdörtgenler Prizması için-->2\nSilindir için----->3\nKoni------->4 için\nKüre için------->5")
            if secimuc=="1":
                kupkenar=float(input("bir kenar uzunluğunu giriniz"))
                kupalan=kupkenar**3
                print("Küpün Alanı:",kupalan)
            elif secimuc=="2":
                dikdörtgenkenarilk= float(input("Kenarlardan birini girin"))
                dikdörtgenkenariki= float(input("ilk kenara dik olan kenarlardan birini girin"))
                dikdörtgenkenaruc= float(input("diğer iki kenara dik olan kenarı girin"))
                dikdörtgenhacim= dikdörtgenkenarilk*dikdörtgenkenariki*dikdörtgenkenaruc
                print("dikdörtgenin hacmi:",dikdörtgenhacim)
            elif secimuc=="3":
                silindiryarıcap=float(input("silindirin yarıçapını girin"))
                silindiralan=silindiryarıcap*silindiryarıcap*pi
            silindiryukseklik=float(input("silindirin yuksekliğini girin"))
            silindirhacim=silindiralan*silindiryukseklik
            print("silindirin hacmi:",silindirhacim)
        
        elif secimuc=="4":
            koniyarıcap=float(input("koninin yarıçapını girin"))
            konialan=koniyarıcap*koniyarıcap*pi
            koniyukseklik=float(input("koninin yüksekliğini girin"))
            konihacim=konialan*koniyukseklik/3
            print("koninin hacmi:",konihacim)
            
        elif secimuc=="5":
            kureyarıcap=float(input("kürenin yarıçapını girin"))
            kurehacim=4/3*pi*kureyarıcap**3
            print("kurenin hacmi:",kurehacim)
            
elif dil=="2": 
     print("Welcome the Converter")    
     while(True):
        print("-"*30)
        secimilk = input("Calculate Area-> 1\nCalculate Volume-> 2 ")
        if secimilk=="1":
            secimiki = input("Calculate the Square--------> 1\nCalculate the Rectangle--> 2\nCalculate the Circle--------> 3")
            if secimiki =="1":
                karekenar=float(input("Enter the Edge Lenght"))
                karealan=karekenar*karekenar
                print("Square Area:",karealan)
            elif secimiki=="2":
                dikdörtgenukenar=float(input("Enter a Edge Lenght"))
                dikdörtgenkkenar=float(input("Enter the Lenght of the Edge Perpendicular to the Edge You Entered First"))
                dikdörtgenalan=dikdörtgenukenar*dikdörtgenkkenar
                print("Rectangle Area:",dikdörtgenalan)
            elif secimiki=="3":
                yarıcap=float(input("Enter the Radius"))
                dairealan=pi*yarıcap*yarıcap
                print("Circle Area:",dairealan)
        elif secimilk== "2":
            secimuc= input("Calculate the Cube --------->1\nCalculate the Rectangles Prism-->2\nCalculate the Cylinder----->3\nCalculate the Cone------->4 \nCalculate the Sphere------->5")
            if secimuc=="1":
                kupkenar=float(input("Enter the Edge Lenght"))
                kupalan=kupkenar**3
                print("Volume of Cube:",kupalan)
            elif secimuc=="2":
                dikdörtgenkenarilk= float(input("Enter a Edge Lenght"))
                dikdörtgenkenariki= float(input("Enter the Lenght of the Edge Perpendicular to the Edge You Entered First"))
                dikdörtgenkenaruc= float(input("Enter the Side That is Perpendicular to the Other Two Sides"))
                dikdörtgenhacim= dikdörtgenkenarilk*dikdörtgenkenariki*dikdörtgenkenaruc
                print("Volume of Rectangles Prism:",dikdörtgenhacim)
            elif secimuc=="3":
                silindiryarıcap=float(input("Enter the Radius of Cylinder"))
                silindiralan=silindiryarıcap*silindiryarıcap*pi
                silindiryukseklik=float(input("Enter the Height Cylinder"))
                silindirhacim=silindiralan*silindiryukseklik
                print("Volume of Cylinder:",silindirhacim)
        
            elif secimuc=="4":
                koniyarıcap=float(input("Enter the Radius of Cone"))
                konialan=koniyarıcap*koniyarıcap*pi
                koniyukseklik=float(input("Enter the Height of Cone"))
                konihacim=konialan*koniyukseklik/3
                print("Volume of Cone:",konihacim)
            
            elif secimuc=="5":
                kureyarıcap=float(input("Enter the Radius of Sphere"))
                kurehacim=4/3*pi*kureyarıcap**3
                print("Volume of Sphere:",kurehacim)
