# Implementación del algoritmo AES (128) a mano
Autores: 
- Abigail Godoy Araujo A01709167
- Daniela Iliana Rivera García A07107056
- Frida Azenette Hernandez Illescas A01713540
- Monserrat Carrera Leal A01713040

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

## Para el developer:
1. Usamos tablas, no algoritmos complejos
