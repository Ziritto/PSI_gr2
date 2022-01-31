from file_manager import FileManager

def zad1(a_list, b_list):
    lista = []
    for i in a_list:
        if ((a_list.index(i)) % 2 == 0):
            lista.append(i)
    for i in b_list:
        if ((b_list.index(i)) % 2 == 1):
            lista.append(i)
    print(lista)
    return lista

a_list = ["0", "1", "2", "3", "4"]
b_list = ["5", "6", "7", "8", "9"]
zad1(a_list, b_list)
print("--------------------------")

def zad2(data_text):
    dict = {}
    word_len = len(data_text)
    letters = []
    letters[:0] = data_text
    word_upper = data_text.upper()
    word_smaller = data_text.lower()

    dict['lenght'] = word_len
    dict['letters'] = letters
    dict['big_letters'] = word_upper
    dict['smaller_letters'] = word_smaller
    print(dict)
    return dict

data_text="Filip Warpechowski"
zad2(data_text)
print("--------------------------")


def zad3(text, letter):
    wynik = text.replace(letter, "")
    print(wynik)
    return wynik

zad3("ala ma kota a kot ma ale",'a')
print("--------------------------")

def zad4():
    y = input("Podaj temerture: ")
    print("na jaką jedostkę zamienić?")
    x = input("1:Kelwin, 2:Rankine, 3:Fahrenheit ")
    wybor = ["1", "2", "3"]
    if (x not in wybor):
        print("nie ma takiej opcji")
    else:
        if str(x) == "1":
            Kelwin = int(y) + 273.15
            print("Kelwina -" + str(Kelwin))
        elif str(x) == "2":
            Rankine = (int(y) + 273.15) * 1.8
            print("Rankine -" + str(Rankine))
        elif str(x) == "3":
            Fahrenheit = ((int(y) * 2) + 32) * 0.9
            print("Fahrenheita -" + str(Fahrenheit))
#zad4()

# zad4()

class calculator:
    def add(x, y):
        wynik=x+y
        return wynik
    def difference(x, y):
        wynik=x-y
        return wynik
    def multiply(x, y):
        wynik=x*y
        return wynik
    def divide(x, y):
        wynik=x/y
        return wynik

class ScienceCalculator(calculator):
    def pow(x,y):
        wynik=pow(x,y)
        return wynik

def zad7(x):
    print((x[::-1]))

zad7("Filip")

FileManager.update_file("aaa.txt")
FileManager.read_file("aaa.txt")