from datetime import *

contenido = ['alex', 0, '13/05/2022 0:00']

for i in range(len(contenido)):
    pos = contenido.index(format="00/00/0000 0:00")
    """
    print(type(contenido[i]))
    if(contenido[i] != datetime.strptime(contenido[i], "%d/%m/%Y 0:00").strftime('%d/%m/%Y 0:00')):
        print("Es una fecha")
    else:
        print("Esto no es una fecha")
    """