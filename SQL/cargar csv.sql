USE paraguay;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\paraguay.csv" INTO TABLE flotaparaguay
FIELDS TERMINATED BY ","
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(`MERCADO`, `SEGMENTO.1`, `MARCA`, `MODELO`,
 `AÑO`, `FLOTA 2019`, `ORIGEN`
);

