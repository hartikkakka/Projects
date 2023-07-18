import sqlite3


def connect():
    # Connect to the database
    conn = sqlite3.connect("books.db")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Create a table named 'book' if it doesn't already exist
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, "
                "isbn integer)")
    # Commit the changes to the database
    conn.commit()
    # Close the connection
    conn.close()


def insert(title, author, year, isbn):
    # Connect to the database
    conn = sqlite3.connect("books.db")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Insert a new row into the 'book' table with the provided values
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    # Commit the changes to the database
    conn.commit()
    # Close the connection
    conn.close()
    # Call the 'view' function to display all books in the database
    view()


def view():
    # Connect to the database
    conn = sqlite3.connect("books.db")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Retrieve all rows from the 'book' table
    cur.execute("SELECT * FROM book")
    # Fetch all the rows as a list of tuples
    rows = cur.fetchall()
    # Close the connection
    conn.close()
    # Return the fetched rows
    return rows


def search(title="", author="", year="", isbn=""):
    # Connect to the database
    conn = sqlite3.connect("books.db")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Search for books matching the provided criteria in the 'book' table
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    # Fetch all the matching rows as a list of tuples
    rows = cur.fetchall()
    # Close the connection
    conn.close()
    # Return the fetched rows
    return rows


def delete(id):
    # Connect to the database
    conn = sqlite3.connect("books.db")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Delete the book with the specified id from the 'book' table
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    # Commit the changes to the database
    conn.commit()
    # Close the connection
    conn.close()


def update(id, title, author, year, isbn):
    # Connect to the database
    conn = sqlite3.connect("books.db")
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    # Update the book with the specified id in the 'book' table with the provided values
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    # Commit the changes to the database
    conn.commit()
    # Close the connection
    conn.close()
