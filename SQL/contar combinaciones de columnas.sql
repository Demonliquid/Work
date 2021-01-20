SELECT MERCADO, `SEGMENTO.1`, MARCA, MODELO, count(*) as 'count'
FROM guatemala.flotaguatemala
WHERE `SEGMENTO.1` in ('PICK UP', 'CAMIONETA', 'CAMION', 'CAMION FURGON', 'CAMIONETILLA' ,'CAMIONETA SPORT')
GROUP BY MARCA, MODELO, `SEGMENTO.1`
order by count DESC;