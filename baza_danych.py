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
lista_sasiedztwa_enum = {st: [] for st in Stacja}

# Pociąg 1
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30750/1", "03:38"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "30750/1", "03:43"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30750/1", "03:46"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30750/1", "03:51"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30750/1", "03:56"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30750/1", "03:59"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30750/1", "04:02"])
lista_sasiedztwa_enum[Stacja.Dulowa].append(
    [Stacja.Wola_Filipowska, "30750/1", "04:07"]
)
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30750/1", "04:11"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30750/1", "04:14"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30750/1", "04:19"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "30750/1", "04:24"]
)
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
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "30753", "04:39"]
)
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
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "30753", "04:53"]
)

# Pociąg 3
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30754/5", "04:19"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "30754/5", "04:24"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30754/5", "04:27"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30754/5", "04:32"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30754/5", "04:37"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30754/5", "04:39"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30754/5", "04:43"])
lista_sasiedztwa_enum[Stacja.Dulowa].append(
    [Stacja.Wola_Filipowska, "30754/5", "04:48"]
)
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30754/5", "04:51"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30754/5", "04:55"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30754/5", "05:00"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "30754/5", "05:05"]
)
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
lista_sasiedztwa_enum[Stacja.Katowice].append(
    [Stacja.Katowice_Zawodzie, "43300/1", "04:31"]
)
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
lista_sasiedztwa_enum[Stacja.Jaworzno_Ciężkowice].append(
    [Stacja.Balin, "43300/1", "05:06"]
)
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "43300/1", "05:10"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "43300/1", "05:15"])
lista_sasiedztwa_enum[Stacja.Dulowa].append(
    [Stacja.Wola_Filipowska, "43300/1", "05:19"]
)
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "43300/1", "05:22"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "43300/1", "05:26"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "43300/1", "05:31"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "43300/1", "05:35"]
)
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
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "30756/7", "05:06"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30756/7", "05:09"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30756/7", "05:15"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30756/7", "05:20"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30756/7", "05:22"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30756/7", "05:27"])
lista_sasiedztwa_enum[Stacja.Dulowa].append(
    [Stacja.Wola_Filipowska, "30756/7", "05:32"]
)
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30756/7", "05:36"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30756/7", "05:40"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30756/7", "05:46"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "30756/7", "05:51"]
)
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
lista_sasiedztwa_enum[Stacja.Bukowno].append(
    [Stacja.Jaworzno_Szczakowa, "33139", "05:03"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Trzebinia, "33139", "05:19"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "33139", "05:33"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "33139", "05:42"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Kraków_Bronowice, "33139", "05:55"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "33139", "06:02"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "33139", "06:09"]
)

# Pociąg 7
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "30758/9", "06:19"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "30758/9", "06:24"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "30758/9", "06:27"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "30758/9", "06:32"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "30758/9", "06:37"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "30758/9", "06:39"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "30758/9", "06:43"])
lista_sasiedztwa_enum[Stacja.Dulowa].append(
    [Stacja.Wola_Filipowska, "30758/9", "06:48"]
)
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "30758/9", "06:51"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "30758/9", "06:55"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "30758/9", "07:00"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "30758/9", "07:06"]
)
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
lista_sasiedztwa_enum[Stacja.Katowice].append(
    [Stacja.Katowice_Zawodzie, "43800/1", "06:04"]
)
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
lista_sasiedztwa_enum[Stacja.Mysłowice].append(
    [Stacja.Jaworzno_Szczakowa, "43800/1", "06:22"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [
        Stacja.Jaworzno_Ciężkowice,
        "43800/1",
        "06:32",
    ]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Ciężkowice].append(
    [Stacja.Balin, "43800/1", "06:36"]
)
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "43800/1", "06:41"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "43800/1", "06:48"])
lista_sasiedztwa_enum[Stacja.Dulowa].append(
    [Stacja.Wola_Filipowska, "43800/1", "06:52"]
)
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "43800/1", "06:55"]
)

