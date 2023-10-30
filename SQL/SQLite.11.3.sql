-- ¿Cuál sería el día de menos cotización en una tendencia alcista en el año
-- 2018?; ¿Y la media ese mismo día?

SELECT date, avg(open+high+low+close) AS media_aritmetica
FROM bitcoin_daily_rates_formatdate
GROUP BY date
HAVING STRFTIME('%Y',date) ='2018' 
ORDER BY min(high)
LIMIT 1