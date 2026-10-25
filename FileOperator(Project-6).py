
import os
from datetime import datetime


class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"
        self.separator = "\n" + "-" * 50 + "\n"

    def add_entry(self):
        try:
            
            try:
                with open(self.filename, "x", encoding="utf-8"):
                    pass
            except FileExistsError:
                pass

            entry = input("\nEnter your journal entry:\n").strip()

            if not entry:
                print("Entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n")
                file.write(self.separator)

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied. Check file permissions.")
        except OSError as error:
            print("File error:", error)

    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if not content.strip():
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:\n")
                print(content)

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while reading the journal.")
        except OSError as error:
            print("File error:", error)

    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            entries = content.split(self.separator)
            matches = [
                entry.strip()
                for entry in entries
                if keyword.casefold() in entry.casefold()
                and entry.strip()
            ]

            if matches:
                print("\nMatching Entries:\n")
                for entry in matches:
                    print(entry)
                    print()
            else:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error: No journal exists. Add an entry first.")
        except PermissionError:
            print("Error: Permission denied while searching the journal.")
        except OSError as error:
            print("File error:", error)

    def delete_all_entries(self):
        try:
            
            with open(self.filename, "r", encoding="utf-8"):
                pass

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).strip().casefold()

            if confirmation != "yes":
                print("Deletion cancelled.")
                return

            with open(self.filename, "w", encoding="utf-8"):
                pass

            os.remove(self.filename)

            print("All journal entries have been deleted.")

        except FileNotFoundError:
            print("No journal entries to delete.")
        except PermissionError:
            print("Error: Permission denied. Could not delete the journal.")
        except OSError as error:
            print("File error:", error)

    def run(self):
        print("Welcome to Personal Journal Manager!")

        while True:
            print("\nPlease select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            try:
                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    self.add_entry()
                elif choice == "2":
                    self.view_entries()
                elif choice == "3":
                    self.search_entry()
                elif choice == "4":
                    self.delete_all_entries()
                elif choice == "5":
                    print("Thank you for using Personal Journal Manager.")
                    break
                else:
                    print("Invalid option. Please select a valid option.")

            except (EOFError, KeyboardInterrupt):
                print("\nProgram closed.")
                break


if __name__ == "__main__":
    journal = JournalManager()
    journal.run()
