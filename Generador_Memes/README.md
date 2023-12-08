<div align="center">
<h1>💻 Página Generadora de Memes   💻</h1>
<h2>Este proyecto es una página web que es capaz de generar memes mediante peticiones que se le haga, posee una base de datos que guarda la elección de las personas y genera el meme de acuerdo a la elección de template de la persona.</h2>
</div>

<!--START_SECTION:activity-->
:zap:DESCARGAR EL REPOSITORIO COMPLETO Y SUS CARPETAS 
1. Tener instalado flask ```(pip install flask o si se usa entorno virtual pipenv install flask)```
2. Ejecutar el archivo main.py    
3. Este proyecto cuenta con un archivo Pipfile (entorno virtual) para instalarlo se puede usar el comando pipenv shell [GUIA DE ENTORNOS VIRTUALES](https://jarroba.com/pipenv-gestor-de-entornos-virtuales-de-python/) 
4. Si se tiene una archivo de requirements.txt. Donde se especifican los paquetes y para instalar ```(pivenv install -r requirements.txt)```
5. Como tiene bases de datos, recuerda crear la base de datos local (Puede que no te funciona la que trae el proyecto) para esto, hay que escribir en la terminal:
     - python
     - from main import app, db
     - app.app_context().push()
     - db.create_all()
     - exit()
6. 🎉 Disfruta el proyecto! 🎉
<!--END_SECTION:activity-->


