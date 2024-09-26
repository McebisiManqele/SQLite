import sqlite3

from employee import Employee 
# Connect to the database
conn = sqlite3.connect(":memory:")
c = conn.cursor()

# Drop the table if it exists
c.execute("DROP TABLE IF EXISTS employees")

# Create table with the correct columns
c.execute("""CREATE TABLE employees (
             first text,
             last text,
             pay integer
             )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))
        

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""",
                  {'first':emp.first, 'last':emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first':emp.first, 'last':emp.last})

emp_1= Employee('John','Doe', 80000)
emp_2= Employee('Jane','Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)



update_pay(emp_2, 95000)
remove_emp(emp_1)

emps= get_emps_by_name('Doe')
print(emps)
# Close the connection
conn.close()

