![img](https://raw.githubusercontent.com/jabonillab/ProyectoCC2018/master/imagenes/logo.png)

---

[![License](https://img.shields.io/aur/license/yaourt.svg?style=plastic)](https://github.com/jabonillab/ProyectoCC2018/master/LICENSE)
[![Status](https://img.shields.io/badge/Status-Documenting-yellow.svg)](https://github.com/jabonillab/ProyectoCC2018/master/README.md)
[![Language](https://img.shields.io/badge/language-Python-green.svg)](https://www.python.org/)
[![Language](https://img.shields.io/badge/Microframework-Flask-brown.svg)](http://flask.pocoo.org/)

### Descripción

El estilo de vida de la sociedad de hoy en día va muy deprisa, si además de esto, tenemos en cuenta que uno de los propósitos de las nuevas tecnologías es optimizar el tiempo de las personas, surge como proyecto el diseño de una aplicación que permita encontrar productos necesarios para el día a día de cualquier persona, como por ejemplo estudiantes o turistas. Es por eso que el objetivo de este proyecto es diseñar un sistema que permita a los usuarios buscar productos cercanos a ellos, garantizando la disponibilidad de los mismos. 

Para llevar a cabo el sistema se requiere de la participación de los establecimientos comerciales, dando una mayor relevancia a los comercios pequeños. Para incentivar la participación de los establecimientos se les ofrecerá la funcionalidad de manejo del inventario, al igual que publicidad para su marca, siendo por tanto un proyecto beneficioso para las partes. El usuario va tener la posibilidad de consultar en tiempo real el lugar donde puede adquirir productos específicos evitando perder tiempo con búsquedas convencionales.

### Arquitectura

Con el objetivo de minimizar costos de computo y permitir que la aplicación en versiones futuras crezca fácilmente agregando microservicios se opta por usar la arquitectura basada en **[microservicios](https://microservices.io/)**. Compuesta por los siguientes microservicios:
- Registro de usuarios
- Login
- Almacenamiento de productos geolocalizados usando **[Postgresql](https://www.postgresql.org/)**
- Buscador de productos basado en geolocalización y preferencias del usuario 
- Administración de Inventario


Los microservicios se comunicaran por medio del Broker **[rabbitmq](https://www.rabbitmq.com/)** usando **[REST](https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional)**, para hacer el desarrollo se usará **[python](https://www.python.org/)** y el framework **[flask](http://flask.pocoo.org/)** 

### Despliegue

Despliegue: https://jabonillabproyectocc2018.herokuapp.com/

El Microservicio maneja su propia base de datos **[Postgresql](https://www.postgresql.org/)** se usa el ORM **[Sqlalchemy](https://www.sqlalchemy.org/)** para el manejo de los objetos en la base de datos.

El despliegue  se en heroku de forma automática, luego de pasar los test en travis los cuales usan una base de datos diferente a la de producción.  

---
Es la primer version de la descripción en el transcurso del desarrollo podrá ser modificada.
