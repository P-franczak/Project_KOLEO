import random
import matplotlib.pyplot as plt
from collections import defaultdict, deque
from enum import Enum
import baza_danych


def stworz_format_tabu(lista_sasiedztwa_enum):
    """
    Zamienia oryginalny słownik (Stacja -> [[StacjaDocelowa, nr_pociagu, godz_odjazdu], ...])
    na słownik { "NazwaStacji": [ [start, end, czas_przejazdu, nr_pociagu], ... ] }
    gdzie 'start' i 'end' to stringi z nazwą stacji, a czas_przejazdu to np. stała = 5.
    """
    new_lista = defaultdict(list)

    for stacja_z, edges in lista_sasiedztwa_enum.items():
        stacja_z_str = baza_danych.mapa_stacji[stacja_z]
        for stacja_do_enum, nr_pociagu, godz_odjazdu in edges:
            stacja_do_str = baza_danych.mapa_stacji[stacja_do_enum]
            # Na potrzeby algorytmu przyjmujemy np. stały czas = 5
            czas_przejazdu = 5

            new_lista[stacja_z_str].append(
                [
                    stacja_z_str,  # stacja początkowa (string)
                    stacja_do_str,  # stacja docelowa (string)
                    czas_przejazdu,  # na razie stały
                    nr_pociagu,
                ]
            )

    # Konwertuj defaultdict na zwykły dict
    return dict(new_lista)


# Funkcja celu: minimalizacja czasu podróży i liczby przesiadek
def funkcja_celu(trasa):
    czas_podrozy = sum(odcinek[2] for odcinek in trasa)  # czas jazdy
    liczba_przesiadek = sum(
        1 for i in range(1, len(trasa)) if trasa[i][3] != trasa[i - 1][3]
    )  # zmiana numeru pociągu
    return czas_podrozy + liczba_przesiadek * 10  # Przesiadki mają większą wagę


# Szukanie rozwiązania startowego
def znajdz_rozwiazanie_startowe(stacja_pocz, stacja_konc, lista_sasiedztwa):
    lista1 = []  # [stacja z, stacja do, godzina odjazdu, czas jazdy, nr pociągu]
    lista2 = []
    odwiedzone1 = set([stacja_pocz])
    odwiedzone2 = set([stacja_konc])
    ostatnia_stacja1 = stacja_pocz  # Ostatnia stacja w rozbudowywanej liście
    ostatnia_stacja2 = stacja_konc  # Ostatnia stacja w rozbudowywanej liście

    while True:
        # Rozbudowa lista1 w kierunku "do przodu"
        mozliwi_sasiedzi1 = [
            sasiad
            for sasiad in lista_sasiedztwa[ostatnia_stacja1]
            if sasiad[1] not in odwiedzone1
        ]
        if mozliwi_sasiedzi1:
            nowy_sasiad1 = random.choice(mozliwi_sasiedzi1)
            lista1.append(nowy_sasiad1)
            odwiedzone1.add(nowy_sasiad1[1])
            ostatnia_stacja1 = nowy_sasiad1[1]
            # Jeśli lista1 dotarła do stacji końcowej, zwróć ją
            if ostatnia_stacja1 == stacja_konc:
                lista_stacji = [stacja[0] for stacja in lista1] + [stacja_konc]
                return lista1, lista_stacji
        elif lista1:
            lista1.pop()

        # Rozbudowa lista2 w kierunku "do tyłu"
        mozliwi_sasiedzi2 = []
        for stacja, polaczenia in lista_sasiedztwa.items():
            for polaczenie in polaczenia:
                if polaczenie[1] == ostatnia_stacja2 and stacja not in odwiedzone2:
                    mozliwi_sasiedzi2.append(
                        [
                            stacja,
                            polaczenie[1],
                            polaczenie[2],
                            polaczenie[3],
                        ]
                    )

        if mozliwi_sasiedzi2:
            nowy_sasiad2 = random.choice(mozliwi_sasiedzi2)
            lista2.append(nowy_sasiad2)
            odwiedzone2.add(nowy_sasiad2[1])
            ostatnia_stacja2 = nowy_sasiad2[0]
            # Jeśli lista2 dotarła do stacji początkowej, zwróć ją
            if ostatnia_stacja2 == stacja_pocz:
                lista_stacji = [stacja[0] for stacja in lista2[::-1]] + [stacja_konc]
                return lista2[::-1], lista_stacji
        elif lista2:
            lista2.pop()

        # Sprawdzenie przecięcia list
        stacje1 = set(stacja[1] for stacja in lista1)
        stacje2 = set(stacja[0] for stacja in lista2)
        przeciecie = stacje1 & stacje2
        if przeciecie:
            break

        if not mozliwi_sasiedzi1 and not mozliwi_sasiedzi2:
            return (0, 0)

    przeciecie_stacja = przeciecie.pop()
    idx1 = next(i for i, stacja in enumerate(lista1) if stacja[1] == przeciecie_stacja)
    idx2 = next(i for i, stacja in enumerate(lista2) if stacja[0] == przeciecie_stacja)

    lista1 = lista1[: idx1 + 1]
    lista2 = lista2[: idx2 + 1]

    # Tworzenie listy stacji
    lista_stacji = (
        [stacja[0] for stacja in lista1]
        + [stacja[0] for stacja in lista2[::-1]]
        + [stacja_konc]
    )

    return lista1 + lista2[::-1], lista_stacji


