# =====================================================
# PLIK: tabu_search_kolej.py
# =====================================================

import random
import math
from enum import Enum
from datetime import datetime, timedelta
from collections import defaultdict, deque
import matplotlib.pyplot as plt

# -----------------------------
# 1. Enum oraz lista stacji
# -----------------------------
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

# Mapa enum -> nazwa stacji (string)
mapa_stacji = {
    Stacja.Wolbrom: "Wolbrom",
    Stacja.Olkusz: "Olkusz",
    Stacja.Bukowno: "Bukowno",
    Stacja.Katowice: "Katowice",
    Stacja.Katowice_Zawodzie: "Katowice Zawodzie",
    Stacja.Katowice_Szopienice_Południowe: "Katowice Szopienice Południowe",
    Stacja.Mysłowice: "Mysłowice",
    Stacja.Jaworzno_Szczakowa: "Jaworzno Szczakowa",
    Stacja.Jaworzno_Ciężkowice: "Jaworzno Ciężkowice",
    Stacja.Balin: "Balin",
    Stacja.Czechowice_Dziedzice: "Czechowice Dziedzice",
    Stacja.Kaniów: "Kaniów",
    Stacja.Dankowice: "Dankowice",
    Stacja.Jawiszowice_Jaźnik: "Jawiszowice Jaźnik",
    Stacja.Brzeszce_Jawiszowice: "Brzeszce Jawiszowice",
    Stacja.Brzeszcze: "Brzeszcze",
    Stacja.Oświęcim: "Oświęcim",
    Stacja.Gorzów_Chrzanowski: "Gorzów Chrzanowski",
    Stacja.Chełmek: "Chełmek",
    Stacja.Libiąż: "Libiąż",
    Stacja.Chrzanów: "Chrzanów",
    Stacja.Chrzanów_Śródmieście: "Chrzanów Śródmieście",
    Stacja.Trzebinia: "Trzebinia",
    Stacja.Dulowa: "Dulowa",
    Stacja.Wola_Filipowska: "Wola Filipowska",
    Stacja.Krzeszowice: "Krzeszowice",
    Stacja.Rudawa: "Rudawa",
    Stacja.Zabierzów: "Zabierzów",
    Stacja.Zabierzów_Rząska: "Zabierzów Rząska",
    Stacja.Kraków_Mydlniki_Wapiennik: "Kraków Mydlniki Wapiennik",
    Stacja.Kraków_Mydlniki: "Kraków Mydlniki",
    Stacja.Kraków_Bronowice: "Kraków Bronowice",
    Stacja.Kraków_Łobzów: "Kraków Łobzów",
    Stacja.Kraków_Główny: "Kraków Główny",
    Stacja.Kraków_Płaszów: "Kraków Płaszów",
    Stacja.Tarnów: "Tarnów",
    Stacja.Dębica: "Dębica",
}

# -----------------------------
# 2. Oryginalna struktura kolejowa
#    (słownik: Stacja -> lista [StacjaDocelowa, nr_pociągu, godz_odjazdu])
# -----------------------------
lista_sasiedztwa_enum = {
    st: [] for st in Stacja
}

# Poniżej: wklej dokładnie to, co podałeś w pytaniu:
# Pociąg 1
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30750/1", "03:38"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append([Stacja.Chełmek, "30750/1", "03:43"])
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30750/1", "03:46"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30750/1", "03:51"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30750/1", "03:56"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30750/1", "03:59"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30750/1", "04:02"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "30750/1", "04:07"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30750/1", "04:11"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30750/1", "04:14"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30750/1", "04:19"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Zabierzów_Rząska, "30750/1", "04:24"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [
        Stacja.Kraków_Mydlniki_Wapiennik,
        "30750/1",
        "04:27",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [
        Stacja.Kraków_Mydlniki,
        "30750/1",
        "04:30",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "30750/1", "04:32"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "30750/1", "04:34"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "30750/1", "04:37"]
)

