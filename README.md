# BD2_proyecto02_Biblioteca

### Integrantes:
- Ascuña Coa, Vìctor
- Cordero Pinela, Luis
- Mejia Ramon, Marlon

## Introducción

El objetivo de este proyecto es poner en practica los conceptos de recuperacion de textos, indices y scoring, aplicándolos sobre grandes cantidades de data real. Para ello utilizaremos Twitter, una red social muy importante en la actualidad por su manejo de informaciòn sobre determinados grupos de usuarios a nivel mundial.

## Frontend

Para el frontend se trabajo una visualización web con backend controlado por python. Las funciones son llamadas con ajax. La visualización usa una plantilla de boostrap para tener una visualización más agradable. La pagina es sencilla hay un buscador y en el escribes el texto que quieres encontrar le das GO! y te realizara la busqueda del tweet con mayor score según el tf-idf. Esto se logra con una conexión por medio de javascrip y ajax que permite realizar un GET al servidor de python y obtener el resultado.

[HTML](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/templates/index.html)

[JS-AJAX](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/static/js/function.js)

## Backend

### Pre-procesado
Se emplearon los filtros y procesos de tokenization, filtros y stemming. Al adquirir el texto de un tweet, se separan cada una de las palabras y signos de puntuación, estos tokens se guardan en una lista a la cual la pasaremos por un filtro para remover palabras irrelevantes y los signos de puntuación. Por último se recorta cada palabra a su raiz de acuerdo al idioma español.  

<pre>
def setFiles(files):
    tweets = {}
    tweets_text = {}
    n = 0
    for file in files:
        print(file)
        with open("clean/"+file, errors='ignore') as file_json:
            file_clean = json.load(file_json)
        for tweet in file_clean:
            text = tweet['text']
            tweets_text[tweet['id']] = text
            file_stemmed = []
            text = text.lower()
            files_tokens = []
            tokenizer = nltk.RegexpTokenizer(r"\w+")
            files_tokens = tokenizer.tokenize(text)
            for token in files_tokens:
                if token in stoplist:
                    files_tokens.remove(token)
            for token in files_tokens:
                file_stemmed.append(stemmer.stem(token))
            tweets[tweet['id']] = file_stemmed
        n+=1
        if n == 2:
            break
    with open('text.json', 'w') as file:
        json.dump(tweets_text, file)

    return tweets
</pre>


[Codigo](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/Files.py)

### Construcción del Índice
La construcción de los indices se empieza a partir de la construcción de un arreglo que almacene todos los tweets y sus palabras, labor que hace el preprocesamiento. Posteriormente se procede a sacar la respectiva frecuencia de cada palabra por documento, se crea un nuevo JSON el cual almacenara el tf-idf, junto con su frecuencia. Esto tambien nos permite calcular las longitudes de los tweets. Esto luego pasara a ser guardado en memoria secundaria. De esta forma, cada vez que en el frontend realice una peticion este se cargara desde memoria secundaria y retornara el indice, posteriormente y segun el querie retornara en el frontend el id de los tweets y su respectivo texto.
<pre>
def tf_idf (self):
    data = {}
    docs_length = {}
    for term in self:
        for word in self[term]:
    	    if word in data.keys():
	        if term in data[word].keys():
		    data[word][term].setdefault('f', 0)
		    data[word][term]['f'] += 1
		else:
		    data[word][term] = {}
		    data[word][term].setdefault('f', 0)
		    data[word][term]['f'] += 1
	    else:
		data[word] = {}
	docs_length[term] = len(self[term])
</pre>

[Codigo](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/invertindex.py)

### Manejo de memoria Secundaria
Se tienen datos de una cantidad bastante grande de Tweets dentros de archivos JSON; para mejorar la eficiencia el manejo de la memoria secundaria esta dividido en 3 files a parte de la data que se guarda,teniendo un file donde se guarda el indice invertido, las normas y los tf_idf.
<pre>
    with open('index.json', 'w') as file:
        json.dump(data, file)
    with open('doc_length.json', 'w') as file:
	json.dump(docs_length, file)
</pre>

[Codigo](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/invertindex.py)

### Consulta
A partir del indice invertido guardado en memoria secundaria la consulta utiliza los valores para calcular los score de cada tweet. Esto se luego se divide por cada length, distancia o cantidad de palabras en el tweet el caul se guardo en la fase de construcción del indice debido a su uso practico en un futuro. Finalmente retornar los 5 tweets con mayor score.


<pre>
def query(content):
    Scores = {}
    Length = {}
    words = parsing(content)
    for t in words:
        with open('index.json') as file:
            data = json.load(file)
        if t in data:
            for doc in data[t]:
                Scores.setdefault(doc, 0)
                Scores[doc] += data[t][doc]['tf-idf']
    with open('doc_length.json') as file:
        doc_length = json.load(file)
    for length in doc_length:
        Length[length] = doc_length[length]
    for d in Scores:
        Scores[d] = Scores[d]/Length[d]
    return top(5, Scores)
</pre>

[Codigo](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/query.py)

### Servidor
Para el manejo del servidor se utilizo un servidor en python con host en **127.0.0.1** para routear la pagina web donde se haran las consultas. Dicho servidor sirve principalmente de enlace entre la función de consulto, la data de los tweets y el usuario por medio del frontend.
<pre>
if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
</pre> 
<pre>
@app.route('/search/<content>', methods = ['GET'])
def search(content):
    data = query(content)
    with open('text.json') as file:
        text = json.load(file)
    response = {}
    i = 0
    for d in data:
        response[i] = text[d]
        i += 1
    return Response(json.dumps(response), mimetype='application/json')
</pre>

[Codigo](https://github.com/LuisUTEC/BD2_proyecto02_Biblioteca/blob/master/server.py)

## Pruebas

#### Preprocesamiento y Creación de indices

| N° de tweets | Tiempo(s) |
| ----- | ---- |
| 9131 | 4,496123688 |
| 34696 | 17,27564565 |
| 46298 | 23,25669138 |
| 181347 | 90,30275361 |

![Alt text](/../master/Diagrama1.png?raw=true "Optional Title")

#### Consultas

| N° de tweets | Tiempo(s) |
| ----- | ---- |
| 9131 | 0,2504851818 |
| 34696 | 0,9956831931 |
| 46298 | 1,345535028 |
| 181347 | 5,467158874 |

![Alt text](/../master/Diagrama2.png?raw=true "Optional Title")

[VIDEO](https://youtu.be/Yh34nujZoYM)
