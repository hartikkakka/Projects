
# BookStore App

This is a simple BookStore app built using the Tkinter library in Python. The app allows users to manage a collection of books by performing various operations such as adding, updating, searching, and deleting books. The app utilizes a backend module to interact with a SQLite database to store and retrieve book information.

## Installation

1. Make sure you have Python installed (version 3.7 or higher).
2. No additional dependencies are required. Tkinter comes pre-installed with Python.

## Usage

1. Clone the repository or download the source code files.
2. Navigate to the project directory.
3. Run the `frontend.py` file using Python:
   ```python
   python frontend.py

4. The BookStore app will be launched.
5. Use the provided entry fields to add, update, or search for books.
6. The listbox displays the books currently in the database.
7. To view all books, click the "View all" button.
8. To search for a specific book, enter the search criteria and click the "Search entry" button.
9. To add a new book, enter the book details and click the "Add entry" button.
10. To update the selected book, make the necessary changes in the entry fields and click the "Update selected" button.
11. To delete the selected book, click the "Delete selected" button.
12. Click the "Close" button to exit the application.

## File Structure

- `frontend.py`: The main Python file that contains the GUI code and handles user interactions.
- `backend.py`: The backend module that interacts with the SQLite database to perform CRUD operations on book data.

## Functions

The app includes the following functions:

- `get_selected_row(event)`: Triggered when a user selects a row in the listbox. Retrieves the selected book's details and populates the entry fields.
- `view_command()`: Triggered when the "View all" button is clicked. Retrieves and displays all books from the database.
- `search_command()`: Triggered when the "Search entry" button is clicked. Searches for books based on the provided search criteria.
- `add_command()`: Triggered when the "Add entry" button is clicked. Adds a new book to the database.
- `delete_command()`: Triggered when the "Delete selected" button is clicked. Deletes the selected book from the database.
- `update_command()`: Triggered when the "Update selected" button is clicked. Updates the selected book in the database.

## GUI Components

The app consists of the following GUI components:

- Labels: Displaying text for each entry field (Title, Author, Year, ISBN).
- Entry fields: Input fields for the book details.
- Listbox: Displaying the list of books.
- Scrollbar: Enabling scrolling in the listbox.
- Buttons: Performing various operations (View all, Search entry, Add entry, Update selected, Delete selected, Close).
