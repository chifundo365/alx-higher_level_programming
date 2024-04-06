-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM cities c
JOIN states s
ON c.id = c.state_id
ORDER BY c.id
