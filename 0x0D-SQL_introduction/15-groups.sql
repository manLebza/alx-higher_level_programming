--This script lists the number of records with the same score
--In the second_table in the hbtn_0c_0 database in MySQL server
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
