-- Mostrar el conteo de las películas relacionadas con los géneros (Action, Crime,
-- Comedy, Drama, Romance), indicando la película con mayor número de votos
-- en cada caso (num_voted_users).

SELECT
CASE WHEN gender LIKE'%Action%' THEN 'pelis_accion'
WHEN gender LIKE '%Crime%' THEN 'pelis_crimen'
WHEN gender LIKE'%Comedy%' THEN 'pelis_comedia'
WHEN gender LIKE'%Drama%' THEN 'pelis_drama'
WHEN gender LIKE'%Romance%' THEN 'pelis_romance' END as genero, 
COUNT(*) AS cantidad_peliculas, max(num_voted_users),movie_title
FROM imdb_movies
WHERE genero IS NOT NULL
GROUP BY genero