# Pociąg 2
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30753", "04:28"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30753", "04:34"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Zabierzów_Rząska, "30753", "04:39"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [
        Stacja.Kraków_Mydlniki_Wapiennik,
        "30753",
        "04:42",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [
        Stacja.Kraków_Mydlniki,
        "30753",
        "04:45",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "30753", "04:47"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "30753", "04:50"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append([Stacja.Kraków_Główny, "30753", "04:53"])

# Pociąg 3
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30754/5", "04:19"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append([Stacja.Chełmek, "30754/5", "04:24"])
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30754/5", "04:27"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30754/5", "04:32"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30754/5", "04:37"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30754/5", "04:39"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30754/5", "04:43"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "30754/5", "04:48"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30754/5", "04:51"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30754/5", "04:55"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30754/5", "05:00"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Zabierzów_Rząska, "30754/5", "05:05"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [Stacja.Kraków_Mydlniki_Wapiennik, "30754/5", "05:08"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [
        Stacja.Kraków_Mydlniki,
        "30754/5",
        "05:11",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "30754/5", "05:13"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "30754/5", "05:15"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "30754/5", "05:18"]
)

# Pociąg 4
lista_sasiedztwa_enum[Stacja.Katowice].append([Stacja.Katowice_Zawodzie, "43300/1", "04:31"])
lista_sasiedztwa_enum[Stacja.Katowice_Zawodzie].append(
    [
        Stacja.Katowice_Szopienice_Południowe,
        "43300/1",
        "04:37",
    ]
)
lista_sasiedztwa_enum[Stacja.Katowice_Szopienice_Południowe].append(
    [
        Stacja.Mysłowice,
        "43300/1",
        "04:41",
    ]
)
lista_sasiedztwa_enum[Stacja.Mysłowice].append(
    [Stacja.Jaworzno_Szczakowa, "43300/1", "04:51"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [
        Stacja.Jaworzno_Ciężkowice,
        "43300/1",
        "05:01",
    ]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Ciężkowice].append([Stacja.Balin, "43300/1", "05:06"])
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "43300/1", "05:10"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "43300/1", "05:15"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "43300/1", "05:19"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "43300/1", "05:22"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "43300/1", "05:26"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "43300/1", "05:31"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Zabierzów_Rząska, "43300/1", "05:35"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [
        Stacja.Kraków_Mydlniki_Wapiennik,
        "43300/1",
        "05:38",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [
        Stacja.Kraków_Mydlniki,
        "43300/1",
        "05:41",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "43300/1", "05:43"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "43300/1", "05:45"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "43300/1", "05:48"]
)

# Pociąg 5
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30756/7", "05:00"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append([Stacja.Chełmek, "30756/7", "05:06"])
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30756/7", "05:09"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30756/7", "05:15"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30756/7", "05:20"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30756/7", "05:22"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30756/7", "05:27"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "30756/7", "05:32"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30756/7", "05:36"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30756/7", "05:40"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30756/7", "05:46"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Zabierzów_Rząska, "30756/7", "05:51"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [Stacja.Kraków_Mydlniki_Wapiennik, "30756/7", "05:54"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [
        Stacja.Kraków_Mydlniki,
        "30756/7",
        "05:57",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "30756/7", "06:00"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "30756/7", "06:03"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "30756/7", "06:05"]
)

# Pociąg 6
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "33139", "04:28"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "33139", "04:53"])
lista_sasiedztwa_enum[Stacja.Bukowno].append([Stacja.Jaworzno_Szczakowa, "33139", "05:03"])
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append([Stacja.Trzebinia, "33139", "05:19"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "33139", "05:33"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "33139", "05:42"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Kraków_Bronowice, "33139", "05:55"])
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "33139", "06:02"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append([Stacja.Kraków_Główny, "33139", "06:09"])

# Pociąg 7
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30758/9", "06:19"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append([Stacja.Chełmek, "30758/9", "06:24"])
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30758/9", "06:27"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30758/9", "06:32"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30758/9", "06:37"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30758/9", "06:39"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30758/9", "06:43"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "30758/9", "06:48"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30758/9", "06:51"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30758/9", "06:55"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30758/9", "07:00"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Zabierzów_Rząska, "30758/9", "07:06"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [
        Stacja.Kraków_Mydlniki_Wapiennik,
        "30758/9",
        "07:08",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [
        Stacja.Kraków_Mydlniki,
        "30758/9",
        "07:11",
    ]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "30758/9", "07:13"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "30758/9", "07:15"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "30758/9", "07:18"]
)

