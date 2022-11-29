--This script lists all records of table second_table
--which have a name value in the hbtn_0c_0 database in MySQL server.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
