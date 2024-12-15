import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, END

# Database Setup
def setup_database():
    conn = sqlite3.connect("simple_database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()

# Add Record to Database
def add_record():
    name = name_entry.get()
    if name:
        conn = sqlite3.connect("simple_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        name_entry.delete(0, END)
        view_records()

# View Records
def view_records():
    record_list.delete(0, END)
    conn = sqlite3.connect("simple_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    for row in rows:
        record_list.insert(END, f"{row[0]}: {row[1]}")
    conn.close()

# Delete Selected Record
def delete_record():
    selected = record_list.get(record_list.curselection())
    record_id = selected.split(":")[0]
    conn = sqlite3.connect("simple_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
    conn.commit()
    conn.close()
    view_records()

# GUI Setup
setup_database()
root = Tk()
root.title("Simple Database GUI")

Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Add Record", command=add_record).grid(row=0, column=2, padx=10, pady=10)
Button(root, text="Delete Selected", command=delete_record).grid(row=1, column=2, padx=10, pady=10)

record_list = Listbox(root, width=50)
record_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

view_records()

root.mainloop()