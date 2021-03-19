# ProyectoFinalAnalisis-
El presente proyecto trata sobre la recopilación de datos de distintias fuentes como redes sociales, páginas de internet y datasets, siguiendo los procesos de extracción de la información, limpieza, procesamiento y visualización. A continuación, se presentan las temáticas estudiadas:

1.     Pulso político en 20 ciudades principales de Ecuador.
2.     Pulso político por provincias en Ecuador.
3.     Juegos en línea por países.
4.     Tema definido por el estudiante.
5.     Eventos o noticias mundiales.


**CASO 1: Pulso político en 20 ciudades principales de Ecuador**
Para el análisis se toma información referente al candidato Guillermo Lasso, extrayendo datos de sus redes sociales de Twitter y Facebook. En el caso de Twitter, se recopila información respecto a las menciones de la palabra 'Lasso' en una muestra de 2094 tweets recolectados, considerando así su impacto en redes. Para la extracción de datos se utiliza la librería _tweepy_, perteneciente a la API oficial de la red social. Específicamente, se utilizaron los métodos _Stream_ y _OAuthHandler_ para la verificación de las credenciales de acceso, y la el método StreamListener para recopilar todos los tweets. A continuación, se envía toda la información recopilada hacia una base local de CouchDB, a través de la librería couch para las conexiones locales. Luego, se realiza un proceso de limpieza del parámetro 'user:location' en los documentos extraídos, para modelarlos respecto al requierimiento del estudio (las provincias), actualizando los datos por defecto para que las ubicaciones sean concisas. Finalmente, se procesa toda la información a través de la herramieta Logstash, para la indexación de los datos con ElasticSearch Cloud y así realizar la visualización de la información con Kivana.

En el caso de Facebook, se extrae información sobre el número de likes, comparticiones, comentarios y la fecha que tiene las más recientes 398 publicaciones de su página. Para llevar a cabo este proceso, se utiliza la librería _facebook_scrapper_, y específicamente su método _get_posts_, que permite el acceso a todos los post y su información, de la cuenta de usuario o perfil especificado. A continuación, almacenó la información en la base de datos CouchDB local, Finalmente, se procesa la información a través de Logstash para indexarla en la ElasticSearch Cloud, para así realizar las visualizaciones en Kivana.

**CASO 2: Pulso político por provincias en Ecuador**
En este caso de estudio se analizó el pefil del candidato Andrés Arauz, extrayendo datos de sus redes sociales de Twitter y Facebook. En Twitter, se recopila información respecto a las menciones de la palabra 'Arauz' en una muestra de 5998 tweets recolectados, considerando así su impacto en redes. El proceso de extracción de información, procesamiento y visualización es similar la descrito en el Caso 1. De la misma forma, para la recopilación de datos de la red social del candidato en Facebook, se tomó una muestra de 398 publicaciones desde la más reciente. Los procesos de extracción, procesamiento y visualización de información son similares a los descritos en el Caso 1.
____________________________________________________________________________________________________________________________________________________________________________

En el punto 5 (Eventos o noticias mundiales) se hizo la extraccion de datos de youtube, instagram y tik-tok scraper, utilizando otoparce, seobots.io y tik-tok scraper, 
para poder realizar la limpieza de los datos extraidos utilizamos la herramienta rapidminer, una vez obtenida nuestros archivos limpios procedemos a guardar los datos 
en nuestras bases mysql, posterior a ello procedemos a pasar nuestros datos desde nuestras bases Mysql a elasticsearch, para esto debiamos tener previamente instalado 
cerebro, logstash, elasticsearch y kibana en nuestra PC, en este caso nosotras por motivo de recursos de nuestra PC utilizamos elasticsearch clud y kibana en la nube, 
para poer establecer conexion con elasticsearch debemos tener nuestro Mysql connector jdbc y nuestro archivo de configuracion, ya una vez enviado los datos de Mysql a 
elasticsearch procedemos a realizar nuestras visualizaciones en kibana.   
 