# Pociąg 8
lista_sasiedztwa_enum[Stacja.Katowice].append([Stacja.Katowice_Zawodzie, "43800/1", "06:04"])
lista_sasiedztwa_enum[Stacja.Katowice_Zawodzie].append(
    [
        Stacja.Katowice_Szopienice_Południowe,
        "43800/1",
        "06:09",
    ]
)
lista_sasiedztwa_enum[Stacja.Katowice_Szopienice_Południowe].append(
    [
        Stacja.Mysłowice,
        "43800/1",
        "06:13",
    ]
)
lista_sasiedztwa_enum[Stacja.Mysłowice].append([Stacja.Jaworzno_Szczakowa, "43800/1", "06:22"])
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [
        Stacja.Jaworzno_Ciężkowice,
        "43800/1",
        "06:32",
    ]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Ciężkowice].append([Stacja.Balin, "43800/1", "06:36"])
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "43800/1", "06:41"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "43800/1", "06:48"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "43800/1", "06:52"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "43800/1", "06:55"]
)

# Pociąg 9
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Bukowno].append([Stacja.Jaworzno_Szczakowa, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append([Stacja.Trzebinia, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Kraków_Bronowice, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "33141", "06:04"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append([Stacja.Kraków_Główny, "33141", "06:04"])


# Pociąg 10
lista_sasiedztwa_enum[Stacja.Katowice].append([Stacja.Katowice_Zawodzie, "43100/1", "06:23"])
lista_sasiedztwa_enum[Stacja.Katowice_Zawodzie].append(
    [
        Stacja.Katowice_Szopienice_Południowe,
        "43100/1",
        "06:27",
    ]
)
lista_sasiedztwa_enum[Stacja.Katowice_Szopienice_Południowe].append(
    [
        Stacja.Mysłowice,
        "43100/1",
        "06:31",
    ]
)
lista_sasiedztwa_enum[Stacja.Mysłowice].append(
    [Stacja.Jaworzno_Szczakowa, "43100/1", "06:39"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [
        Stacja.Jaworzno_Ciężkowice,
        "43100/1",
        "06:48",
    ]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Ciężkowice].append(
    [Stacja.Trzebinia, "43100/1", "06:52"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "43100/1", "07:00"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "43100/1", "07:09"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Kraków_Bronowice, "43100/1", "07:18"])
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "43100/1", "07:30"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "43100/1", "07:32"]
)


# Pociąg 11
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "33143", "06:33"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "33143", "06:58"])
lista_sasiedztwa_enum[Stacja.Bukowno].append([Stacja.Jaworzno_Szczakowa, "33143", "07:07"])
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append([Stacja.Trzebinia, "33143", "07:22"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "33143", "07:34"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "33143", "07:43"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Kraków_Bronowice, "33143", "07:57"])
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "33143", "08:04"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append([Stacja.Kraków_Główny, "33143", "08:07"])


# Pociąg 12
lista_sasiedztwa_enum[Stacja.Czechowice_Dziedzice].append([Stacja.Kaniów, "43528", "06:40"])
lista_sasiedztwa_enum[Stacja.Kaniów].append([Stacja.Dankowice, "43528", "06:45"])
lista_sasiedztwa_enum[Stacja.Dankowice].append([Stacja.Jawiszowice_Jaźnik, "43528", "06:49"])
lista_sasiedztwa_enum[Stacja.Jawiszowice_Jaźnik].append(
    [Stacja.Brzeszce_Jawiszowice, "43528", "06:52"]
)
lista_sasiedztwa_enum[Stacja.Brzeszce_Jawiszowice].append(
    [Stacja.Brzeszcze, "43528", "06:56"]
)
lista_sasiedztwa_enum[Stacja.Brzeszcze].append([Stacja.Olkusz, "43528", "07:01"])



# itd. - Kontynuuj wklejanie wszystkich pociągów tak, jak w Twoim pliku:
# Pociąg 4, 5, 6, 7, 8, 9, 10, 11, 12:
# (skrócone tutaj - w praktyce wklej wszystko)

lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "33139", "04:28"])
# ... etc. ...

