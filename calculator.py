#Hesap Makinesi-Calculator


def topla(x, y):
    return x + y

def çıkar(x, y):
    return x - y

def çarp(x, y):
    return x * y

def böl(x, y):
    return x / y
sayi1 = float(input(""))
islem = input("")
sayi2 = float(input(""))
if islem == "+":
    print(topla(sayi1,sayi2))
    
elif islem == "-":
    print(çıkar(sayi1,sayi2))

elif islem == "*":
    print(çarp(sayi1,sayi2))

elif islem == "/":
    print(böl(sayi1,sayi2))
