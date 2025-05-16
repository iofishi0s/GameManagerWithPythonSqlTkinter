import tkinter as tk
from tkinter import messagebox
from sindesi import get_connection


def insert_game(GameName,year,CompanyName):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO games(GameName,year,CompanyName) values()"
    values = (GameName,year,CompanyName)
    cursor.execute(query, values)
    print("To paixnidi prostethike")
    cursor.close()
    connection.close

GameName= input("dwse onoma paixnidiou: ")
year=int(input("eisagetai etos: "))
CompanyName=input("eiasgetai etairis: ")

insert_game(GameName,year,CompanyName)


# Συνάρτηση για εισαγωγή βιβλίου
def insert_book(GameName,year,CompanyName):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO books (GameName,year,CompanyName) VALUES (%s, %s, %s)"
        values = (GameName,year,CompanyName)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print("Σφάλμα:", e)
        return False

# Συνάρτηση για χειρισμό του κουμπιού
def submit_book():
    GameName = entry_GameName.get()
    year = entry_year.get()
    CompanyName = entry_CompanyName.get()

    if not (GameName and year and CompanyName ):
        messagebox.showwarning("Σφάλμα", "Συμπλήρωσε όλα τα πεδία!")
        return

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Σφάλμα", "Το έτος πρέπει να είναι αριθμός!")
        return

    if insert_book(GameName,year,CompanyName):
        messagebox.showinfo("Επιτυχία", "Το βιβλίο προστέθηκε επιτυχώς!")
        entry_GameName.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_CompanyName.delete(0, tk.END)
    else:
        messagebox.showerror("Αποτυχία", "Αποτυχία εισαγωγής βιβλίου.")

# Δημιουργία παραθύρου
window = tk.Tk()
window.title("Εισαγωγή Βιβλίου")
window.geometry("400x300")

# Ετικέτες και πεδία
tk.Label(window, text="Onoma Paixnidiou:").pack(pady=5)
entry_GameName = tk.Entry(window, width=40)
entry_GameName.pack()

tk.Label(window, text="Xronologia:").pack(pady=5)
entry_year = tk.Entry(window, width=40)
entry_year.pack()

tk.Label(window, text="Onoma Etairias:").pack(pady=5)
entry_CompanyName = tk.Entry(window, width=40)
entry_CompanyName.pack()

# Κουμπί καταχώρησης
submit_button = tk.Button(window, text="Καταχώρηση Βιβλίου", command=submit_book)
submit_button.pack(pady=20)

# Εκκίνηση εφαρμογής
window.mainloop()

