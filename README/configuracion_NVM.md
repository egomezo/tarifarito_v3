-- COMANDOS PARA INSTALAR NVM (NODE VERSION MANAGER) LINUX

https://www.youtube.com/watch?v=M_asn_Vr3Xs

1. Comando para descargar el instalador de NVM (Verificar siempre en la pagina oficial)
--> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

2. Comando para actualizar la instalación de NVM en la terminal
--> source ~/.bashrc

3. Comando para validar la instalación de NVM y apareceran todos sus comandos
--> nvm

4. Comando para conocer la versión de NVM
--> nvm --version

5. Comando para instalar la ultima version de Node
--> nvm install node

6. Comando para listar las versiones de node instaladas con nvm
--> nvm list

7. Comando para listar las versiones disponibles de node
--> nvm ls-remote

8. Comando para instalar una versión especifica de node con nvm (nvm install [node_version])
--> nvm install v14.18.2

9. Comando para cambiar entre versiones de node con nvm (nvm use [node_version])
--> nvm use v14.18.2

Nota. Para instanciar las librerias (node_modules) no utilizar el comando sudo