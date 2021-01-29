SET GLOBAL local_infile = 1;
USE honduras;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\honduras.csv" INTO TABLE honduras.flotahonduras
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(`AÑO`, `SEGMENTO.1`, `COMBUSTIBLE`,
`MARCA`, `MODELO/VERSION`, `CILINDRADA`,
 `FLOTA 2019`, `MERCADO`);