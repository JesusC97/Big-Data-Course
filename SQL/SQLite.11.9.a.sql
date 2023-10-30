-- Queremos saber cuáles son las 20 películas y género al que pertenecen,
-- 1) con mayor presupuesto

SELECT movie_title,gender
FROM imdb_movies
ORDER BY budget DESC
LIMIT 20