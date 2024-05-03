import subprocess
import tkinter as tk


def redirect(scripth_path):
    subprocess.run(['python', scripth_path])

#tkinter window
window = tk.Tk()
window.title("Home Page")
window.configure(bg="green")
window.geometry('400x400')

#gui components
msg_label = tk.Label(window, text='''Welcome to
Srivathsan Technical Solutions'
Employee DBMS''',bg='green',fg='white',font=('Helvetica',20))
msg_label.pack(pady=10)

addemp_button = tk.Button(window, text="ADD EMPLOYEE", bg="red",fg="white",command=lambda:redirect("add_employees.py"))
addemp_button.pack(pady=10)

searchemp_button = tk.Button(window, text="SEARCH EMPLOYEE",bg="red", fg='white',command=lambda:redirect("search_employees.py"))
searchemp_button.pack(pady=10)

delemp_button = tk.Button(window, text="DELETE EMPLOYEE", bg="red",fg='white', command=lambda:redirect("delete_employee.py"))
delemp_button.pack(pady=10)

#mainloop
window.mainloop()