def znajdz_pomiedzy(stacja_pocz, stacja_konc, lista_sasiedztwa, odwiedzone=[]):
    lista1 = []  # [stacja z, stacja do, godzina odjazdu, czas jazdy, nr pociągu]
    lista2 = []
    odwiedzone1 = set(odwiedzone)
    odwiedzone2 = set(odwiedzone)
    odwiedzone1.add(stacja_pocz)
    odwiedzone2.add(stacja_konc)
    ostatnia_stacja1 = stacja_pocz
    ostatnia_stacja2 = stacja_konc

    while True:
        # Rozbudowa lista1 w kierunku "do przodu"
        mozliwi_sasiedzi1 = [
            sasiad
            for sasiad in lista_sasiedztwa[ostatnia_stacja1]
            if sasiad[1] not in odwiedzone1
        ]
        if mozliwi_sasiedzi1:
            nowy_sasiad1 = random.choice(mozliwi_sasiedzi1)
            lista1.append(nowy_sasiad1)
            odwiedzone1.add(nowy_sasiad1[1])
            ostatnia_stacja1 = nowy_sasiad1[1]
            # Jeśli lista1 dotarła do stacji końcowej, zwróć ją
            if ostatnia_stacja1 == stacja_konc:
                return lista1
        elif lista1:
            lista1.pop()

        # Rozbudowa lista2 w kierunku "do tyłu"
        mozliwi_sasiedzi2 = []
        for stacja, polaczenia in lista_sasiedztwa.items():
            for polaczenie in polaczenia:
                if polaczenie[1] == ostatnia_stacja2 and stacja not in odwiedzone2:
                    mozliwi_sasiedzi2.append(
                        [
                            stacja,
                            polaczenie[1],
                            polaczenie[2],
                            polaczenie[3],
                        ]
                    )

        if mozliwi_sasiedzi2:
            nowy_sasiad2 = random.choice(mozliwi_sasiedzi2)
            lista2.append(nowy_sasiad2)
            odwiedzone2.add(nowy_sasiad2[0])
            ostatnia_stacja2 = nowy_sasiad2[0]
            if ostatnia_stacja2 == stacja_pocz:
                return lista2[::-1]
        elif lista2:
            lista2.pop()

        # Sprawdzenie przecięcia list
        stacje1 = set(stacja[1] for stacja in lista1)
        stacje2 = set(stacja[0] for stacja in lista2)
        przeciecie = stacje1 & stacje2
        if przeciecie:
            break

        if not mozliwi_sasiedzi1 and not mozliwi_sasiedzi2:
            return []

    przeciecie_stacja = przeciecie.pop() if przeciecie else None
    if przeciecie_stacja:
        idx1 = next(
            i for i, stacja in enumerate(lista1) if stacja[1] == przeciecie_stacja
        )
        idx2 = next(
            i for i, stacja in enumerate(lista2) if stacja[0] == przeciecie_stacja
        )
        lista1 = lista1[: idx1 + 1]
        lista2 = lista2[: idx2 + 1]

    return lista1 + lista2[::-1]


