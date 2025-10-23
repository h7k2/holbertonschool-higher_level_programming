-- 13-count_shows_by_genre.sql (version "un peu faux")
SELECT g.name AS genre, COUNT(sg.show_id) AS nb_shows
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY nb_shows ASC;
