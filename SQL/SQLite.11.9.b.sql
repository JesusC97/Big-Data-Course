-- Queremos saber cuáles son las 20 películas y género al que pertenecen,
-- 2) con mayor beneficio

SELECT movie_title,gender
FROM imdb_movies
ORDER BY gross DESC
LIMIT 20