# Generowanie sąsiedztwa
def generuj_sasiedztwo(rozwiazanie, lista_sasiedztwa):
    if len(rozwiazanie) < 2:
        return rozwiazanie

    idx1, idx2 = sorted(
        [
            random.randint(0, len(rozwiazanie) - 1),
            random.randint(0, len(rozwiazanie) - 1),
        ]
    )

    lista1 = rozwiazanie[: idx1 + 1]
    lista2 = rozwiazanie[idx2:]

    odwiedzone = [stacja[0] for stacja in lista1] + [stacja[1] for stacja in lista2]

    stacja_start = rozwiazanie[idx1][0]
    stacja_end = rozwiazanie[idx2][1]
    # print(stacja_start, stacja_end)

    nowa_sciezka = znajdz_pomiedzy(
        stacja_start, stacja_end, lista_sasiedztwa, odwiedzone
    )

    if not nowa_sciezka:
        return rozwiazanie

    nowe_rozwiazanie = lista1[:-1] + nowa_sciezka + lista2[1:]

    return nowe_rozwiazanie


# Algorytm Tabu Search
def tabu_search(
    stacja_pocz,
    stacja_konc,
    lista_sasiedztwa,
    max_iter=100,
    dlugosc_tabu=10,
    aspiracja_iter=10,
):
    rozwiazanie_startowe, lista_stacji = znajdz_rozwiazanie_startowe(
        stacja_pocz, stacja_konc, lista_sasiedztwa
    )
    if not rozwiazanie_startowe and not lista_stacji:
        return 0
    start = rozwiazanie_startowe
    najlepsze_rozwiazanie = rozwiazanie_startowe
    aktualne_rozwiazanie = rozwiazanie_startowe
    lista_tabu = deque(maxlen=dlugosc_tabu)
    iteracje_bez_poprawy = 0

    # Lista do przechowywania wartości funkcji celu najlepszego rozwiązania
    historia_funkcji_celu = []

    for _ in range(max_iter):
        sasiedztwo = generuj_sasiedztwo(aktualne_rozwiazanie, lista_sasiedztwa)
        # print(sasiedztwo, funkcja_celu(sasiedztwo), '\n', '=======')

        if sasiedztwo in lista_tabu:
            iteracje_bez_poprawy += 1
            if iteracje_bez_poprawy > aspiracja_iter:
                # Kryterium aspiracji
                sasiedztwo = min(lista_tabu, key=funkcja_celu)
                iteracje_bez_poprawy = 0
        else:
            iteracje_bez_poprawy = 0

        if funkcja_celu(sasiedztwo) < funkcja_celu(najlepsze_rozwiazanie):
            najlepsze_rozwiazanie = sasiedztwo

        lista_tabu.append(sasiedztwo)
        aktualne_rozwiazanie = sasiedztwo

        # Zapisz wartość funkcji celu najlepszego rozwiązania w tej iteracji
        historia_funkcji_celu.append(funkcja_celu(najlepsze_rozwiazanie))

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(
        range(max_iter), historia_funkcji_celu, marker="o", linestyle="-", color="b"
    )
    plt.title("Wartość funkcji celu najlepszego rozwiązania w każdej iteracji")
    plt.xlabel("Numer iteracji")
    plt.ylabel("Wartość funkcji celu")
    plt.grid(True)

    # Zapis wykresu do pliku
    plt.savefig("wykres.jpg", format="jpg")
    plt.close()  # Zamknięcie figury, aby zwolnić zasoby

    return najlepsze_rozwiazanie, funkcja_celu(najlepsze_rozwiazanie)


lista_sasiedztwa_enum = stworz_format_tabu(baza_danych.lista_sasiedztwa_enum)
