-- Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Does not list rows without a name value
-- Listed in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
