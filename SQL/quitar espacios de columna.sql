UPDATE colombia.motocicletas SET `ORIGEN` = REPLACE(`ORIGEN`, '\t', '' );
UPDATE colombia.motocicletas SET `ORIGEN` = REPLACE(`ORIGEN`, '\n', '');
UPDATE colombia.motocicletas SET `ORIGEN` = TRIM(`ORIGEN`);
