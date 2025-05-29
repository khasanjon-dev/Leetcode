create table Employee;

select name as Employee
from Employee E
         INNER JOIN (select id, salary from Employee) M ON E.managerId = M.id
where E.salary >= M.salary;