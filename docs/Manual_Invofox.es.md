# Invofox
  
Módulo para conectarse a Invofox y automatizar facturas  

*Read this in other languages: [English](Manual_Invofox.md), [Español](Manual_Invofox.es.md), [Português](Manual_Invofox.pr.md).*
  
![banner](imgs/Banner_Invofox.jpg)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Configurar credenciales Invofox
  
Configura credenciales para conectar con el API de Invofox.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Sesión a utilizar|Invofox1|
|API Key|API Key de Invofox|$2b$10$3/6YJ2kYHE0rtUrks8PO7.IPDdgrNsGGTCpDLY6s8pTNzcjiQFFFe|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Obtener compañías
  
Obtiene una lista de las compañías y sus datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Sesión a utilizar|Invofox1|
|Saltar|Cantidad de documentos a saltar|0|
|Límite de compañías|Cantidad máxima de compañías a obtener|10|
|Asignar resultado a variable|Asignar resultado de la consulta a una variable|result|

### Subir documentos
  
Sube uno o varios documentos a la plataforma de Invofox. Utilizar uno de los dos métodos de subida: Archivo O Carpeta.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Sesión a utilizar|Invofox1|
|Archivo|Ruta del archivo a subir|C:/Users/usuario/Desktop/Archivo.pdf|
|Archivos|Ruta de la carpeta que contiene los archivos a subir|C:/Users/usuario/Desktop/Archivos|
|Tipo de documento|Tipo de documento a subir|invoice|
|ID Compañía|ID de la Compañía a la que se asociará el documento|54aadbb7e79e2aba5d25f3e3|
|ID Lote de carga|ID del lote de carga al que se asociará el documento|2|
|Cerrar lote|Marca esta casilla si quieres cerrar el lote de carga luego de subir los archivos.|True|
|Datos adicionales|Datos adicionales que se adjuntarán a los archivos. Debe ser un array de objetos con el nombre del archivo al que se adjuntará el dato y el dato en sí.|[ { _filename: \<name of the file to which attach this data>, \<key>: \<value> }, ... { _filename: \<name of the file to which attach this data>, \<key>: \<value> } ]|
|Asignar resultado a variable|Asignar resultado de la subida de archivos a una variable.|result|

### Obtener documentos
  
Obtiene una lista con los ID de los documentos de una sesión de Invofox.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Sesión a utilizar|Invofox1|
|Saltar|Cantidad de documentos a saltar|0|
|Límite de documentos|Cantidad máxima de documentos a obtener|50|
|Tipo de documento|Tipo de documento a obtener|invoice|
|Estado público|Estado público de los documentos a obtener|processing|
|ID Compañía|ID de la Compañía de la que se obtendrán los documentos|54aadbb7e79e2aba5d25f3e3|
|Asignar resultado a variable|Asignar resultado de la ejecución a una variable|result|

### Leer documento por ID
  
Obtiene información de un documento pasándole su ID.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Sesión a utilizar|Invofox1|
|ID Documento|ID del documento a obtener|52543ec6d13ac7000bb90823|
|Valores a obtener|Valores a obtener del documento|_id,account,environment,company,creator,clientData|
|Asignar resultado a variable|Asignar resultado de la consulta a una variable|result|

### Crear compañía
  
Crear una compañía en Invofox.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Sesión a utilizar|Invofox1|
|Nombre|Nombre de la compañía|Rocketbot|
|Tax ID|Tax ID de la compañía|12345|
|Código de país|Código de país de la compañía|ES|
|Asignar resultado a variable|Asignar resultado de la consulta a una variable|result|
