-- list all the cities of california that can be found in db hbtn_0d_usa
SELECT
    id,
    name
FROM hbtn_0d_usa.cities
WHERE
    state_id = (
        SELECT hbtn_0d_usa.states.id
        FROM hbtn_0d_usa.states
        WHERE hbtn_0d_usa.states.name = 'California'
    )
ORDER BY id ASC;
