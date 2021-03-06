![img](https://raw.githubusercontent.com/jabonillab/ProyectoCC2018/master/docs/imagenes/logo.png)

---

[![License](https://img.shields.io/aur/license/yaourt.svg?style=plastic)](https://github.com/jabonillab/ProyectoCC2018/master/LICENSE)
[![Status](https://img.shields.io/badge/Status-Documenting-yellow.svg)](https://github.com/jabonillab/ProyectoCC2018/master/README.md)
[![Language](https://img.shields.io/badge/language-Python-green.svg)](https://www.python.org/)
[![Language](https://img.shields.io/badge/Microframework-Flask-brown.svg)](http://flask.pocoo.org/)
#### Autor: Jorge Bonilla
#### Máster en Ingeniería Informática
#### Enlace de la documentación: https://jabonillab.github.io/ProyectoCC2018/

### Descripción

El estilo de vida de la sociedad de hoy en día va muy deprisa, si además de esto, tenemos en cuenta que uno de los propósitos de las nuevas tecnologías es optimizar el tiempo de las personas, surge como proyecto el diseño de una aplicación que permita encontrar productos necesarios para el día a día de cualquier persona, como por ejemplo estudiantes o turistas. Es por eso que el objetivo de este proyecto es diseñar un sistema que permita a los usuarios buscar productos cercanos a ellos, garantizando la disponibilidad de los mismos.

Para llevar a cabo el sistema se requiere de la participación de los establecimientos comerciales, dando una mayor relevancia a los comercios pequeños. Para incentivar la participación de los establecimientos se les ofrecerá la funcionalidad de manejo del inventario, al igual que publicidad para su marca, siendo por tanto un proyecto beneficioso para las partes. El usuario va tener la posibilidad de consultar en tiempo real el lugar donde puede adquirir productos específicos evitando perder tiempo con búsquedas convencionales.

### Arquitectura

Con el objetivo de minimizar costos de computo y permitir que la aplicación en versiones futuras crezca fácilmente agregando microservicios se opta por usar la arquitectura basada en **[microservicios](https://microservices.io/)**. Compuesta por los siguientes microservicios:

- Administración de productos con el almacenamiento geolocalizado usando **[Postgresql](https://www.postgresql.org/)**
- Administración de usuarios
- Gestión de Promociones

Los microservicios se comunicaran por medio del Broker **[rabbitmq](https://www.rabbitmq.com/)** usando **[REST](https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional)**, para hacer el desarrollo se usará **[python](https://www.python.org/)** y el framework **[flask](http://flask.pocoo.org/)**



## Pruebas y test

Las pruebas se hacen con [Unittest](https://docs.python.org/3/library/unittest.html) intentando cubrir la mayor cantidad de código posible, así al hacer una modificación los test serán ejecutados en [Travis](https://docs.travis-ci.com/) y notificará en caso de que se presente un problema


### Despliegue

Despliegue: https://jabonillabproyectocc2018.herokuapp.com/

El Microservicio maneja su propia base de datos **[Postgresql](https://www.postgresql.org/)** se usa el ORM **[Sqlalchemy](https://www.sqlalchemy.org/)** para el manejo de los objetos en la base de datos.

El despliegue  se en heroku de forma automática, luego de pasar los test en [Travis](https://docs.travis-ci.com/) los cuales usan una base de datos diferente a la de producción.

Recursos disponibles:

- [/](https://jabonillabproyectocc2018.herokuapp.com/) : Es la raíz en la que se muestra status:OK en caso de que este levantado el servidor.
- [/Productos](https://jabonillabproyectocc2018.herokuapp.com/productos): Hace exactamente lo mismo que la raíz, es una prueba que realice para comprobar si podía poner el mismo recurso en más de una ruta.
- [/nuevoproducto/< nombre >/< ubicacion >](): Usada para agregar productos al Inventario

### Definición de la Infraestructura

Tanto Heroku y Travis usan documentos de configuración para generar la infraestructura necesaria a continuación se describen los documentos principales

Siguientes archivos:

- [requirements.txt](https://github.com/jabonillab/ProyectoCC2018/blob/master/requirements.txt): En heroku se facilita usar Gunicorn, que es un servidor WSGI HTTP para Python y nos permite correr el servidor.
- [database.yml](https://github.com/jabonillab/ProyectoCC2018/blob/master/database.yml): Para poder ejecutar las pruebas es necesario crear una base de datos temporal en travis en este documento especifico las credenciales de la base de datos temporal que se creara al momento de comenzar las prubas y se destruira al terminarlas
- [Procfile](https://github.com/jabonillab/ProyectoCC2018/blob/master/Procfile): En este documento de especifica a Heroku el tipo de servidor y la aplicacion que debe desplegar, se usa gunicorn ya que permite administrar las peticiones simultaneas que la aplicación reciba.

continuar en [Hito 2](/docs/Hitodos.md)

## Aprovisionamiento

En el aprovisionamiento se ha usado Ansible. El servicio se ha desplegado en una máquina virtual a través de la plataforma Azure.

MV: 13.69.54.133

Toda la información sobre este hito se encuentra en

[Hito 3](/docs/Hitotres.md)


## Automatización

MV2: 13.69.21.103

Se ha creado un [script](./acopio.sh) donde se crear una MV en Azure con la imagen de la empresa [jetware](http://jetware.io) que está compuesta por Ubuntu Server 16.04 LTS y postgresql 9.6. Además se prepara la imagen para poder acceder a ella vía http y se aprovisiona con un [playbook](./provision/ansible/aprovisionamientoazure.yml) de Ansible. Documentación sobre la automatización se encuentra en el siguiente [documento](./docs/Hitocuatro.md)

## Orquestación

Se realiza la orquestación de la infraestructura usando la herramienta de orquestación Vagrant. 

Despliegue Vagrant: 13.94.202.85

Toda la información a este hito se encuentra en siguiente [documento](/docs/Hitocinco.md)


