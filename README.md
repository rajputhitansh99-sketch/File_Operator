Personal Journal Manager

About the Project
Personal Journal Manager is a simple Python program that allows users to add, view, and search journal entries. It also provides an option to delete all saved entries.

The program stores journal entries in a text file named journal.txt. Each entry contains the date and time when it was saved.
How to Run the Program
1. Make sure Python is installed on your computer.
2. Open the terminal in the folder containing your Python file.
3. Run the following command:
python "FileOperator(Project-6).py"


On Windows, you can also use:
py "FileOperator(Project-6).py"


Program Output
When you run the program, the following menu appears:
Welcome to Personal Journal Manager!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
Enter your choice:


Select an option by entering its corresponding number.
1. Add a New Entry
Enter 1 to add a new journal entry.

Sample output:
Enter your choice: 1

Enter your journal entry:
Today I completed my Python project.
Entry added successfully!


The program saves the entry in journal.txt along with the current date and time.

Example of saved content in journal.txt:
[2026-10-25 18:30:00]
Today I completed my Python project.
--------------------------------------------------


The timestamp above is an example. The program records the actual date and time. If the entry is empty, the program displays an error message and does not save it.
2. View All Entries
Enter 2 to display all saved journal entries.

Sample output:
Enter your choice: 2

Your Journal Entries:

[2026-10-25 18:30:00]
Today I completed my Python project.
--------------------------------------------------
[2026-10-25 19:00:00]
I revised Python file handling.
--------------------------------------------------


The program reads the contents of journal.txt and displays all saved entries.

If the journal file does not exist, the program displays an appropriate error message.
3. Search for an Entry
Enter 3 to search for a journal entry using a keyword or date.

Sample output:
Enter your choice: 3

Enter a keyword or date to search: Python

Matching Entries:

[2026-10-25 18:30:00]
Today I completed my Python project.
--------------------------------------------------

[2026-10-25 19:00:00]
I revised Python file handling.
--------------------------------------------------


The search is case-insensitive, which means Python and python can both match.

If no entry matches the search term, the program displays:
No entries were found for the keyword: Python.


The actual keyword in this message depends on what the user enters.
4. Delete All Entries
Enter 4 to delete all journal entries. The program asks for confirmation before deleting the file.

Sample output when deletion is cancelled:
Enter your choice: 4

Are you sure you want to delete all entries? (yes/no): no
Deletion cancelled.


Sample output when deletion is confirmed:
Enter your choice: 4

Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.


When the user enters yes, the program clears the journal file and then deletes it. This action cannot be undone through the application.
5. Exit the Program
Enter 5 to exit the application.

Sample output:
Enter your choice: 5
Thank you for using Personal Journal Manager.


The program closes after displaying the message.
Main Methods Used
The project uses a class named JournalManager to organize its operations.
- __init__() — Initializes the journal filename and the separator used between entries.
- add_entry() — Accepts a new entry, adds a timestamp, and saves it to the file.
- view_entries() — Reads and displays all saved journal entries.
- search_entry() — Searches journal entries for a keyword or date.
- delete_all_entries() — Requests confirmation, clears the file, and deletes it.
- run() — Displays the menu and executes the operation selected by the user.
The program also uses exception handling to manage errors such as missing files, permission problems, and other file-related issues.
Project Files
- FileOperator(Project-6).py — Contains the Python source code.
- README.md — Explains the project and demonstrates its output.
- journal.txt — Stores journal entries and is created automatically when the first entry is added.
Conclusion
Personal Journal Manager is a beginner-friendly Python project that demonstrates object-oriented programming, file handling, user input, timestamps, and exception handling. It provides a simple way to store, view, and search personal journal entries through a menu-driven interface.
