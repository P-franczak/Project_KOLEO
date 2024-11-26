from enum import Enum


class Stacja(Enum):
    Wolbrom = 0
    Olkusz = 1
    Bukowno = 2
    Katowice = 3
    Katowice_Zawodzie = 4
    Katowice_Szopienice_Południowe = 5
    Mysłowice = 6
    Jaworzno_Szczakowa = 7
    Jaworzno_Ciężkowice = 8
    Balin = 9
    Czechowice_Dziedzice = 10
    Kaniów = 11
    Dankowice = 12
    Jawiszowice_Jaźnik = 13
    Brzeszce_Jawiszowice = 14
    Brzeszcze = 15
    Oświęcim = 16
    Gorzów_Chrzanowski = 17
    Chełmek = 18
    Libiąż = 19
    Chrzanów = 20
    Chrzanów_Śródmieście = 21
    Trzebinia = 22
    Dulowa = 23
    Wola_Filipowska = 24
    Krzeszowice = 25
    Rudawa = 26
    Zabierzów = 27
    Zabierzów_Rząska = 28
    Kraków_Mydlniki_Wapiennik = 29
    Kraków_Mydlniki = 30
    Kraków_Bronowice = 31
    Kraków_Łobzów = 32
    Kraków_Główny = 33
    Kraków_Płaszów = 34
    Tarnów = 35
    Dębica = 36


lista_sasiedztwa = {}

# stacja z której odjazd = [stacja do której jedzie, numer pociągu, godzina odjazdu]
lista_sasiedztwa[Stacja.Katowice] = [Stacja.Katowice_Zawodzie, "43300/1", "04:31"]
lista_sasiedztwa[Stacja.Katowice_Zawodzie] = [
    Stacja.Katowice_Szopienice_Południowe,
    "43300/1",
    "04:37",
]
lista_sasiedztwa[Stacja.Katowice_Szopienice_Południowe] = [
    Stacja.Mysłowice,
    "43300/1",
    "04:41",
]
lista_sasiedztwa[Stacja.Mysłowice] = [Stacja.Jaworzno_Szczakowa, "43300/1", "04:51"]
lista_sasiedztwa[Stacja.Jaworzno_Szczakowa] = [
    Stacja.Jaworzno_Ciężkowice,
    "43300/1",
    "05:01",
]
lista_sasiedztwa[Stacja.Jaworzno_Ciężkowice] = [Stacja.Balin, "43300/1", "05:06"]
lista_sasiedztwa[Stacja.Balin] = [Stacja.Trzebinia, "43300/1", "05:10"]
lista_sasiedztwa[Stacja.Trzebinia] = [Stacja.Dulowa, "43300/1", "05:15"]
lista_sasiedztwa[Stacja.Dulowa] = [Stacja.Wola_Filipowska, "43300/1", "05:19"]
lista_sasiedztwa[Stacja.Wola_Filipowska] = [Stacja.Krzeszowice, "43300/1", "05:22"]
lista_sasiedztwa[Stacja.Krzeszowice] = [Stacja.Rudawa, "43300/1", "05:26"]
lista_sasiedztwa[Stacja.Rudawa] = [Stacja.Zabierzów, "43300/1", "05:31"]
lista_sasiedztwa[Stacja.Zabierzów] = [Stacja.Zabierzów_Rząska, "43300/1", "05:35"]
lista_sasiedztwa[Stacja.Zabierzów_Rząska] = [
    Stacja.Kraków_Mydlniki_Wapiennik,
    "43300/1",
    "05:38",
]
lista_sasiedztwa[Stacja.Kraków_Mydlniki_Wapiennik] = [
    Stacja.Kraków_Mydlniki,
    "43300/1",
    "05:41",
]
lista_sasiedztwa[Stacja.Kraków_Mydlniki] = [Stacja.Kraków_Bronowice, "43300/1", "05:43"]
lista_sasiedztwa[Stacja.Kraków_Bronowice] = [Stacja.Kraków_Łobzów, "43300/1", "05:45"]
lista_sasiedztwa[Stacja.Kraków_Łobzów] = [Stacja.Kraków_Główny, "43300/1", "05:48"]


print(lista_sasiedztwa[Stacja.Balin])
