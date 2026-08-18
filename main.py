
import os 
import shutil 

carpetas = {"Ejecutables": [".exe"],
            "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
            "Documentos": [".docx", ".doc", ".pdf", ".txt", ".xlsx", ".xls", ".pptx", ".ppt"],
            "Archivos comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Multimedia - Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
            "Multimedia - Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
            "Desarrollo / Código": [".py", ".js", ".html", ".css", ".json", ".sql"],
            "Instaladores / Imágenes de Disco": [".msi", ".dmg", ".iso", ".pkg"],
            "Diseño / Gráficos Avanzados": [".psd", ".ai"]}

ruta_carpeta = input("Introduce la ruta de la carpeta que deseas organizar: ")

for elemento in os.listdir(ruta_carpeta):  
    ruta_completa = os.path.join(ruta_carpeta, elemento) 
    if os.path.isfile(ruta_completa): # El filtro de seguridad para comprobar si es un archivo o una carpeta
        print(f"Archivo detectado: {elemento}")
        nombre, extension = os.path.splitext(elemento) 
        extension = extension.lower()
        destino = "Otros" # Asignando un destino por defecto
        for nombre_categoria, lista_extensiones in carpetas.items():
            if extension in lista_extensiones:
                destino = nombre_categoria
                break
        ruta_exacta = os.path.join(ruta_carpeta, destino)  
        if not os.path.isdir(ruta_exacta):
            os.mkdir(ruta_exacta) 
        ruta_final = os.path.join(ruta_exacta, elemento)     
        archivo_mudanza = shutil.move(ruta_completa, ruta_final) 
   
   
            
    

