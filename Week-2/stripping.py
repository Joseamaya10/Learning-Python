fh = open("C:/Users/57300/OneDrive/Documentos/GitHub/Learning-Python/Week-2/mbox-short.txt")
print(fh)
for line in fh:
    line_1 = line.strip()
    print(line_1)
        
# Para abrir el archivo es necesario colocar la ruta completa del archivo o tener el archivo en la misma carpeta donde se encuentra el script de python.        
# La ruta se ve así "C:\Users\57300\OneDrive\Documentos\GitHub\Learning-Python\Week-2\mbox-short.txt"
# Así que se debe cambiar las \ por / o colocar \\ para que no de error.