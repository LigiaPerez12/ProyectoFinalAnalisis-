# ProyectoFinalAnalisis-
El presente proyecto trata sobre la recopilación de datos de distintias fuentes como redes sociales, páginas de internet y datasets, siguiendo los procesos de extracción de la información, limpieza, procesamiento y visualización. A continuación, se presentan las temáticas estudiadas:

1.     Pulso político en 20 ciudades principales de Ecuador.
2.     Pulso político por provincias en Ecuador.
3.     Juegos en línea por países.
4.     Tema definido por el estudiante.
5.     Eventos o noticias mundiales.


CASO 1:
 Para el análisis, se consideró

En el punto 5 (Eventos o noticias mundiales) se hizo la extraccion de datos de youtube, instagram y tik-tok scraper, utilizando otoparce, seobots.io y tik-tok scraper, 
para poder realizar la limpieza de los datos extraidos utilizamos la herramienta rapidminer, una vez obtenida nuestros archivos limpios procedemos a guardar los datos 
en nuestras bases mysql, posterior a ello procedemos a pasar nuestros datos desde nuestras bases Mysql a elasticsearch, para esto debiamos tener previamente instalado 
cerebro, logstash, elasticsearch y kibana en nuestra PC, en este caso nosotras por motivo de recursos de nuestra PC utilizamos elasticsearch clud y kibana en la nube, 
para poer establecer conexion con elasticsearch debemos tener nuestro Mysql connector jdbc y nuestro archivo de configuracion, ya una vez enviado los datos de Mysql a 
elasticsearch procedemos a realizar nuestras visualizaciones en kibana.   
 
