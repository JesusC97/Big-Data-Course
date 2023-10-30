-- ¿Cuántas películas de acción hay que duren menos de 60 minutos? Haz un
-- listado de las mismas.

SELECT movie_title
FROM imdb_movies
WHERE duration<60 and gender LIKE '%Action%' 