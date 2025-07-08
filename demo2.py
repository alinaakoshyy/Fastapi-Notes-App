# NOTES APP
FILENAME = "notes.txt"
# This is a simple notes app that allows users to add, view, and delete notes.
# It stores notes in a list and provides a command-line interface for interaction.

notes = []


def add_note(note):
    notes.append(note)
    with open(FILENAME, "a") as f:     #a- append mode to add new notes without overwriting existing ones
        f.write(note + "\n")
    print(f"Note added: '{note}'")


def list_notes():
    if not notes:
        print("No notes yet.")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")


def delete_note(index):
    if 1 <= index <= len(notes):
        removed = notes.pop(index - 1)
        with open(FILENAME, "w") as f:    #w- write mode to overwrite the file with the updated notes list
            for note in notes:
                f.write(note + "\n")
        print(f"Deleted note: '{removed}'")
    else:
        print("Invalid note number.")
# This function loads notes from the file into the notes list.
# If the file does not exist, it simply passes without error.


def load_notes():
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                notes.append(line.strip())
    except FileNotFoundError:
        pass  # if file doesn't exist yet





def main():
    while True:
        print("\n--- NOTE APP ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            note = input("Enter your note: ")
            add_note(note)
        elif choice == '2':
            list_notes()
        elif choice == '3':
            try:
                index = int(input("Enter note number to delete: "))
                delete_note(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    load_notes()
    main()
