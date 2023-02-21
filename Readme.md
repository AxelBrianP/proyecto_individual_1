# Descripicon de los dintintos archivos y carpetas

## Datos:
En esta capeta se alojan los datos que usaremos para nuestro proyecto.

        - Informacion sobre peliculas de Amazon Prime, Disney Plus, Hulu y Netflix. 
            En total tenemos un total de 29 mil peliuclas.
        - Datos sobre usuarios, y calificaciones que hicieron sobre distintas películas. 
            En total tenemos 11 millones de calificaciones

## Extraccion_transformacion_datos.ipynb
En este archivo leemos los datos, los ordenamos y los transformamos para tener un mejor     entendimiento y para poder procesarlos. Nuestros daots al finalizar son los siguientes:

        - Peliculas_Ratings: donde unimos las peliculas de las 4 plataformas, con su respectivo promedio de calificaciones.
        - Usuarios_Ratings: donde unimos los usuarios con la calificacion que dieron a "X" pelicula.

## Analisis_exploratorio_datos.ipynb
En este archivo hacemos un analizis sobre nuestros datos para entender mejor sobre que estamos trabajando, intentaremos buscar relaciones entre los ellos. También buscaremos outliers, es decir, datos que estan por fuera de lo normal.

        Encontrarás:
            - Graficos acerca de visitas por peliculas y plataformas
            - Graficos acerca sobre el promedio de las calificaciones
            - Graficos acerca de valoraciones por plataforma
            - Graficos acerca de valoraciones por genero
            - Graficos acerca de valoraciones por genero y plataforma

## main.py
Esta es nuestra aplicaciones, capas de realizar distintas operaciones sobre las películas.

No necesita ejecutar la aplicacion desde su ordenador, puede ingresar a mi app en la nube, solo necesita tener una cuenta en Deta Cloud, y descargar la aplicacion [con el siguiente enlace](https://deta.space/discovery/r/k2ywtcccr5jv7nrz "Api").

Las funciones que contiene son las siguientes:

- get_max_duration(año, plataforma, duracion_tipo)
            
        Esta funcion calcula la duracion maxima para una pelicula o temporada. Pide como parametros, un año en especifico, una plataforma (Amazon Prime, Disney Plus, Hulu, Netflix), y tipo de durarion (min para referirse a los minutos de las peliculas, y seasons para referirse, season no se incluye ya que siempre serían minimos por tener 1 temporada)
        
- get_rating_movie(plataforma, desde_el_año, calificacion_minima)

        Esta funcion calcula la cantidad de peliculas por plataforma que superan un determinado promedio de calificaciones, desde un determinado año en adelante. Pide como parametros la plataforma, desde que año analizar, y la calificacion minima que se desee (esta puede estar entre los valores 3.336 y 3.722), para un mejor analizis se recomienda agregar un promedio con 3 decimales

- get_count_platform(plataforma)

        Esta funcion calcula la cantidad de peliculas por plataforma, para ello basta con agregar la plataforma que se desee calcualr.

- get_actor(platform, year)

        Esta funcion define que actor participo en más peliculas para una determinada plataforma, durante un año en especifico. Los parametros de la funcion son la plataforma y durante que año.

## Sistema_recomendaciones_ML.ipybn
En este archivo se aloja una aplicación capas de recomendar peliculas o series a los usuarios, analizando su historial para que las recomendaciones sean de interés.
Al final del archivo se encuentra la siguiente funcion:
- recomendacion_peliculas(usuario)
        
        Solo deberá ingresar el id de un usuario, y la funcion imprimirá las peliculas recomendadas, con una calificacion esperada por el usuario para dicha pelicula.
        Ejemplo--> recomendacion_peliculas(1450) --> 1450 = ID de usuario