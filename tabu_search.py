import random
import przejazdy
from collections import deque


# Funkcja celu: minimalizacja czasu podróży i liczby przesiadek
def funkcja_celu(trasa):
    czas_podrozy = sum(odcinek[2] for odcinek in trasa)  # czas_przejazdu
    liczba_przesiadek = sum(
        1 for i in range(1, len(trasa)) if trasa[i][3] != trasa[i - 1][3]
    )  # zmiana numeru pociągu
    return czas_podrozy + liczba_przesiadek * 10  # Przesiadki mają większą wagę


def rozbuduj_liste(lista, lista_sasiedztwa, kierunek):
    """
    Rozbudowuje listę w określonym kierunku:
    - kierunek = "do_przodu": dodaje sąsiadów od końca listy.
    - kierunek = "do_tylu": dodaje stacje, z których można dojechać do końca listy.
    """
    odwiedzone = set(stacja[0] for stacja in lista)  # Unikamy zapętlenia
    while True:
        ostatnia_stacja = lista[-1][0]
        mozliwi_sasiedzi = []

        if kierunek == "do_przodu":
            # Dodajemy stacje, do których można dojechać z ostatniej stacji
            mozliwi_sasiedzi = [
                sasiad
                for sasiad in lista_sasiedztwa[ostatnia_stacja]
                if sasiad[0] not in odwiedzone
            ]
        elif kierunek == "do_tylu":
            # Dodajemy stacje, z których można dojechać do ostatniej stacji
            for stacja, polaczenia in lista_sasiedztwa.items():
                for polaczenie in polaczenia:
                    if polaczenie[0] == ostatnia_stacja and stacja not in odwiedzone:
                        mozliwi_sasiedzi.append(
                            [stacja, polaczenie[1], polaczenie[2], polaczenie[3]]
                        )

        if not mozliwi_sasiedzi:
            break  # Brak dalszych możliwych sąsiadów - kończymy rozbudowę

        # Wybieramy losowego sąsiada
        nowy_sasiad = random.choice(mozliwi_sasiedzi)
        if nowy_sasiad[0] in odwiedzone:
            # Zapętlenie - usuwamy zapętloną część
            lista = [stacja for stacja in lista if stacja[0] != nowy_sasiad[0]]
            break

        lista.append(nowy_sasiad)
        odwiedzone.add(nowy_sasiad[0])

    return lista


# Szukanie rozwiązania startowego
def znajdz_rozwiazanie_startowe(stacja_pocz, stacja_konc, lista_sasiedztwa):
    """
    Znajduje rozwiązanie startowe poprzez równoczesne rozwijanie dwóch list:
    - `lista1` zaczynając od stacji początkowej, dodając sąsiadów.
    - `lista2` zaczynając od stacji końcowej, dodając stacje, z których można do niej dojechać.
    """
    lista1 = [
        [stacja_pocz, None, 0, None]
    ]  # [stacja, godzina odjazdu, czas przejazdu, numer pociągu]
    lista2 = [[stacja_konc, None, 0, None]]
    odwiedzone1 = set([stacja_pocz])
    odwiedzone2 = set([stacja_konc])

    while True:
        # Rozbudowa lista1 w kierunku "do przodu"
        ostatnia_stacja1 = lista1[-1][0]
        mozliwi_sasiedzi1 = [
            sasiad
            for sasiad in lista_sasiedztwa[ostatnia_stacja1]
            if sasiad[0] not in odwiedzone1
        ]
        if mozliwi_sasiedzi1:
            nowy_sasiad1 = random.choice(mozliwi_sasiedzi1)
            lista1.append(nowy_sasiad1)
            odwiedzone1.add(nowy_sasiad1[0])
        else:
            # Ślepa uliczka - odrzucamy ostatni element
            lista1.pop()

        # Rozbudowa lista2 w kierunku "do tyłu"
        ostatnia_stacja2 = lista2[-1][0]
        mozliwi_sasiedzi2 = []
        for stacja, polaczenia in lista_sasiedztwa.items():
            for polaczenie in polaczenia:
                if polaczenie[0] == ostatnia_stacja2 and stacja not in odwiedzone2:
                    mozliwi_sasiedzi2.append(
                        [stacja, polaczenie[1], polaczenie[2], polaczenie[3]]
                    )

        if mozliwi_sasiedzi2:
            nowy_sasiad2 = random.choice(mozliwi_sasiedzi2)
            lista2.append(nowy_sasiad2)
            odwiedzone2.add(nowy_sasiad2[0])
        else:
            # Ślepa uliczka - odrzucamy ostatni element
            lista2.pop()

        # Sprawdzenie przecięcia list
        stacje1 = set(stacja[0] for stacja in lista1)
        stacje2 = set(stacja[0] for stacja in lista2)
        przeciecie = stacje1 & stacje2
        if przeciecie:
            break

        # Sprawdzenie zapętlenia
        if not mozliwi_sasiedzi1 and not mozliwi_sasiedzi2:
            print("Zapętlenie!")
            break

    # Usunięcie ślepych końców i połączenie list
    przeciecie_stacja = przeciecie.pop()
    idx1 = next(i for i, stacja in enumerate(lista1) if stacja[0] == przeciecie_stacja)
    idx2 = next(i for i, stacja in enumerate(lista2) if stacja[0] == przeciecie_stacja)
    lista1 = lista1[:idx1]
    lista2 = lista2[: idx2 + 1]

    rozwiązanie = lista1 + lista2[::-1]
    return rozwiązanie


