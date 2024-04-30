import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Narayanan",
    database="employee_management"
)
cursor =db.cursor()
def home_screen():
    print("Welcome to Employee DBMS")
    print("1.ADD EMPLOYEE")
    print("2.SEARCH EMPLOYEE")
    print("3.DELETE EMPLOYEE")
    print("4.EXIT")
    choice=int(input("Enter the choice (1,2,3 or 4):"))
    if choice == 1:
        add_details()
        return True
    elif choice == 2:
        search_employee()
        return True
    elif choice ==3:
        delete_employee()
        return True
    elif choice ==4:
        return False
    else:
        print("Invalid Choice")
        return True
        

def add_details():
    ecode= int(input("Enter the employee code:"))
    name= input("Enter the name of employee:")
    department = input("Enter the department:")
    city= input("Enter the city")
    job = input("Enter the JOB:")
    gender = input("Entry the gender")
    dob = input("Enter date of birth:")
    salary = float(input("Enter Salary:"))
    
    sql= "INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (ecode,name,department,city,job,gender,dob,salary)
    cursor.execute(sql,val)
    db.commit()

def search_employee():
    ecode = int(input("Enter ID to Search"))
    sql= "SELECT* FROM EMPLOYEE WHERE Ecode =%s"
    cursor.execute(sql,(ecode,))
    emps = cursor.fetchone()
    if emps:
        print(f'''Employee Found:
            NAME: {emps[1]}
            DEPARTMENT: {emps[2]}
            CITY: {emps[3]}
            JOB: {emps[4]}
            GENDER: {emps[5]}
            DOB: {emps[6]}
            SALARY: {emps[7]}''')
    else:
        print("EMPLOYEE NOT FOUND.")

def delete_employee():
    ecode = int(input("Enter ID to REMOVE:"))
    cursor.execute("DELETE FROM EMPLOYEE WHERE Ecode = %s",(ecode,))
    conn.commit()
    print("REMOVED SUCCESSFULLY")
        
while True:
    if not home_screen():
        break
    

