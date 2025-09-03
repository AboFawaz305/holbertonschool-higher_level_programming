-- list genres and the number of shows in it
SELECT DISTINCT g.name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tvg ON g.id = tvg.genre_id
INNER JOIN tv_shows AS tv ON tvg.show_id = tv.id
WHERE tv.title = "Dexter"
ORDER BY g.name ASC;