# Pociąg 9
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Bukowno].append(
    [Stacja.Jaworzno_Szczakowa, "33141", "06:04"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Trzebinia, "33141", "06:04"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "33141", "06:04"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Kraków_Bronowice, "33141", "06:04"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "33141", "06:04"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "33141", "06:04"]
)


# Pociąg 10
lista_sasiedztwa_enum[Stacja.Katowice].append(
    [Stacja.Katowice_Zawodzie, "43100/1", "06:23"]
)
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
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Kraków_Bronowice, "43100/1", "07:18"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "43100/1", "07:30"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "43100/1", "07:32"]
)


# Pociąg 11
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "33143", "06:33"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "33143", "06:58"])
lista_sasiedztwa_enum[Stacja.Bukowno].append(
    [Stacja.Jaworzno_Szczakowa, "33143", "07:07"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Trzebinia, "33143", "07:22"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "33143", "07:34"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Zabierzów, "33143", "07:43"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Kraków_Bronowice, "33143", "07:57"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Łobzów, "33143", "08:04"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Główny, "33143", "08:07"]
)


# Pociąg 12
lista_sasiedztwa_enum[Stacja.Czechowice_Dziedzice].append(
    [Stacja.Kaniów, "43528", "06:40"]
)
lista_sasiedztwa_enum[Stacja.Kaniów].append([Stacja.Dankowice, "43528", "06:45"])
lista_sasiedztwa_enum[Stacja.Dankowice].append(
    [Stacja.Jawiszowice_Jaźnik, "43528", "06:49"]
)
lista_sasiedztwa_enum[Stacja.Jawiszowice_Jaźnik].append(
    [Stacja.Brzeszce_Jawiszowice, "43528", "06:52"]
)
lista_sasiedztwa_enum[Stacja.Brzeszce_Jawiszowice].append(
    [Stacja.Brzeszcze, "43528", "06:56"]
)
lista_sasiedztwa_enum[Stacja.Brzeszcze].append([Stacja.Olkusz, "43528", "07:01"])

# Pociąg 13
lista_sasiedztwa_enum[Stacja.Katowice].append(
    [Stacja.Katowice_Zawodzie, "45800", "06:00"]
)
lista_sasiedztwa_enum[Stacja.Katowice_Zawodzie].append(
    [Stacja.Katowice_Szopienice_Południowe, "45800", "06:05"]
)
lista_sasiedztwa_enum[Stacja.Katowice_Szopienice_Południowe].append(
    [Stacja.Mysłowice, "45800", "06:10"]
)
lista_sasiedztwa_enum[Stacja.Mysłowice].append(
    [Stacja.Jaworzno_Szczakowa, "45800", "06:20"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Balin, "45800", "06:30"]
)
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "45800", "06:35"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "45800", "06:40"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "45800", "06:45"])

# Pociąg 14
lista_sasiedztwa_enum[Stacja.Czechowice_Dziedzice].append(
    [Stacja.Kaniów, "45900", "07:30"]
)
lista_sasiedztwa_enum[Stacja.Kaniów].append([Stacja.Dankowice, "45900", "16:35"])
lista_sasiedztwa_enum[Stacja.Dankowice].append(
    [Stacja.Jawiszowice_Jaźnik, "45900", "07:40"]
)
lista_sasiedztwa_enum[Stacja.Jawiszowice_Jaźnik].append(
    [Stacja.Brzeszce_Jawiszowice, "45900", "07:45"]
)
lista_sasiedztwa_enum[Stacja.Brzeszce_Jawiszowice].append(
    [Stacja.Brzeszcze, "45900", "07:50"]
)
lista_sasiedztwa_enum[Stacja.Brzeszcze].append([Stacja.Oświęcim, "45900", "07:55"])
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "45900", "08:00"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "45900", "08:05"]
)

# Pociąg 15
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "46000", "07:15"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "46000", "07:30"])
lista_sasiedztwa_enum[Stacja.Bukowno].append(
    [Stacja.Jaworzno_Szczakowa, "46000", "07:45"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Trzebinia, "46000", "08:00"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "46000", "08:10"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "46000", "08:20"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "46000", "08:30"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "46000", "08:40"])