# -----------------------------
# 3. Konwersja do formatu Tabu Search
# -----------------------------
def stworz_format_tabu(lista_sasiedztwa_enum):
    """
    Zamienia oryginalny słownik (Stacja -> [[StacjaDocelowa, nr_pociagu, godz_odjazdu], ...])
    na słownik { "NazwaStacji": [ [start, end, czas_przejazdu, nr_pociagu], ... ] }
    gdzie 'start' i 'end' to stringi z nazwą stacji, a czas_przejazdu to np. stała = 5.
    """
    new_lista = defaultdict(list)

    for stacja_z, edges in lista_sasiedztwa_enum.items():
        stacja_z_str = mapa_stacji[stacja_z]
        for (stacja_do_enum, nr_pociagu, godz_odjazdu) in edges:
            stacja_do_str = mapa_stacji[stacja_do_enum]
            # Na potrzeby algorytmu przyjmujemy np. stały czas = 5
            czas_przejazdu = 5

            new_lista[stacja_z_str].append([
                stacja_z_str,      # stacja początkowa (string)
                stacja_do_str,     # stacja docelowa (string)
                czas_przejazdu,    # na razie stały
                nr_pociagu
            ])

    # Konwertuj defaultdict na zwykły dict
    return dict(new_lista)

# Tworzymy nowy słownik do Tabu Search
lista_sasiedztwa_enum = stworz_format_tabu(lista_sasiedztwa_enum)

# -----------------------------
# 4. Funkcje Tabu Search (z wcześniejszego przykładu)
# -----------------------------
def funkcja_celu(trasa):
    """
    Przykładowa funkcja celu: 
    - zlicza sumaryczny 'czas_przejazdu' (trasa[i][2])
    - zlicza liczbę przesiadek (gdy zmienia się nr pociągu).
    Tutaj przesiadki mnożone ×10, aby były bardziej "kosztowne".
    """
    czas_podrozy = sum(odcinek[2] for odcinek in trasa)
    liczba_przesiadek = sum(
        1 for i in range(1, len(trasa)) if trasa[i][3] != trasa[i - 1][3]
    )
    return czas_podrozy + liczba_przesiadek * 10

def znajdz_rozwiazanie_startowe(stacja_pocz, stacja_konc, lista_sasiedztwa_enum):
    """
    Przykładowa funkcja budująca trasę startową (dość losowa).
    Zwraca (trasa, [lista_nazw_stacji]).
    """
    # Dla uproszczenia – weźmy stację startową i 'błądźmy' aż trafimy na stację docelową.
    # Oryginalnie było to bardziej rozbudowane, tu można uprościć.

    sciezka = []
    aktualna = stacja_pocz
    visited = set([stacja_pocz])
    while aktualna != stacja_konc:
        sasiedzi = [s for s in lista_sasiedztwa_enum[aktualna] if s[1] not in visited]
        if not sasiedzi:
            # Jeśli nie mamy gdzie iść, przerwij
            break
        wybor = random.choice(sasiedzi)
        sciezka.append(wybor)
        visited.add(wybor[1])
        aktualna = wybor[1]

        if aktualna == stacja_konc:
            break

    # Druga wartość to lista stacji (stringów)
    lista_stacji = [stacja_pocz] + [odcinek[1] for odcinek in sciezka]
    return sciezka, lista_stacji

def znajdz_pomiedzy(stacja_pocz, stacja_konc, lista_sasiedztwa_enum, odwiedzone=[]):
    """
    W wersji minimalnej można zwrócić pustą listę lub krótką 'sub-ścieżkę'.
    Tutaj prosta implementacja – losowo budujemy sub-ścieżkę.
    """
    sciezka = []
    aktualna = stacja_pocz
    visited = set(odwiedzone)
    visited.add(stacja_pocz)

    for _ in range(5):  # ograniczmy do 5 kroków
        sasiedzi = [s for s in lista_sasiedztwa_enum[aktualna] if s[1] not in visited]
        if not sasiedzi:
            break
        wybor = random.choice(sasiedzi)
        sciezka.append(wybor)
        visited.add(wybor[1])
        aktualna = wybor[1]
        if aktualna == stacja_konc:
            break

    return sciezka

