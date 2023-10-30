-- ¿Cuántas películas duran menos de 60 minutos?; ¿Cuántas entre 60 y 100? Y
-- ¿Cuántas más de 100?

SELECT
    SUM(CASE WHEN duration < 60 THEN 1 ELSE 0 END) AS ' < 60 min',
    SUM(CASE WHEN duration BETWEEN 60 and 100 THEN 1 ELSE 0 END) AS '60 min < x < 100 min',
    SUM(CASE WHEN duration >= 100 THEN 1 ELSE 0 END) AS '> 100 min',
    COUNT(movie_title) as pelis_totales
FROM imdb_movies
