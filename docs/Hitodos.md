# Documentación del Hito 2


### Definición de la Infraestructura

Tanto Heroku y Travis usan documentos de configuración para generar la infraestructura necesaria a continuación se describen los documentos principales

Siguientes archivos:

- [requirements.txt](https://github.com/jabonillab/ProyectoCC2018/blob/master/requirements.txt): En heroku se facilita usar Gunicorn, que es un servidor WSGI HTTP para Python y nos permite correr el servidor. 
- [database.yml](https://github.com/jabonillab/ProyectoCC2018/blob/master/database.yml): Para poder ejecutar las pruebas es necesario crear una base de datos temporal en travis en este documento especifico las credenciales de la base de datos temporal que se creara al momento de comenzar las prubas y se destruira al terminarlas
- [Procfile](https://github.com/jabonillab/ProyectoCC2018/blob/master/Procfile): En este documento de especifica a Heroku el tipo de servidor y la aplicacion que debe desplegar, se usa gunicorn ya que permite administrar las peticiones simultaneas que la aplicación reciba.

### Test con Travis

Se vincula la cuenta de Github con Travis como se ve en la siguiente imagen

![img](https://raw.githubusercontent.com/jabonillab/ProyectoCC2018/master/docs/imagenes/travis.png)

Cada vez que actualizamos el repositorio a partir de este momento debería de aparecer en la página web de Travis algo parecido a la siguiente imagen si todo ha salido bien.

![img](https://raw.githubusercontent.com/jabonillab/ProyectoCC2018/master/docs/imagenes/resultTravis.png)

### Vinculación con Heroku

Para vincular con Heroku se puede hacer desde la interfaz en su página web.

![img](https://raw.githubusercontent.com/jabonillab/ProyectoCC2018/master/docs/imagenes/herokuConection.png)

En github nos muestra el despliegue

![img](https://raw.githubusercontent.com/jabonillab/ProyectoCC2018/master/docs/imagenes/autodeploy.png)