def generuj_sasiedztwo(rozwiazanie, lista_sasiedztwa_enum):
    if len(rozwiazanie) < 2:
        return rozwiazanie

    # Wylosuj dwa indeksy (jak w oryginalnym kodzie)
    idx1, idx2 = sorted([
        random.randint(0, len(rozwiazanie) - 1),
        random.randint(0, len(rozwiazanie) - 1),
    ])

    lista1 = rozwiazanie[: idx1 + 1]
    lista2 = rozwiazanie[idx2:]

    odwiedzone = [stacja[0] for stacja in lista1] + [stacja[1] for stacja in lista2]

    stacja_start = rozwiazanie[idx1][0]  # nazwa stacji początkowej
    stacja_end   = rozwiazanie[idx2][1]  # nazwa stacji końcowej

    nowa_sciezka = znajdz_pomiedzy(stacja_start, stacja_end, lista_sasiedztwa_enum, odwiedzone)

    if not nowa_sciezka:
        return rozwiazanie

    # Sklejamy nową listę
    nowe_rozwiazanie = lista1[:-1] + nowa_sciezka + lista2[1:]
    return nowe_rozwiazanie

def tabu_search(stacja_pocz, stacja_konc, lista_sasiedztwa_enum, max_iter=50, dlugosc_tabu=10):
    # Szukamy rozwiązania startowego
    rozwiazanie_startowe, _ = znajdz_rozwiazanie_startowe(stacja_pocz, stacja_konc, lista_sasiedztwa_enum)
    start = rozwiazanie_startowe[:]
    najlepsze_rozwiazanie = rozwiazanie_startowe[:]
    aktualne_rozwiazanie = rozwiazanie_startowe[:]

    lista_tabu = deque(maxlen=dlugosc_tabu)
    iteracje_bez_poprawy = 0
    aspiracja_iter = 10

    historia_funkcji_celu = []

    for _ in range(max_iter):
        sasiedztwo = generuj_sasiedztwo(aktualne_rozwiazanie, lista_sasiedztwa_enum)
        
        if sasiedztwo in lista_tabu:
            iteracje_bez_poprawy += 1
            if iteracje_bez_poprawy > aspiracja_iter:
                # Kryterium aspiracji: weź najlepsze z tabu
                sasiedztwo = min(lista_tabu, key=funkcja_celu)
                iteracje_bez_poprawy = 0
        else:
            iteracje_bez_poprawy = 0

        if funkcja_celu(sasiedztwo) < funkcja_celu(najlepsze_rozwiazanie):
            najlepsze_rozwiazanie = sasiedztwo

        lista_tabu.append(sasiedztwo)
        aktualne_rozwiazanie = sasiedztwo
        
        historia_funkcji_celu.append(funkcja_celu(najlepsze_rozwiazanie))

    # Wizualizacja
    plt.figure(figsize=(10, 6))
    plt.plot(range(max_iter), historia_funkcji_celu, marker='o', color='b')
    plt.title("Wartość funkcji celu najlepszego rozwiązania w każdej iteracji (Tabu Search)")
    plt.xlabel("Iteracja")
    plt.ylabel("Funkcja celu")
    plt.grid(True)
    plt.show()

    print("Rozwiązanie startowe =", start, ", koszt =", funkcja_celu(start))
    print("Najlepsze rozwiązanie =", najlepsze_rozwiazanie, ", koszt =", funkcja_celu(najlepsze_rozwiazanie))

    return najlepsze_rozwiazanie


# -----------------------------
# 5. Główna część programu (przykład uruchomienia)
# -----------------------------
if __name__ == "__main__":
    # Wywołanie Tabu Search
    # Przykład: stacja_pocz = "Oświęcim", stacja_konc = "Kraków Główny"

    stacja_pocz = "Oświęcim"
    stacja_konc = "Kraków Główny"

    najlepsza_trasa = tabu_search(stacja_pocz, stacja_konc, lista_sasiedztwa_enum, max_iter=50, dlugosc_tabu=10)

    print("\nNajlepsza znaleziona trasa (lista krawędzi):")
    for odcinek in najlepsza_trasa:
        print(" ", odcinek)

    print("\nKoszt najlepszej trasy:", funkcja_celu(najlepsza_trasa))
