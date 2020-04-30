#Kodun geri kalanını tamamlayıp kodu güncelleyeceğim ...
#English version is coming.I am completing the code .When finished i will share ...

import random
puan=0

while True:
    print("""
Matematik Egzersiz Programına Hoşgeldiniz
Toplama İçin  1
Çıkarma İçin  2
Çarpma İçin   3
Bölme İçin    4
Çıkış q""")
    seçim=input("Seçiminizi girin")
    if seçim == "1":
        print("""
Kolay Mod  1
Orta Mod  2
Zor Mod   3""")
        seçimtop=input("Seçiminizi Girin")
        if seçimtop=="1":
            while True:
                kolaytop1=random.randint(1,15)
                kolaytop2=random.randint(0,15)
                cevaptopkolay=kolaytop1+kolaytop2
                print(kolaytop1,"+",kolaytop2,"=")
                giriştopkolay=int(input("Cevap"))
                print("Doğru Cevap",giriştopkolay)
                if giriştopkolay==cevaptopkolay:
                    puan+=2
                elif giriştopkolay==000:
                    print("puanınız",puan)
                    break
                else:puan-=1
        elif seçimtop=="2":
            while True:
                ortatop1=random.randint(10,55)
                ortatop2=random.randint(15,60)
                cevaptoporta=ortatop1+ortatop2
                print(ortatop1,"+",ortatop2,"=")
                giriştoporta=int(input("Cevap"))
                print("Doğru Cevap",cevaptoporta)
                if giriştoporta==cevaptoporta:
                    puan+=3
                elif giriştoporta==000:
                    print("puanınız",puan)
                    break
                else:
                    puan-=2
        elif seçimtop=="3":
            while True:
                zortop1=random.randint(55,150)
                zortop2=random.randint(75,170)
                cevaptopzor=zortop1+zortop2
                print(zortop1,"+",zortop2,"=")
                giriştopzor=int(input("Cevap"))
                print("Doğru Cevap",cevaptopzor)
                if giriştopzor==cevaptopzor:
                    puan+=5
                elif giriştopzor==000:
                    print("puanınız",puan)
                    break
                else:
                    puan-=3
    elif seçim =="2":
        print("""
Kolay Mod  1
Orta Mod  2
Zor Mod   3""")
        seçimçık=input("Seçiminizi girin")
        if seçimçık=="1":
            while True:
                kolayçık1=random.randint(-5,15)
                kolayçık2=random.randint(-5,15)
                cevapçıkkolay=kolayçık1-kolayçık2
                print(kolayçık1,"-",kolayçık2,"=")
                girişçıkkolay=int(input("Cevap"))
                print("Doğru Cevap",cevapçıkkolay)
                if girişçıkkolay==cevapçıkkolay:
                    puan+=2
                elif girişçıkkolay==000:
                    print("puanınız",puan)
                    break
                else:
                    puan-=1
        elif seçimçık=="2":
            while True:
                ortaçık1=random.randint(-15,45)
                ortaçık2=random.randint(-15,25)
                cevapçıkorta=ortaçık1-ortaçık2
                print(ortaçık1,"-",ortaçık2,"=")
                girişçıkorta=int(input("Cevap"))
                print("Doğru Cevap",cevapçıkorta)
                if girişçıkorta==cevapçıkorta:
                    puan+=4
                elif girişçıkorta==000:
                    print("puanınız",puan)
                    break
                else:
                    puan-=2
        elif seçimçık=="3":
            while True:
                zorçıkçık1=random.randint(-20,150)
                zorçık2=random.randint(-50,150)
                cevapçıkzor=zorçık1-zorçık2
                print(zorçık1,"-",zorçık2,"=")
                girişçıkzor=int(input("Cevap"))
                print("Doğru Cevap",cevapçıkzor)
                if girişçıkzor==cevapçıkzor:
                    puan+=6
                elif girişçıkzor==000:
                    print("puanınız",puan)
                    break
                else:
                    puan-=3


    elif seçim=="q":
        break
                    
        
