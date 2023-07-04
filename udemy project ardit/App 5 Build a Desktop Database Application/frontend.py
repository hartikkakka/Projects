from tkinter import *
import backend


def get_selected_row(event):
    # This function is triggered when a user selects a row in the listbox.
    global selected_tuple
    # Get the index of the selected row
    index = list1.curselection()[0]
    # Retrieve the selected tuple from the listbox
    selected_tuple = list1.get(index)
    # Clear the entry fields
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    # This function is triggered when the "View all" button is clicked.
    list1.delete(0, END)
    # Retrieve all books from the database using the backend view() function
    for row in backend.view():
        # Insert each book into the listbox
        list1.insert(END, row)


def search_command():
    # This function is triggered when the "Search entry" button is clicked.
    list1.delete(0, END)
    # Retrieve books matching the search criteria using the backend search() function
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        # Insert each matching book into the listbox
        list1.insert(END, row)


def add_command():
    # This function is triggered when the "Add entry" button is clicked.
    # Insert a new book into the database using the backend insert() function
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    # Clear the entry fields
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    # Refresh the listbox to display the updated book list
    view_command()


def delete_command():
    # This function is triggered when the "Delete selected" button is clicked.
    # Delete the selected book from the database using the backend delete() function
    backend.delete(selected_tuple[0])
    # Refresh the listbox to remove the deleted book
    view_command()


def update_command():
    # This function is triggered when the "Update selected" button is clicked.
    # Update the selected book in the database using the backend update() function
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    # Refresh the listbox to display the updated book list
    view_command()


window = Tk()
window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