# Pociąg 16
lista_sasiedztwa_enum[Stacja.Kraków_Główny].append(
    [Stacja.Kraków_Łobzów, "46100", "05:15"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Bronowice, "46100", "05:18"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Mydlniki, "46100", "05:21"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Mydlniki_Wapiennik, "46100", "05:24"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [Stacja.Zabierzów_Rząska, "46100", "05:28"]
)
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [Stacja.Zabierzów, "46100", "05:33"]
)
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Rudawa, "46100", "05:40"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Krzeszowice, "46100", "05:50"])

# Pociąg 17
lista_sasiedztwa_enum[Stacja.Katowice].append(
    [Stacja.Katowice_Zawodzie, "46300", "07:00"]
)
lista_sasiedztwa_enum[Stacja.Katowice_Zawodzie].append(
    [Stacja.Katowice_Szopienice_Południowe, "46300", "07:05"]
)
lista_sasiedztwa_enum[Stacja.Katowice_Szopienice_Południowe].append(
    [Stacja.Mysłowice, "46300", "07:10"]
)
lista_sasiedztwa_enum[Stacja.Mysłowice].append(
    [Stacja.Jaworzno_Szczakowa, "46300", "07:20"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Jaworzno_Ciężkowice, "46300", "07:30"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Ciężkowice].append(
    [Stacja.Balin, "46300", "07:35"]
)
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "46300", "07:40"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "46300", "07:45"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "46300", "07:50"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "46300", "07:55"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "46300", "08:00"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "46300", "08:05"])

# Pociąg 18
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "46400", "04:00"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "46400", "04:05"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "46400", "04:10"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "46400", "04:20"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "46400", "04:25"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "46400", "04:30"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "46400", "04:35"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "46400", "04:40"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "46400", "04:50"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "46400", "04:55"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "46400", "05:00"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Zabierzów_Rząska, "46400", "05:05"]
)
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [Stacja.Kraków_Mydlniki_Wapiennik, "46400", "05:10"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [Stacja.Kraków_Mydlniki, "46400", "05:15"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Bronowice, "46400", "05:20"]
)

# Pociąg 19
lista_sasiedztwa_enum[Stacja.Katowice].append(
    [Stacja.Katowice_Zawodzie, "46500", "08:00"]
)
lista_sasiedztwa_enum[Stacja.Katowice_Zawodzie].append(
    [Stacja.Katowice_Szopienice_Południowe, "46500", "08:05"]
)
lista_sasiedztwa_enum[Stacja.Katowice_Szopienice_Południowe].append(
    [Stacja.Mysłowice, "46500", "08:10"]
)
lista_sasiedztwa_enum[Stacja.Mysłowice].append(
    [Stacja.Jaworzno_Szczakowa, "46500", "08:20"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Balin, "46500", "08:30"]
)
lista_sasiedztwa_enum[Stacja.Balin].append([Stacja.Trzebinia, "46500", "08:35"])
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "46500", "08:50"])
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "46500", "08:00"])

# Pociąg 20
lista_sasiedztwa_enum[Stacja.Wolbrom].append([Stacja.Olkusz, "46600", "08:00"])
lista_sasiedztwa_enum[Stacja.Olkusz].append([Stacja.Bukowno, "46600", "08:20"])
lista_sasiedztwa_enum[Stacja.Bukowno].append(
    [Stacja.Jaworzno_Szczakowa, "46600", "08:35"]
)
lista_sasiedztwa_enum[Stacja.Jaworzno_Szczakowa].append(
    [Stacja.Trzebinia, "46600", "08:50"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Dulowa, "46600", "09:00"])
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Wola_Filipowska, "46600", "09:10"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Krzeszowice, "46600", "09:20"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append([Stacja.Rudawa, "46600", "09:30"])
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Zabierzów, "46600", "09:40"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append(
    [Stacja.Kraków_Bronowice, "46600", "09:55"]
)

