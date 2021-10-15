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
