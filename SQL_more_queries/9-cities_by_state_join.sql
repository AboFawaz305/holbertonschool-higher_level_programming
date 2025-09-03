-- list all cities hbtn_0d_usa
SELECT
    hbtn_0d_usa.cities.id,
    hbtn_0d_usa.cities.name,
    hbtn_0d_usa.states.name
FROM hbtn_0d_usa.cities
INNER JOIN hbtn_0d_usa.states
    ON hbtn_0d_usa.cities.state_id = hbtn_0d_usa.states.id
ORDER BY cities.id ASC;
