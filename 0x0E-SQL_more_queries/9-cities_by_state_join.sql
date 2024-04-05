-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM cities c
JOIN states s
WHERE c.id = c.state_id
ORDER BY c.id