# Pociąg 21
lista_sasiedztwa_enum[Stacja.Czechowice_Dziedzice].append(
    [Stacja.Kaniów, "46700", "06:00"]
)
lista_sasiedztwa_enum[Stacja.Kaniów].append([Stacja.Dankowice, "46700", "06:05"])
lista_sasiedztwa_enum[Stacja.Dankowice].append(
    [Stacja.Jawiszowice_Jaźnik, "46700", "06:10"]
)
lista_sasiedztwa_enum[Stacja.Jawiszowice_Jaźnik].append(
    [Stacja.Brzeszce_Jawiszowice, "46700", "06:15"]
)
lista_sasiedztwa_enum[Stacja.Brzeszce_Jawiszowice].append(
    [Stacja.Brzeszcze, "46700", "06:20"]
)
lista_sasiedztwa_enum[Stacja.Brzeszcze].append([Stacja.Oświęcim, "46700", "06:25"])
lista_sasiedztwa_enum[Stacja.Oświęcim].append(
    [Stacja.Gorzów_Chrzanowski, "46700", "06:35"]
)
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Chełmek, "46700", "06:40"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append([Stacja.Libiąż, "46700", "06:45"])
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chrzanów, "46700", "06:50"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append(
    [Stacja.Chrzanów_Śródmieście, "46700", "06:55"]
)
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Trzebinia, "46700", "07:00"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append([Stacja.Krzeszowice, "46700", "07:15"])

# odwrócone

# Pociąg 1
lista_sasiedztwa_enum[Stacja.Gorzów_Chrzanowski].append(
    [Stacja.Oświęcim, "30750/1", "03:38"]
)
lista_sasiedztwa_enum[Stacja.Chełmek].append(
    [Stacja.Gorzów_Chrzanowski, "30750/1", "03:43"]
)
lista_sasiedztwa_enum[Stacja.Libiąż].append([Stacja.Chełmek, "30750/1", "03:46"])
lista_sasiedztwa_enum[Stacja.Chrzanów].append([Stacja.Libiąż, "30750/1", "03:51"])
lista_sasiedztwa_enum[Stacja.Chrzanów_Śródmieście].append(
    [Stacja.Chrzanów, "30750/1", "03:56"]
)
lista_sasiedztwa_enum[Stacja.Trzebinia].append(
    [Stacja.Chrzanów_Śródmieście, "30750/1", "03:59"]
)
lista_sasiedztwa_enum[Stacja.Dulowa].append([Stacja.Trzebinia, "30750/1", "04:02"])
lista_sasiedztwa_enum[Stacja.Wola_Filipowska].append(
    [Stacja.Dulowa, "30750/1", "04:07"]
)
lista_sasiedztwa_enum[Stacja.Krzeszowice].append(
    [Stacja.Wola_Filipowska, "30750/1", "04:11"]
)
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Krzeszowice, "30750/1", "04:14"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Rudawa, "30750/1", "04:19"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [Stacja.Zabierzów, "30750/1", "04:24"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [Stacja.Zabierzów_Rząska, "30750/1", "04:27"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Mydlniki_Wapiennik, "30750/1", "04:30"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Mydlniki, "30750/1", "04:32"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Bronowice, "30750/1", "04:34"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Główny].append(
    [Stacja.Kraków_Łobzów, "30750/1", "04:37"]
)

# Pociąg 2
lista_sasiedztwa_enum[Stacja.Rudawa].append([Stacja.Krzeszowice, "30753", "04:28"])
lista_sasiedztwa_enum[Stacja.Zabierzów].append([Stacja.Rudawa, "30753", "04:34"])
lista_sasiedztwa_enum[Stacja.Zabierzów_Rząska].append(
    [Stacja.Zabierzów, "30753", "04:39"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki_Wapiennik].append(
    [Stacja.Zabierzów_Rząska, "30753", "04:42"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Mydlniki].append(
    [Stacja.Kraków_Mydlniki_Wapiennik, "30753", "04:45"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Bronowice].append(
    [Stacja.Kraków_Mydlniki, "30753", "04:47"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Łobzów].append(
    [Stacja.Kraków_Bronowice, "30753", "04:50"]
)
lista_sasiedztwa_enum[Stacja.Kraków_Główny].append(
    [Stacja.Kraków_Łobzów, "30753", "04:53"]
)
