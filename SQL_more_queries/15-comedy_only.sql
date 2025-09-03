-- list comedy shows
SELECT DISTINCT tv.title
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tvg ON g.id = tvg.genre_id
INNER JOIN tv_shows AS tv ON tvg.show_id = tv.id
WHERE g.name = "Comedy"
ORDER BY tv.title ASC;
