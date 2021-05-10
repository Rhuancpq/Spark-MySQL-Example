from typing import Set
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root123',
                              host='mysql',
                              database='employees')

cursor = cnx.cursor()

query = ("""
SELECT D.dept_name, SUM(S.salary)
FROM DEPARTMENTS D INNER JOIN dept_emp de ON D.dept_no = de.dept_no
INNER JOIN EMPLOYEES E ON de.emp_no = E.emp_no
INNER JOIN SALARIES S ON E.emp_no = S.emp_no
WHERE S.from_date BETWEEN '2000-01-01' AND '2000-01-31'
GROUP BY D.dept_no
""")

cursor.execute(query)
