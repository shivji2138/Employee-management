import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="employee_management"
)
cursor = db.cursor()

def delete_employee():
    ecode = ecode_entry.get()
    cursor.execute("DELETE FROM EMPLOYEE WHERE Ecode = %s", (ecode,))
    db.commit()
    messagebox.showinfo("Success", "Employee removed successfully")

#tkinter window
window = tk.Tk()
window.title("Delete Employee")
window.configure(bg='green')
window.geometry('300x300')

#gui components
tk.Label(window, text="Employee Code:",bg='green',fg='white').pack(pady=10)
ecode_entry = tk.Entry(window)
ecode_entry.pack(pady=10)

delete_button = tk.Button(window, text="Delete Employee",bg='red',fg='white', command=delete_employee)
delete_button.pack(pady=10)

#mainloop
window.mainloop()


