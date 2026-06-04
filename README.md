# Implementación del algoritmo AES (128) a mano
Autores: 
- Abigail Godoy Araujo A01709167
- Daniela Iliana Rivera García A07107056
- Frida Azenette Hernandez Illescas A01713540
- Montserrat Carrera Leal A01713040

# Sobre el algoritmo

## Implementación del Algoritmo AES en Python

Este proyecto implementa el algoritmo **AES (Advanced Encryption Standard)** para el cifrado de datos.

AES es un estándar de cifrado simétrico ampliamente utilizado, que opera sobre bloques de **128 bits** y utiliza claves de **128, 192 o 256 bits**.

***

# -- FLUJO GENERAL DEL ALGORITMO --

El proceso de cifrado AES se divide en las siguientes etapas:

1. **Expansión de la llave (Key Expansion)**
2. **Rondas de cifrado**
3. **Transformaciones internas por ronda**

***

# 1. Expansión de la llave (Key Expansion)

Antes de comenzar el cifrado, la clave original se expande en varias subclaves.

* Para AES-128:
  * Se generan **11 llaves de ronda**
* Cada una se usa en una ronda del algoritmo

### Operaciones principales:

* Rotación de bytes (`rotate`)
* Sustitución con la S-Box (`SubBytes`)
* XOR con constantes (`Rcon`)

Esto permite que cada ronda utilice una clave distinta, aumentando la seguridad.
***

# 2. Proceso de cifrado

AES trabaja sobre una estructura llamada **estado (state)**:

* Matriz de 4x4 bytes (16 bytes = 128 bits)

El cifrado sigue este flujo:

```text
Estado inicial
↓
AddRoundKey (clave inicial)

Para cada ronda:
    SubBytes
    ShiftRows
    MixColumns
    AddRoundKey

Última ronda (sin MixColumns):
    SubBytes
    ShiftRows
    AddRoundKey
```

***

# 3. Transformaciones del AES

## 3.1 AddRoundKey

* Se hace un **XOR** entre el estado y la subclave:

$$
Estado = Estado \oplus Llave
$$

Es el único paso que usa directamente la clave.

***

## 3.2 SubBytes

* Sustitución byte a byte usando la **S-Box**
* Introduce **no linealidad**

Cada byte se reemplaza por otro según una tabla.

Aumenta la resistencia contra ataques criptográficos.

***

## 3.3 ShiftRows

* Desplaza filas de la matriz:

| Fila | Desplazamiento |
| ---- | -------------- |
| 1    | 0              |
| 2    | 1 izquierda    |
| 3    | 2 izquierda    |
| 4    | 3 izquierda    |

Mezcla la información entre columnas.

***

## 3.4 MixColumns

* Opera por columnas usando aritmética en **GF(2⁸)**

Cada columna se transforma usando multiplicaciones y XOR.

Ejemplo conceptual:

$$
Columna = Matriz ⋅ Columna
$$

 Difunde los datos (efecto avalancha)
 El código utiliza la tabla **SXBOX** para reducir el costo computacional de hacer las operaciones manualmente.
 
***

# 4. Aritmética en GF(2⁸)

AES trabaja con operaciones en un **campo finito binario**:

* Suma → XOR
* Multiplicación → con reducción modular

Se usa especialmente en:

* MixColumns
* InvMixColumns
***

# 5. Número de rondas

Dependiendo de la clave:

| Tamaño de clave | Rondas |
| --------------- | ------ |
| 128 bits        | 10     |
| 192 bits        | 12     |
| 256 bits        | 14     |

***

# 6. Propiedades importantes de AES

* ✔ Seguro contra criptoanálisis lineal y diferencial
* ✔ Alta eficiencia en software y hardware
* ✔ Uso extensivo en aplicaciones reales

***

# Resumen del flujo

```text
Texto plano → Estado inicial

1. AddRoundKey

Rondas:
    SubBytes
    ShiftRows
    MixColumns
    AddRoundKey

Última ronda:
    SubBytes
    ShiftRows
    AddRoundKey

→ Texto cifrado
```

***

# Conclusión

AES combina:

* Transformaciones no lineales
* Permutaciones
* Operaciones en campos finitos


## Etapas
Etapas básicas del AES:
1. Key expansion: su utiliza para generar una subllave para cada ronda a partir de la llave original.

2. Sub Bytes (substitute bytes): utiliza una matriz S-box para realizar una substitución byte a byte del bloque del estado.

3. Shift Rows: realiza una permutación simple de bytes

4. Mix Columns: substitución que usa aritmética de campos finitos sobre GF(28).

5. Add round key: mezcla la llave expandida con el bloque de estado.

## Tablas
Se hace uso de tablas en lugar de la implementación de la aritmética de campos finitos.


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

