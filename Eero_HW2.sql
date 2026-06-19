CREATE TABLE employees ( 
id INT PRIMARY KEY, 
name VARCHAR(50), 
department VARCHAR(50), 
salary DECIMAL(10,2), 
hire_date DATE
);

CREATE TABLE projects ( 
id INT PRIMARY KEY, 
project_name VARCHAR(50), 
department VARCHAR(50), 
budget DECIMAL(10,2)
);
INSERT INTO employees VALUES
(1, 'Alice', 'Engineering', 85000, '2019-03-15'),
(2, 'Bob', 'Marketing', 62000, '2021-07-01'),
(3, 'Carol', 'Engineering', 92000, '2017-11-20'),
(4, 'David', 'HR', 54000, '2022-01-10'),
(5, 'Eva', 'Marketing', 71000, '2020-05-30'),
(6, 'Frank', 'Engineering', 78000, '2018-09-05'),
(7, 'Grace', 'HR', 58000, '2023-02-14'),
(8, 'Henry', 'Marketing', 65000, '2019-12-01');

INSERT INTO projects VALUES
(1, 'Alpha', 'Engineering', 150000),
(2, 'Beta', 'Marketing', 80000),
(3, 'Gamma', 'Engineering', 200000),
(4, 'Delta', 'Finance', 95000 ),
(5, 'Epsilon', 'HR', 40000);

-- Task 1 — GROUP BY
-- Show the number of employees and the average salary for each department.Include only those departments 
-- that have more than one employee.
-- Expected columns: department, employee_count, avg_salary
SELECT COUNT(`id`) AS employee_count, department, AVG(salary)
FROM employees
GROUP BY department
HAVING employee_count >1;

-- Task 2 — GROUP BY + ORDER BY
-- Show the total salary expenses for each department, sorted from highest tolowest.
-- Expected columns: department, total_salary
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;

-- Task 3 — ORDER BY
-- Display a list of all employees sorted by salary from highest to lowest. If two employees have the same salary, 
-- sort them by name in alphabetical order.
-- Expected columns: id, name, department, salary
SELECT id, `name`, department, salary
FROM employees
ORDER BY salary DESC, `name` ASC;

-- Task 4 — UNION
-- Compile a single list of all department names that appear in either the employees table or the projects table, 
-- without duplicates.
-- Expected columns: department
SELECT department FROM employees
UNION
SELECT department FROM projects;

-- Task 5 — EXISTS
-- Find all employees who work in a department that has at least one projectassigned to it. Use EXISTS, not JOIN.
-- Expected columns: id, name, department
SELECT id, `name`, department
FROM employees
WHERE EXISTS (
SELECT department 
FROM projects
WHERE employees.department = projects.department
);
