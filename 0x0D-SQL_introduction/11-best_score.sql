--This script lists all records with a score >= 10 in the
--second_table of the hbtn_0c_0 database in MySQL server
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
