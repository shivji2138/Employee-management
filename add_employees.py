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

def add_details():
    ecode = ecode_entry.get()
    name = name_entry.get()
    department = department_entry.get()
    city = city_entry.get()
    job = job_entry.get()
    gender = gender_entry.get()
    dob = dob_entry.get()
    salary = salary_entry.get()
    try:
        sql = "INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (ecode, name, department, city, job, gender, dob, salary)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Success", "Employee added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"ERROR:{err}")

# GUI
window = tk.Tk()
window.title("Add Employees")
window.configure(bg='green')

# Labels
tk.Label(window, bg='green', fg='white', text="Employee Code:").grid(row=0, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="Name:").grid(row=1, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="Department:").grid(row=2, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="City:").grid(row=3, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="Job:").grid(row=4, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="Gender:").grid(row=5, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="Date of Birth:").grid(row=6, column=0,pady=10)
tk.Label(window, bg='green', fg='white', text="Salary:").grid(row=7, column=0,pady=10)

# Entry fields
ecode_entry = tk.Entry(window)
name_entry = tk.Entry(window)
department_entry = tk.Entry(window)
city_entry = tk.Entry(window)
job_entry = tk.Entry(window)
gender_entry = tk.Entry(window)
dob_entry = tk.Entry(window)
salary_entry = tk.Entry(window)

ecode_entry.grid(row=0, column=1,pady=10)
name_entry.grid(row=1, column=1,pady=10)
department_entry.grid(row=2, column=1,pady=10)
city_entry.grid(row=3, column=1,pady=10)
job_entry.grid(row=4, column=1,pady=10)
gender_entry.grid(row=5, column=1,pady=10)
dob_entry.grid(row=6, column=1,pady=10)
salary_entry.grid(row=7, column=1,pady=10)

# Buttons
add_button = tk.Button(window, text="Add Employee",bg='blue',fg='white', command=add_details)
add_button.grid(row=8, column=0,columnspan=2,pady=10)

#mainloop
window.mainloop()
