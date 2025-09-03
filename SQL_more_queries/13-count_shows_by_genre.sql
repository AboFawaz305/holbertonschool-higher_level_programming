-- list genres and the number of shows in it
SELECT
    g.name AS genre,
    COUNT(tvg.genre_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tvg ON g.id = tvg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