# Generowanie sąsiedztwa
def generuj_sasiedztwo(rozwiazanie, lista_sasiedztwa):
    # Sprawdź, czy rozwiązanie ma wystarczającą długość
    if len(rozwiazanie) < 4:
        return rozwiazanie  # Zwróć oryginalne rozwiązanie, bo nie można wygenerować sąsiedztwa

    # Losowanie dwóch indeksów z środka listy rozwiązania
    idx1, idx2 = sorted(random.sample(range(1, len(rozwiazanie) - 1), 2))

    # Podział listy na dwie części
    lista1 = rozwiazanie[: idx1 + 1]
    lista2 = rozwiazanie[idx2:]

    # Rozbudowanie list w odpowiednich kierunkach
    lista1 = rozbuduj_liste(lista1, lista_sasiedztwa, "do_przodu")
    lista2 = rozbuduj_liste(lista2, lista_sasiedztwa, "do_tylu")

    # Usunięcie ślepych końców i połączenie list
    rozwiazanie_sasiednie = lista1 + lista2[1:]
    return rozwiazanie_sasiednie


# Algorytm Tabu Search
def tabu_search(
    stacja_pocz, stacja_konc, lista_sasiedztwa, max_iter=100, dlugosc_tabu=10
):
    rozwiazanie_startowe = znajdz_rozwiazanie_startowe(
        stacja_pocz, stacja_konc, lista_sasiedztwa
    )
    najlepsze_rozwiazanie = rozwiazanie_startowe
    print(najlepsze_rozwiazanie)
    aktualne_rozwiazanie = rozwiazanie_startowe
    lista_tabu = deque(maxlen=dlugosc_tabu)
    iteracje_bez_poprawy = 0
    aspiracja_iter = 10  # Kryterium aspiracji

    for iteracja in range(max_iter):
        sasiedztwo = generuj_sasiedztwo(aktualne_rozwiazanie, lista_sasiedztwa)

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

    return najlepsze_rozwiazanie, funkcja_celu(najlepsze_rozwiazanie)


lista_sasiedztwa = {
    "A": [["B", "08:00", 30, 101], ["C", "08:15", 40, 102], ["H", "08:45", 50, 117]],
    "B": [["A", "09:00", 30, 103], ["D", "09:30", 50, 104], ["E", "09:50", 40, 118]],
    "C": [["A", "09:15", 40, 105], ["D", "09:45", 35, 106], ["F", "10:00", 45, 119]],
    "D": [["B", "10:00", 50, 107], ["E", "10:20", 30, 108], ["G", "10:40", 60, 120]],
    "E": [["D", "11:00", 30, 109], ["F", "11:30", 40, 110], ["H", "11:50", 50, 121]],
    "F": [["E", "12:00", 40, 111], ["G", "12:20", 50, 112], ["A", "12:40", 60, 122]],
    "G": [["F", "13:00", 50, 113], ["H", "13:30", 60, 114], ["C", "13:50", 55, 123]],
    "H": [["G", "14:00", 60, 115], ["A", "14:30", 70, 116], ["B", "14:50", 65, 124]],
}


# Wywołanie algorytmu
stacja_pocz = "A"
stacja_konc = "G"
najlepsza_trasa, koszt = tabu_search(stacja_pocz, stacja_konc, lista_sasiedztwa)
print("Najlepsza trasa:")
for odcinek in najlepsza_trasa:
    print(odcinek)
print("Koszt:", koszt)
