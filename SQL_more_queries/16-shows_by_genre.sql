-- list all shows and all geners linked to that show
SELECT
    tv.title,
    g.name
FROM tv_genres AS g
LEFT OUTER JOIN tv_show_genres AS tvg ON g.id = tvg.genre_id
RIGHT OUTER JOIN tv_shows AS tv ON tvg.show_id = tv.id
ORDER BY tv.title, g.name ASC;
