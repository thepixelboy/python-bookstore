""""
A program that stores information about books in a database using:
Title, Author, Year, ISBN

Users can: 
View all records, search for any entry, add a new entry,
update an existing entry, delete an entry and close the application.
"""
from tkinter import Button, Entry, Label, Listbox, Scrollbar, StringVar, Tk

window = Tk()

# Frontend
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
title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

# Book list and scrollbar
book_list = Listbox(window, height=9, width=35)
book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

book_scrollbar = Scrollbar(window)
book_scrollbar.grid(row=2, column=2, rowspan=6)

book_list.configure(yscrollcommand=book_scrollbar.set)
book_scrollbar.configure(command=book_list.yview)

# Buttons
button_viewall = Button(window, text="View all", width=12)
button_viewall.grid(row=2, column=3)

button_search = Button(window, text="Search", width=12)
button_search.grid(row=3, column=3)

button_add = Button(window, text="Add new", width=12)
button_add.grid(row=4, column=3)

button_update = Button(window, text="Update selected", width=12)
button_update.grid(row=5, column=3)

button_delete = Button(window, text="Delete selected", width=12)
button_delete.grid(row=6, column=3)

button_close = Button(window, text="Close", width=12)
button_close.grid(row=7, column=3)


window.mainloop()
