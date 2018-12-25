# Documentacion del Hito 4

En este hito se automatiza la creacion de la maquina virtual usando la herramienta de Azure CLI.


## Imagen

En azure la busqueda de la imagen se puede hacer por medio de [Azuremarketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/jetware-srl.postgresql?tab=PlansAndPrice)
esta es la unica imagen gratuita con PostgresSQL  y Ubuntu por eso es la que vamos a usar.

![alt text](./imagenes/hito4-1.png)

```
{
    "offer": "postgresql",
    "publisher": "jetware-srl",
    "sku": "postgresql96-ubuntu-1604",
    "urn": "jetware-srl:postgresql:postgresql96-ubuntu-1604:1.0.170503",
    "version": "1.0.170503"
  }

```
![alt text](./imagenes/hito4-5.png)
Dependiendo la region en nuestro caso West Europe el precio de la maquina puede variar, el proyecto funciona perfectamente con mas de 512 MB de ram por lo que se selecciona la mas economica
![alt text](./imagenes/hito4-2.png)

Resutado de ejecutar acopio.sh
![alt text](./imagenes/hito4-3.png)

```
1-az login
2-az vm image accept-terms
3-az group create
4-az vm create
5-az vm open-port

```

- 1- Se usa para autenticarce en azure
- 2- Se usa para aceptar terminos y condiciones de la imagen
- 3- Crear un grupo en azure
- 4- Crear la maquina virtual
- 5- Abrir los puertos de la maquina  
 
Resultado de ejecutar el playbook con ansible
![alt text](./imagenes/hito4-4.png)

