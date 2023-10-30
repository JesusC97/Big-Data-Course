-- Obtén un listado de las películas de acción con actor protagonista con más de
-- 10000 likes en Facebook y cuyas películas hayan sido valoradas con al menos
-- un 8 en imdb. Todo ello con fechas anteriores a 2012.

SELECT movie_title
FROM imdb_movies
WHERE gender LIKE '%Action%' AND imdb_score>=8 AND title_year<2012 AND actor_1_facebook_likes > 10000
