#zad 1

lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMake"
print("------------------------------------------")

#zad 2

imie = 'Filip'
nazwisko = 'Warpechowski'

litera1 = imie[2]
litera2 = nazwisko[3]

print('w tekscie jest {} liter {} i {} liter {}'.format(lorem.count(
    litera1), litera1, lorem.count(litera2), litera2))
print("------------------------------------------")

#zad 3

print("Filip {} Kamil {}".format(1, 2))
print('{:>20}'.format('Filip'))
print('{:^20}'.format('Filip'))
print('{:.5}'.format('przykładowy tekst'))
print("------------------------------------------")

#zad 4
string = "Ala ma kota a kot ma Ale"
print(dir(string))
help(string.count("a"))
print("------------------------------------------")

#zad 5
imie = "Filip Warpechowski"
print(imie[::-1])
print("------------------------------------------")

#zad 6 i 7
lista = [i for i in range(1, 11)]
print(lista)
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)
polaczone = [0] + lista + lista2
print(polaczone)
lista3 = polaczone
lista3.sort(reverse=True)
print(lista3)
print("------------------------------------------")

#zad 8
krotka = ("Filip Warpechowski", 155661, "Kamil Nowak", 121212, "Jak Kowalski", 343434, "Kamil Stoch", 123456)
print("------------------------------------------")

#zad 9
slownik = dict([("Filip Warpechowski", 155661), ("Kamil Nowak", 121212), ("Jak Kowalski", 343434),( "Kamil Stoch", 123456)])
print(slownik)
print("------------------------------------------")

#zad 10
lista = [
    "123123123",
    "123123123",
    "111222333",
    "222111333",
    "333222111",
    "321232132",
    "111222333",
    "213213213"
]
print(lista)
lista = list(set(lista))
print(lista)
print("------------------------------------------")

#zad 11
for i in range(1,11, 1):
    print(i)
print("------------------------------------------")

#zad 12

for i in range(100,19, -5):
    print(i)
print("------------------------------------------")
