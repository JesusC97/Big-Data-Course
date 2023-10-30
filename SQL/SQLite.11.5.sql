-- Mostrar el número de personajes que tienen el mismo color de ojos (eye_color)
-- y el planeta de origen (homeworld). No mostrar color de ojos desconocidos
-- (unknown) ni planetas sin datos/nombre (NA).

SELECT eye_color,count(name) as numero_de_personajes
FROM star_wars_characters_2
WHERE eye_color != 'unknown' AND homeworld != 'NA'
GROUP BY eye_color
ORDER BY COUNt(name) DESC