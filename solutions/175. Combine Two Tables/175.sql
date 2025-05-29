SELECT p.firstName as "firstName", p.lastName as "lastName", A.city, A.state
FROM Person P
         LEFT JOIN Address A on P.personID = A.personID;