# *******************************************************
# klasa: Notatka
# opis: Działaniem klasy ma być zapisywanie oraz wyświetlanie informacji w opdowiedni sposób, znajduje się w niej konstruktor oraz dwie funkcje
# pola: liczaNotatek - przechowuje liczby rzeczywiste które w tej funkcji przedstawiają liczbe notatek,
#   id - przechowuje wartość od liczbyNotatek, liczby rzeczywiste, slyzy jako indentyfikator
#   tytul - przechowuje ciąg znakow ktory przedstawia tytył notatki
#   tresz - przechowuje ciag znakow krory przedstawia tresc notatki 
# *******************************************************


class Notatka:
    liczbaNotatek = 0

    def __init__(self, tytul, tresc):
        Notatka.liczbaNotatek += 1
        self.id = Notatka.liczbaNotatek
        self.tytul = tytul
        self.tresc = tresc

    def display(self):
        print("Tytul:", self.tytul)
        print("Tresc", self.tresc)

    def print_diagnostic(self):
        print("ID:", self.id, "; Tytul:", self.tytul, "; Tresc:", self.tresc)


# Test tej aplikacji
def main():
    note1 = Notatka("Lista Zakupow", "\n1. Jaja\n2. Mleko\n3. Chleb")
    note2 = Notatka("Spotkanie", "\n1. isc na spotknie\n2. gadac z ludzmi\n3. wrocic z spotkania")

    print("Note 1:")
    note1.display()
    note1.print_diagnostic()

    print("\nNote 2:")
    note2.display()
    note2.print_diagnostic()


if __name__ == "__main__":
    main()