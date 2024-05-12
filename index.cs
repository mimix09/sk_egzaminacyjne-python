// *******************************************************
// klasa: Notatka
// opis: Działaniem klasy ma być zapisywanie oraz wyświetlanie informacji w opdowiedni sposób, znajduje się w niej konstruktor oraz dwie funkcje
// pola: liczaNotatek - przechowuje liczby rzeczywiste które w tej funkcji przedstawiają liczbe notatek,
//   id - przechowuje wartość od liczbyNotatek, liczby rzeczywiste, slyzy jako indentyfikator
//   tytul - przechowuje ciąg znakow ktory przedstawia tytył notatki
//   tresz - przechowuje ciag znakow krory przedstawia tresc notatki 
// *******************************************************

using System;

class Notatka
{
    private static int liczbaNotatek = 0;
    private int id;
    private string tytul;
    private string tresc;

    public Notatka(string tytul, string tresc)
    {
        Notatka.liczbaNotatek++;
        this.id = Notatka.liczbaNotatek;
        this.tytul = tytul;
        this.tresc = tresc;
    }

    public void Display()
    {
        Console.WriteLine("Tytul: " + this.tytul);
        Console.WriteLine("Tresc: " + this.tresc);
    }

    public void DisplayDiagnostic()
    {
        Console.WriteLine("ID: " + this.id + " ; Tytul: " + this.tytul + " ; Tresc: " + this.tresc);
    }
}

class HelloWorld {
  static void Main() {
    Notatka note1 = new Notatka("Lista Zakupow", "\n1. Jaja\n2. Mleko\n3. Chleb");
        Notatka note2 = new Notatka("Spotkanie", "\n1. isc na spotknie\n2. gadac z ludzmi\n3. wrocic z spotkania");

        Console.WriteLine("Note 1:");
        note1.Display();
        note1.DisplayDiagnostic();

        Console.WriteLine("\nNote 2:");
        note2.Display();
        note2.DisplayDiagnostic();
  }
}
