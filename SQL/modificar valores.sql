UPDATE guatemala.flotaguatemala
SET MODELO = 'HILUX'
WHERE MARCA = 'TOYOTA' AND MODELO in ('HI LUX', '4X2 STD', '4X4 DLX', '4X4', '4WD', '4X2', 'XTRA CAB 4X4 DLX', 'XTRA CAB 4X2 DLX', 'STD 4X2', '4X4 STD', 'XTRA CAB 4X4', '4X2 DLX', 'XTRA CAB 4X2', 'STANDARD', 'X/C 4X2 DLX', '4X4 SR5', 'SENCILLO');

UPDATE guatemala.flotaguatemala
SET MODELO = 'RAV4'
WHERE MARCA = 'TOYOTA' AND MODELO LIKE '%RAV%4%';


UPDATE guatemala.flotaguatemala
SET MODELO = '4RUNNER'
WHERE MARCA = 'TOYOTA' AND MODELO LIKE '%4RUNNER%';


UPDATE guatemala.flotaguatemala
SET MODELO = 'TACOMA'
WHERE MARCA = 'TOYOTA' AND MODELO LIKE '%TACOMA%';
