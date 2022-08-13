-- A script that print all the recording of second_tabele
-- Recording should be orderde by a scrore and Greater than or equl to 10
SELECT score, name
FROM second_table
WHERE score >= 10
    ORDER BY score DESC;