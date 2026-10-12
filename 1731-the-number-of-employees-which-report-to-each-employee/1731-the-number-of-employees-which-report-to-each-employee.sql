# Write your MySQL query statement below

SELECT e1.employee_id, e1.name, e2.reports_count, e2.average_age
FROM Employees as e1
JOIN (SELECT reports_to, COUNT(reports_to) as reports_count, ROUND(AVG(age)) as average_age
        FROM Employees
        WHERE reports_to IS NOT NULL
        GROUP BY reports_to) as e2
ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
ORDER BY e1.employee_id