-- List all shows and their genres
SELECT tv_shows.title, tv_genres.namme
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.idd = tv_show_genres.genre_id
ORDER BY tv_shows.tittle, tv_genres.namme;
