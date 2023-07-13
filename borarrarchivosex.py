import os
import shutil

folder = r'C:\Users\kevin\Desktop\PRUEBAS - copia'  # Reemplaza con la ruta de la carpeta que deseas vaciar
preserve = [r'C:\Users\kevin\Desktop\PRUEBAS - copia\pipip.xlsx', r'C:\Users\kevin\Desktop\PRUEBAS - copia\uno.docx', r'C:\Users\kevin\Desktop\PRUEBAS - copia\uryvas.pub']  # Reemplaza con las rutas de los archivos o directorios que deseas preservar

for root, dirs, files in os.walk(folder, topdown=False): 
    for file in files:
        file_path = os.path.join(root, file)
        if file_path not in preserve:
            try:
                os.remove(file_path)
                print(f"Eliminando archivo: {file_path}")
            except Exception as e:
                print(f"No se pudo eliminar el archivo: {file_path} - Error: {str(e)}")
    
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if dir_path not in preserve:
            try:
                shutil.rmtree(dir_path)
                print(f"Eliminando directorio: {dir_path}")
            except Exception as e:
                print(f"No se pudo eliminar el directorio: {dir_path} - Error: {str(e)}")
