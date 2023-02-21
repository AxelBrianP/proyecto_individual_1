from fastapi import FastAPI
import pandas as pd

app = FastAPI(title = 'Ratings',
              description = 'Abarcamos peliculas, series, y programas de TV de las siguientes plataformas: Amazon Prime, Disney Plus, Hulu y Netflix',
              version = '1.0.1')

@app.get("/")
async def index():
    return {'Bienvenido a tu aplicación para operar con peliculas de diferentes plataformas'}

peliculas_ratings = pd.read_csv('..\PI_1\Datos\Peliculas_Ratings.csv')

@app.get("/duración_maxima")
async def get_max_duration(año: int, plataforma: str, duracion_tipo: str):
    
    #Aplicamos una condicion para que el año ingresado sea correcto
    if (año < 1920) or (año > 2021):
        return {'El año ingresado solo puede ser un valor entre 1920-2021'}
    
    #Aplicamos una condicion para que el tipo de duracion sea correcto
    if duracion_tipo not in ['min', 'seasons']:
        return {'los datos en duracion_tipo pueden ser los siguientes: 1) min: expresa minutos. 2) seasons: se refiere a mas de una temporada.'}
    
    #Aplicamos una condicion para que la plataforma sea correcta
    if plataforma not in ['amazon prime','disney plus','netflix','hulu']:
        return {'los nombres de plataformas permitidos para esta funcion son las siguientes: 1) amazon prime. 2) disney plus. 3) netflix. 4) hulu no funcionará si solo escribe amazon, o disney. Deberá ser el nombre completo'}
    
    #Creamos una variable donde almacenaremos la inical de la plataforma para facilitar la busqueda del dato
    id_plataforma = 'txt'

    #aplicamos condiciones para obtener el dato de la variable recien creada
    if plataforma == 'amazon prime':
        id_plataforma = 'a'
    elif plataforma == 'disney plus':
        id_plataforma = 'd'
    elif plataforma == 'netflix':
        id_plataforma = 'n'
    else:
        plataforma == 'hulu'
        id_plataforma = 'h'
    
    #En x almacenamos los titulos que cumplen las condiciones seleccionadas en la funcion
    x = pd.DataFrame(peliculas_ratings['title'][peliculas_ratings['release_year'] == año][peliculas_ratings['plataforma'] == (id_plataforma)][peliculas_ratings['duration_type'] == (duracion_tipo)])
    #En y almacenamos la duracion de la pelicula/serie/programa
    y = pd.DataFrame(peliculas_ratings['duration_int'][peliculas_ratings['release_year'] == año][peliculas_ratings['plataforma'] == (id_plataforma)][peliculas_ratings['duration_type'] == (duracion_tipo)])
    #En z unimos los datos para sacar el resultado mas facil
    z = pd.merge(x, y, how = 'outer', left_index= True, right_index=True)
    #Verificamos que los datos no esten vacios, si lo estan es porque no existe elemento que cumpla con las condiciones
    if (z.empty) == True:
        return {"Ningun elemento cumple con las condiciones de busqueda"}
    #max será un filtro que almacenará el valor de la duracion maxima en minutos/temporadas
    max = z['duration_int'].max()
    #aplicamos el filtro tener solo la fila que contiene la pelicula con maxima duracion en z
    z = z.loc[z['duration_int'] == max]
    #reseteamos el indice para facilitar la extraxión del dato
    z.reset_index(inplace=True)
    #extraemos el nombre de la pelicula
    z = z['title'][0]
    #resultado contendra el nombre de la pelicula
    resultado = z
    #eliminamos los dataframe creados para ahorrar memoria
    del(x,y,z)
    #imprimimos el resultado en pantalla
    return {"Pelicula/programa con mayor duracion.", resultado}

@app.get("/calificacion_peliculas_por_plataforma")
async def get_rating_movie(plataforma: str, desde_el_año: int, calificacion_minima: float):
        
    #Aplicamos una condicion para que la plataforma sea correcta
    if plataforma not in ['amazon prime','disney plus','netflix','hulu']:
        return {'los nombres de plataformas permitidos para esta funcion son las siguientes: 1) amazon prime. 2) disney plus. 3) netflix. 4) hulu no funcionará si solo escribe amazon, o disney. Deberá ser el nombre completo'}
    
    #Aplicamos una condicion para que el año ingresado sea correcto
    if (desde_el_año < 1920) or (desde_el_año > 2021):
        return {'El año ingresado solo puede ser un valor entre 1920-2021'}

    #Aplicamos una condicion para que la calificacion sea valida
    if (calificacion_minima < 3.336 ) or (calificacion_minima > 3.722):
        return {'Para una mejor busqueda trabajaremos con 3 decimales. Se aceptan valores entre 3.336 y 3.722'}
    
    #Creamos una variable donde almacenaremos la inical de la plataforma para facilitar la busqueda del dato
    id_plataforma = 'txt'
    #aplicamos condiciones para obtener el dato de la variable recien creada
    if plataforma == 'amazon prime':
        id_plataforma = 'a'
    elif plataforma == 'disney plus':
        id_plataforma = 'd'
    elif plataforma == 'netflix':
        id_plataforma = 'n'
    else:
        plataforma == 'hulu'
        id_plataforma = 'h'

    #filtramos las filas en base a los datos seleccionados en la funcion
    x = pd.DataFrame(peliculas_ratings['id'][peliculas_ratings['plataforma'] == id_plataforma][peliculas_ratings['release_year'] > desde_el_año][peliculas_ratings['score'] > calificacion_minima])
    #contamos las filas de los datos obtenidos
    resultado = x['id'].count()
    #eliminamos x para ahorrar espacio
    return {'elementos coinciden con la busqueda', int(resultado)}

