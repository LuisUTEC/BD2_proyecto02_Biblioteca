# BD2_proyecto02_Biblioteca

Integrantes:
- Ascuña Coa, Vìctor
- Cordero Pinela, Luis
- Mejia Ramon, Marlon

## Introducción

El objetivo de este proyecto es poner en practica los conceptos de recuperacion de textos, indices y scoring, aplicándolos sobre grandes cantidades de data real. Para ello empleamos la API de Twitter.

## Frontend

Para el frontend se trabajo una visualización web con backend controlado por python. Las funciones son llamadas con ajax. La visualización usa una plantilla de boostrap para tener una visualización más agradable. La pagina es sencilla hay un buscador y en el escribes el texto que quieres encontrar le das GO! y te realizara la busqueda del tweet con mayor score según el tf-idf. Esto se logra con una conexión por medio de javascrip y ajax que permite realizar un GET al servidor de python y obtener el resultado.

## Backend

### Pre-procesado
Se emplearon los filtros y procesos de tokenization, filtros y stemming. Al adquirir el texto de un tweet, se separan cada una de las palabras y signos de puntuación, estos tokens se guardan en una lista a la cual la pasaremos por un filtro para remover palabras irrelevantes y los signos de puntuación. Por último se recorta cada palabra a su raiz de acuerdo al idioma español.  

### Construcción del Índice


### Consulta
A partir del indice invertido guardado en memoria secundaria la consulta utiliza los valores para calcular los score de cada tweet. Esto se luego se divide por cada length, distancia o cantidad de palabras en el tweet el caul se guardo en la fase de construcción del indice debido a su uso practico en un futuro. Finalmente retornar los 5 tweets con mayor score.
