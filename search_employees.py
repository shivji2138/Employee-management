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

def search_employee():
    ecode = ecode_entry.get()
    sql = "SELECT * FROM EMPLOYEE WHERE Ecode = %s"
    cursor.execute(sql, (ecode,))
    emp = cursor.fetchone()
    if emp:
        messagebox.showinfo("Employee Found", f'''Employee Found:
            NAME: {emp[1]}
            DEPARTMENT: {emp[2]}
            CITY: {emp[3]}
            JOB: {emp[4]}
            GENDER: {emp[5]}
            DOB: {emp[6]}
            SALARY: {emp[7]}''')
    else:
        messagebox.showinfo("Employee Not Found", "EMPLOYEE NOT FOUND.")

#tkinter window
window = tk.Tk()
window.title("Search Employees")
window.configure(bg='green')
window.geometry('300x300')

#gui components
tk.Label(window, text="Employee Code:",bg='green',fg='white').pack(pady=10)
ecode_entry = tk.Entry(window)
ecode_entry.pack(pady=10)

search_button = tk.Button(window, text="Search Employee",bg='skyblue', command=search_employee)
search_button.pack(pady=10)

#mainloop
window.mainloop()