@app.get("/cantidad_peliculas_por_ptalaforma")
async def get_count_platform(plataforma: str):
    
    if plataforma not in ['amazon prime','disney plus','netflix','hulu']:
        return {'los nombres de plataformas permitidos para esta funcion son las siguientes: 1) amazon prime. 2) disney plus. 3) netflix. 4) hulu no funcionará si solo escribe amazon, o disney. Deberá ser el nombre completo'}
    
    #Creamos una variable donde almacenaremos la inical de la plataforma para facilitar la busqueda del dato
    id_plataforma = 'txt'
    #aplicamos condiciones para obtener el dato de la variable recien creada
    if plataforma == 'amazon prime':
        id_plataforma = 'a'
    elif plataforma == 'disney plus':
        id_plataforma = 'd'
    elif plataforma == 'netflix':
        id_plataforma = 'n'
    else:
        plataforma == 'hulu'
        id_plataforma = 'h'
    
    x = (peliculas_ratings['id'][peliculas_ratings['plataforma'] == id_plataforma])
    resultado = x.count()
    return {"Peliculas/series contiene la plataforma", int(resultado)}

@app.get("/actor_mas_repetido")
async def get_actor(platform: str, year: int):
    
    #Aplicamos una condicion para que la plataforma sea correcta
    if platform not in ['amazon prime','disney plus','netflix','hulu']:
        return {'los nombres de plataformas permitidos para esta funcion son las siguientes: 1) amazon prime. 2) disney plus. 3) netflix. 4) hulu no funcionará si solo escribe amazon, o disney. Deberá ser el nombre completo'}
    
    #Aplicamos una condicion para que el año ingresado sea correcto
    if (year < 1920) or (year > 2021):
        return {'El año ingresado solo puede ser un valor entre 1920-2021'}
    
    #Creamos una variable donde almacenaremos la inical de la plataforma para facilitar la busqueda del dato
    id_plataforma = 'txt'
    #aplicamos condiciones para obtener el dato de la variable recien creada
    if platform == 'amazon prime':
        id_plataforma = 'a'
    elif platform == 'disney plus':
        id_plataforma = 'd'
    elif platform == 'netflix':
        id_plataforma = 'n'
    else:
        platform == 'hulu'
        id_plataforma = 'h'

    #Filtramos los datos de acuerdo a los parametros pasados en la funcion, solo nos quedaremos con los nombres de los actores
    x = pd.DataFrame(peliculas_ratings['cast'][peliculas_ratings['plataforma'] == id_plataforma][peliculas_ratings['release_year'] == year])
    #eliminamos filas donde no figuren los actores
    x.dropna(inplace = True)
    #reseteamos el indice para facilitar las operaciones
    x.reset_index(inplace = True)
    #eliminamos la columna con los indices originales
    x.drop(['index'], axis = 1, inplace = True)
    #contamos la cantidad de actores, necesitaremos el valor para nuestro bucle while
    contador = int(x['cast'].count())
    #creamos una lista vacia donde agregaremos a todos los actores, aunque esten repetidos
    actores = []
    #con while recorreremos todos los indices para extraer los actores
    while (contador > 0):
        #cast accedera a la columna cast de cada registro
        cast = (x['cast'][(contador - 1)])
        #separaremos los diferentes actores obteniendo un string
        separados = cast.split(sep = ',')
        #agregamos todos loas actores a la lista antes creada, aunque esten repetidos
        actores = actores + separados
        #restamos 1 al contador para acceder a un registro anterior
        contador -= 1
    #En esta lista iran los actores con una modificacion, quitaremos los espacios de mas
    actors = []
    #con for iteramos sobre todos los actores
    for i in actores:
        #con strip quitamos los espacios en blanco al inicio del string
        actors.append(i.strip(' '))
    #convertimos la lista en una serie
    actors = pd.Series(actors)
    #contamos los valores repetidos para cada actor
    mm = actors.value_counts()
    #reseteamos el indice para que se transforme en un DataFrame
    jj = mm.reset_index()
    #cambiamos nombres de columnas para facilitar operaciones
    jj.rename(columns={0:'cantidad'}, inplace=True)
    #revisamos la cantidad de veces que aparece el nombre mas repetido
    xx = int(jj['cantidad'][0])
    #si el nombre mas repetido es igual a 1, significa que todos los actores figuraron una sola vez
    if xx == 1:
        return {"Todos los actores tiene 1 sola participacion"}
    return {"El actor mas repetido durante el año", mm.index[0]}