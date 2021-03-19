# ProyectoFinalAnalisis-
El presente proyecto trata sobre la recopilación de datos de distintias fuentes como redes sociales, páginas de internet y datasets, siguiendo los procesos de extracción de la información, limpieza, procesamiento y visualización. A continuación, se presentan las temáticas estudiadas:

1.     Pulso político en 20 ciudades principales de Ecuador.
2.     Pulso político por provincias en Ecuador.
3.     Juegos en línea por países.
4.     Tema definido por el estudiante.
5.     Eventos o noticias mundiales.


CASO 1
Para el análisis se toma información referente al candidato Guillermo Lasso, extrayendo datos de sus redes sociales de Twitter y Facebook. En el caso de Twitter, se recopila información respecto a las menciones de la palabra 'Lasso' en una muestra de 2094 tweets recolectados, considerando así su impacto en redes. Para la extracción de datos se utiliza la librería Tweepy, perteneciente a la API oficial de la red social. Específicamente, se utilizaron los métodos Stream y OAuthHandler para la verificación de las credenciales de acceso, y la el método StreamListener para recopilar todos los tweets. A continuación, se envía toda la información recopilada hacia una base local de CouchDB, a través de la librería couch para las conexiones locales. Luego, se realiza un proceso de limpieza del parámetro 'user:location' en los documentos extraídos, para modelarlos respecto al requierimiento del estudio (las provincias), actualizando los datos por defecto para que las ubicaciones sean concisas. Finalmente, se procesa toda la información a través de la herramieta Logstash, para la indexación de los datos con ElasticSearch Cloud y así realizar la visualización de la información con Kivana.

En el caso de Facebook, se extrae información sobre el número de likes, comparticiones y comentarios que tiene las más recientes 398 publicaciones de su página. Para la extracción de la inforamción

La extracción de datos se realizó uti

En el punto 5 (Eventos o noticias mundiales) se hizo la extraccion de datos de youtube, instagram y tik-tok scraper, utilizando otoparce, seobots.io y tik-tok scraper, 
para poder realizar la limpieza de los datos extraidos utilizamos la herramienta rapidminer, una vez obtenida nuestros archivos limpios procedemos a guardar los datos 
en nuestras bases mysql, posterior a ello procedemos a pasar nuestros datos desde nuestras bases Mysql a elasticsearch, para esto debiamos tener previamente instalado 
cerebro, logstash, elasticsearch y kibana en nuestra PC, en este caso nosotras por motivo de recursos de nuestra PC utilizamos elasticsearch clud y kibana en la nube, 
para poer establecer conexion con elasticsearch debemos tener nuestro Mysql connector jdbc y nuestro archivo de configuracion, ya una vez enviado los datos de Mysql a 
elasticsearch procedemos a realizar nuestras visualizaciones en kibana.   
 
