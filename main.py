class Notatka:
    note_counter = 0

    def __init__(self, title, content):
        Note.note_counter += 1
        self.__id = Note.note_counter
        self.__title = title
        self.__content = content

    def display(self):
        print("Title:", self.__title)
        print("Content:", self.__content)

    def print_diagnostic(self):
        print("ID:", self.__id, "; Title:", self.__title, "; Content:", self.__content)


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
