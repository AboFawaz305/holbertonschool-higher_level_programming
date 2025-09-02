-- list all records of second_table where the name does contain a value 
SELECT
    score,
    name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;
