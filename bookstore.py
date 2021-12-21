""""
A program that stores information about books in a database using:
Title, Author, Year, ISBN

Users can: 
View all records, search for any entry, add a new entry,
update an existing entry, delete an entry and close the application.
"""
import tkinter
from tkinter import Button, Entry, Label, Listbox, Scrollbar, StringVar, Tk

from database import Database

database = Database()


class Window(object):
    def __init__(self, window):
        self.window = window

        window.wm_title("BookStore")

        # Labels
        title_label = Label(window, text="Title")
        title_label.grid(row=0, column=0)

        author_label = Label(window, text="Author")
        author_label.grid(row=0, column=2)

        year_label = Label(window, text="Year")
        year_label.grid(row=1, column=0)

        isbn_label = Label(window, text="ISBN")
        isbn_label.grid(row=1, column=2)

        # Text entries
        self.title_text = StringVar()
        self.title_entry = Entry(window, textvariable=self.title_text)
        self.title_entry.grid(row=0, column=1)

        self.author_text = StringVar()
        self.author_entry = Entry(window, textvariable=self.author_text)
        self.author_entry.grid(row=0, column=3)

        self.year_text = StringVar()
        self.year_entry = Entry(window, textvariable=self.year_text)
        self.year_entry.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.isbn_entry = Entry(window, textvariable=self.isbn_text)
        self.isbn_entry.grid(row=1, column=3)

        # Book list and scrollbar
        self.book_list = Listbox(window, height=9, width=35)
        self.book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

        book_scrollbar = Scrollbar(window)
        book_scrollbar.grid(row=2, column=2, rowspan=6)

        self.book_list.configure(yscrollcommand=book_scrollbar.set)
        book_scrollbar.configure(command=self.book_list.yview)

        self.book_list.bind("<<ListboxSelect>>", self.get_selected_row)

        # Buttons
        button_viewall = Button(
            window, text="View all", width=12, command=self.view_all
        )
        button_viewall.grid(row=2, column=3)

        button_search = Button(
            window, text="Search", width=12, command=self.search
        )
        button_search.grid(row=3, column=3)

        button_add = Button(
            window, text="Add new", width=12, command=self.add_entry
        )
        button_add.grid(row=4, column=3)

        button_update = Button(
            window,
            text="Update selected",
            width=12,
            command=self.update_selected,
        )
        button_update.grid(row=5, column=3)

        button_delete = Button(
            window,
            text="Delete selected",
            width=12,
            command=self.delete_selected,
        )
        button_delete.grid(row=6, column=3)

        button_close = Button(
            window, text="Close", width=12, command=window.destroy
        )
        button_close.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            global selected_row

            index = self.book_list.curselection()[0]
            selected_row = self.book_list.get(index)

            self.title_entry.delete(0, tkinter.END)
            self.title_entry.insert(tkinter.END, selected_row[1])
            self.author_entry.delete(0, tkinter.END)
            self.author_entry.insert(tkinter.END, selected_row[2])
            self.year_entry.delete(0, tkinter.END)
            self.year_entry.insert(tkinter.END, selected_row[3])
            self.isbn_entry.delete(0, tkinter.END)
            self.isbn_entry.insert(tkinter.END, selected_row[4])
        except IndexError:
            pass

    def view_all(self):
        self.book_list.delete(0, tkinter.END)
        for row in database.view():
            self.book_list.insert(tkinter.END, row)

    def search(self):
        self.book_list.delete(0, tkinter.END)
        for row in database.search(
            self.title_text.get() if self.title_text.get() != "" else None,
            self.author_text.get() if self.author_text.get() != "" else None,
            self.year_text.get() if self.year_text.get() != "" else None,
            self.isbn_text.get() if self.isbn_text.get() != "" else None,
        ):
            self.book_list.insert(tkinter.END, row)

    def add_entry(self):
        database.insert(
            self.title_text.get() if self.title_text.get() != "" else None,
            self.author_text.get() if self.author_text.get() != "" else None,
            self.year_text.get() if self.year_text.get() != "" else None,
            self.isbn_text.get() if self.isbn_text.get() != "" else None,
        )
        self.book_list.delete(0, tkinter.END)
        self.book_list.insert(
            tkinter.END,
            (
                self.title_text.get(),
                self.author_text.get(),
                self.year_text.get(),
                self.isbn_text.get(),
            ),
        )

    def update_selected(self):
        database.update(
            selected_row[0],
            self.title_text.get(),
            self.author_text.get(),
            self.year_text.get(),
            self.isbn_text.get(),
        )

    def delete_selected(self):
        database.delete(selected_row[0])


window = Tk()
Window(window)

window.mainloop()
