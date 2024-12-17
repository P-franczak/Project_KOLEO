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


# Szukanie rozwiązania startowego
def znajdz_rozwiazanie_startowe(stacja_pocz, stacja_konc, lista_sasiedztwa):
    lista1 = [
        [stacja_pocz, None, 0, None]
    ]  # [stacja, godzina_odjazdu, czas_przejazdu, numer_pociągu]
    lista2 = [[stacja_konc, None, 0, None]]
    odwiedzone1, odwiedzone2 = set(), set()

    while (
        set(stacja[0] for stacja in lista1) & set(stacja[0] for stacja in lista2)
        == set()
    ):
        # Rozwijanie listy 1
        if lista1:  # Sprawdzamy, czy lista1 nie jest pusta
            ostatnia_stacja1 = lista1[-1][0]
            sasiedzi1 = [
                p
                for p in lista_sasiedztwa.get(ostatnia_stacja1, [])
                if p[0] not in odwiedzone1
            ]
            if not sasiedzi1:
                lista1.pop()
            else:
                nastepny1 = random.choice(sasiedzi1)
                lista1.append(nastepny1)
                odwiedzone1.add(nastepny1[0])

        # Rozwijanie listy 2
        if lista2:  # Sprawdzamy, czy lista2 nie jest pusta
            ostatnia_stacja2 = lista2[-1][0]
            sasiedzi2 = [
                p
                for p in lista_sasiedztwa.get(ostatnia_stacja2, [])
                if p[0] not in odwiedzone2
            ]
            if not sasiedzi2:
                lista2.pop()
            else:
                nastepny2 = random.choice(sasiedzi2)
                lista2.append(nastepny2)
                odwiedzone2.add(nastepny2[0])

        # Jeśli obie listy się opróżnią, przerwij pętlę
        if not lista1 or not lista2:
            raise ValueError(
                "Nie można znaleźć rozwiązania startowego: brak połączeń między stacjami."
            )

    # Połączenie list
    przeciecie = set(stacja[0] for stacja in lista1) & set(
        stacja[0] for stacja in lista2
    )
    punkt_przeciecia = list(przeciecie)[0]

    # Tworzenie pełnej trasy
    indeks1 = next(i for i, s in enumerate(lista1) if s[0] == punkt_przeciecia)
    indeks2 = next(i for i, s in enumerate(lista2) if s[0] == punkt_przeciecia)

    rozwiazanie = lista1[: indeks1 + 1] + lista2[:indeks2][::-1]
    return rozwiazanie


# Generowanie sąsiedztwa
def generuj_sasiedztwo(rozwiazanie, lista_sasiedztwa):
    if len(rozwiazanie) < 4:
        return rozwiazanie

    idx1, idx2 = sorted(random.sample(range(1, len(rozwiazanie) - 1), 2))
    lista1 = rozwiazanie[: idx1 + 1]
    lista2 = rozwiazanie[idx2:]

    # Odbudowa list
    while lista1[-1][0] != lista2[-1][0]:
        ostatnia_stacja1 = lista1[-1][0]
        sasiedzi1 = lista_sasiedztwa[ostatnia_stacja1]
        if not sasiedzi1:
            break
        lista1.append(random.choice(sasiedzi1))

    rozwiazanie_sasiedztwa = lista1 + lista2
    return rozwiazanie_sasiedztwa


# Algorytm Tabu Search
def tabu_search(
    stacja_pocz, stacja_konc, lista_sasiedztwa, max_iter=100, dlugosc_tabu=10
):
    rozwiazanie_startowe = znajdz_rozwiazanie_startowe(
        stacja_pocz, stacja_konc, lista_sasiedztwa
    )
    najlepsze_rozwiazanie = rozwiazanie_startowe
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

    return najlepsze_rozwiazanie


# Przykładowa baza danych jako słownik list
lista_sasiedztwa = {
    "A": [["B", "08:00", 2, "P1"], ["C", "09:00", 3, "P2"]],
    "B": [["C", "08:30", 1, "P3"], ["A", "10:00", 2, "P1"]],
    "C": [["D", "09:30", 2, "P4"], ["A", "12:00", 3, "P2"], ["B", "09:30", 1, "P3"]],
    "D": [["C", "11:30", 2, "P4"]],
}

# Wywołanie algorytmu
stacja_pocz = "A"
stacja_konc = "D"
najlepsza_trasa = tabu_search(stacja_pocz, stacja_konc, lista_sasiedztwa)
print("Najlepsza trasa:")
for odcinek in najlepsza_trasa:
    print(odcinek)
