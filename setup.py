from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Paquete de notificaciones kemok'
LONG_DESCRIPTION = 'Paquete de canales de notificaciones de kemok'

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="notificaction-service", 
        version=VERSION,
        author="Carlos Pacheco",
        author_email="<carlos.pacheco@kemok.io>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        url='https://github.com/Kemok-Repos/notification-service'
)