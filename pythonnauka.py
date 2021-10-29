# zadanie 1
lorem = """Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"""

# zadanie 2
imie = "Filip"
nazwisko = "Warpechowski"

liczba_liter1 = lorem.count(imie[2])
liczba_liter2 = lorem.count(nazwisko[3])


print(imie+" "+nazwisko+"\n")
print("W tekście jest %i liter %s oraz %i liter %s \n" % (liczba_liter1,imie[2], liczba_liter2, nazwisko[3]))


#zadanie 3
slowo = "przykładowy"
liczba = 420
print('{:_<20}'.format(slowo))
print('{:_>20}'.format(slowo))
print('{:_^20}'.format(slowo))
print('{:>20.5}'.format(slowo))
print('{:+d}'.format(liczba))

#zadanie 4
zad = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print(dir(zad))
help(zad.center)

#zadanie 5
imie2 = "Filip"[::-1]
nazwisko2 = "Warpechowski"[::-1]
print(imie2)
print(nazwisko2)
print("\n")

#zadanie 6
lista = [1,3,5,7,9,2,4,6,8,10]
lista2 = lista[5:]
print(lista2)
del lista[5:]
print(lista)
print("\n")

#zadanie 7
lista.extend(lista2)
print(lista)
lista.insert(0,0)
print(lista)
kopia = lista.copy()
print(kopia)
lista.sort()
print(lista)
print("\n")

#zadanie 8

index = (123456,234567,345678,456789,567890)
im_i_naz = ("Filip warpechowski","Olaf Nowak", "Zenek Martyniuk","Michał Wiśniewski","Marta Łapszo")
dane = index, im_i_naz
print(dane[0][0],dane[1][0])
print(dane[0][1],dane[1][1])
print(dane[0][2],dane[1][2])
print(dane[0][3],dane[1][3])
print(dane[0][4],dane[1][4])
print("\n")

#zadanie 9

słownik={
    "imie":"Filip",
    "Nazwisko":"Warpechowski",
    "index":"123456"
}
print(słownik)
słownik["wiek"]="21"
słownik["email"]="ziritto@gmail.com"
słownik["rok urodzenia"]="1999"
słownik["adres"]="Jana Pawła 2/31"
print(słownik)
print("\n")

#zadanie 10
numery = ["111222333","444555666","777888999","123456789","987654321","111222333"]
print(numery)
bez_powtorzen=set(numery)
print(bez_powtorzen)
print("\n")

#zadanie 11
for i in range(1,11):
    print(i)
print("\n")

#zadanie 12
for i in range(100,19,-5):
    print(i)
print("\n")
#zadanie 13






