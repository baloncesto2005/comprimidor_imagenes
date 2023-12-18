import os
from PIL import Image

print("Dime la ruta en la que debo buscar las imágenes para comprimirlas")
ruta = input().strip()
files = os.listdir(ruta)

terminaciones = [".jpg", ".png", ".gif", ".jpeg"]
carpeta = "images_comprimidos"
ruta_crear = os.path.join(ruta, carpeta)

if not os.path.exists(ruta_crear):
    os.makedirs(ruta_crear)
    print(f"Se ha creado la carpeta '{carpeta}' en '{ruta}'")

print(f"\nArchivos en la ruta ({ruta}):")
print([f for f in files if os.path.splitext(f)[1] in terminaciones and os.path.isfile(os.path.join(ruta, f))])

print("\n¿Qué opción te gustaría hacer?")
print("1 ----> PARA COMPRIMIR UNA IMAGEN EN ESPECÍFICO")
print("2 ----> PARA COMPRIMIR TODAS LAS IMÁGENES DE UNA CARPETA")
print("3 ----> PARA SALIR")
opcion_jugador = input("Dime qué opción te gustaría hacer:\n")

if opcion_jugador == "1":
    array_nombre = []
    print("Dime el número de archivos que deseas comprimir")
    numero_archivos = int(input())
    for i in range(numero_archivos):
        print(f"Dime el nombre del archivo número {i+1}:")
        while True:
            file_name = input().strip()
            if file_name in files and file_name not in array_nombre and os.path.splitext(file_name)[1] in terminaciones:
                array_nombre.append(file_name)
                break
            else:
                print("Nombre no válido o archivo ya añadido, por favor, intenta de nuevo.")
    for file_name in array_nombre:
        try:
            foto = Image.open(os.path.join(ruta, file_name))
            foto = foto.convert('RGB')
            new_filename = f'{os.path.splitext(file_name)[0]}_compressed.jpg'
            foto.save(os.path.join(ruta_crear, new_filename), "JPEG", optimize=True, quality=50)
            print(f"{file_name} ha sido comprimida y guardada como {new_filename}")
        except IOError:
            print(f"No se pudo procesar la imagen {file_name}. Puede que el archivo esté dañado o no sea una imagen.")
elif opcion_jugador == "2":
    print("Comprimiendo imágenes...\n")
    for filename in files:
        if os.path.splitext(filename)[1] in terminaciones and os.path.isfile(os.path.join(ruta, filename)):
            try:
                foto = Image.open(os.path.join(ruta, filename))
                foto = foto.convert('RGB')
                new_filename = f'{os.path.splitext(filename)[0]}_compressed.jpg'
                foto.save(os.path.join(ruta_crear, new_filename), "JPEG", optimize=True, quality=50)
                print(f"{filename} ha sido comprimida y guardada como {new_filename}")
            except IOError:
                print(f"No se pudo procesar la imagen {filename}. Puede que el archivo esté dañado o no sea una imagen.")
elif opcion_jugador == "3":
    print("Saliendo...")
else:
    print("Opción no válida.")

# Asegúrate de tener PIL/Pillow actualizado e instalado.
