# Implementación del algoritmo AES (128) a mano
Autores: 
- Abigail Godoy Araujo A01709167
- Daniela Iliana Rivera García A07107056
- Frida Azenette Hernandez Illescas A01713540
- Montserrat Carrera Leal A01713040

## Sobre el algoritmo
El algoritmo AES es un algoritmo de encriptación

1. La llave TIENE QUE SER DE 128 BYTES: e.g. 3034a1475043f4cacf4d46a8625a53f9
2. El texto puede ser de cualquier longitud
3. En ambos archivos .txt , no agregar nada más que el texto a usarse.

## Etapas
Etapas básicas del AES:

1. Key expansion: su utiliza para generar una subllave para cada ronda a partir de la llave original.
2. Sub Bytes (substitute bytes): utiliza una matriz S-box para realizar una substitución byte a byte del bloque del estado.
3. Shift Rows: realiza una permutación simple de bytes
4. Mix Columns: substitución que usa aritmética de campos finitos sobre GF(28).
5. Add round key: mezcla la llave expandida con el bloque de estado.

Nota: Cada etapa fue realizada por X

## Tablas
Se hace uso de tablas en lugar de la implementación de la aritmética de campos finitos.

## Comparación con Cryptool
Para comparar con Cryptool, abra el archivo con este formato:

Para el Caso 1, disponible en este repositorio:
``python -c "data = open('Casos/Resultados/Caso1.txt.enc', 'rb').read(); print(' '.join(f'{b:02X}' for b in data[:16]))" ``

Para el Caso 2, disponible en este repositorio:
`` python -c "data = open('Casos/Resultados/Caso2.txt.enc', 'rb').read(); print(' '.join(f'{b:02X}' for b in data[:16]))" ``

Para cualquier archivo encriptado, léalo utilizando
`` python -c "data = open('{RUTA ARCHIVO}', 'rb').read(); print(' '.join(f'{b:02X}' for b in data[:16]))" ``


## Resultados por caso
Caso 1:
- Texto: "lagallinaestaenl"
- Llave: "FF0102030405060708090A0B0C0D0E0F"
- Resultado en terminal: ``8A 72 0C 5E 9B D4 FF FB 62 CF D8 D7 68 54 D6 4B``

Caso 2:
- Texto: "SecurityTest1234"
- Llave: "FF0102030405060708090A0B0C0D0E0F"
- Resultado en terminal: ``20 0D 78 04 04 DA 50 39 A1 38 01 3F 4F A9 F3 EF``

