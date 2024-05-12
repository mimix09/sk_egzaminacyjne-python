class Notatka:
    liczbaNotatek = 0

    def __init__(self, title, content):
        Notatka.liczbaNotatek += 1
        self.id = Notatka.liczbaNotatek
        self.title = title
        self.content = content

    def display(self):
        print("Tytul:", self.title)
        print("Tresc", self.content)

    def print_diagnostic(self):
        print("ID:", self.id, "; Title:", self.title, "; Content:", self.content)


# Test tej aplikacji
def main():
    note1 = Notatka("Shopping List", "1. Eggs\n2. Milk\n3. Bread")
    note2 = Notatka("Meeting Agenda", "1. Discuss project timeline\n2. Assign tasks\n3. Set next meeting date")

    print("Note 1:")
    note1.display()
    note1.print_diagnostic()

    print("\nNote 2:")
    note2.display()
    note2.print_diagnostic()


if __name__ == "__main__":
    main()
