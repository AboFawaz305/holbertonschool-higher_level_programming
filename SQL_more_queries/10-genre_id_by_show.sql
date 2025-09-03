-- list all shows contained that have at least one genre linked
SELECT
    tv.title,
    tvg.genre_id
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS tvg ON tv.id = tvg.show_id
ORDER BY tv.title, tvg.genre_id ASC;
