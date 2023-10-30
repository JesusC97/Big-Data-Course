-- ¿Cuál es el monto de los créditos otorgados y no otorgados según el Status
-- personal?

SELECT personal_status, 
SUM(CASE WHEN class = 'good' THEN 1 ELSE 0 END) AS credito_otorgado,
SUM(CASE WHEN class = 'bad' THEN 1 ELSE 0 END) AS credito_no_otorgado
FROM LoanData
GROUP BY personal_status