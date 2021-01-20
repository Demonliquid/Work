SELECT PATENTE, COUNT(PATENTE) AS cantidad
FROM chile.bbddchile
GROUP BY PATENTE
HAVING (cantidad > 1)
order by cantidad DESC;