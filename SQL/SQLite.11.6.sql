-- Identificar y calcular el presupuesto de aquellas películas de James Bond que
-- fueron dirigidas por John Glen y protagonizadas por Timothy Dalton.

SELECT sum(budget) as presupuesto_total
FROM jamesbond
WHERE director='John Glen' and actor='Timothy Dalton'