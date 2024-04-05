-- Lists all he cities of California in the hbtn_0d_usa databse
SELECT id, name
FROM cities
WHERE state_id = 
(SELECT id FROM states
	   WHERE name = 'California');
