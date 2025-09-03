-- list all the cities of california that can be found in db hbtn_0d_usa
SELECT
    id,
    name
FROM cities
WHERE
    state_id = (
        SELECT states.id
        FROM states
        WHERE states.name = 'California'
    )
ORDER BY id ASC;
