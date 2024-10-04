from compressor import RLE_compression
from tqdm import tqdm
import time
import os

# Función para comprimir un archivo, aceptando todo tipo de archivos
def compress_file(input_file, output_file, chunk_size=8*1024*1024):  # Leer en trozos de 8MB por defecto
    start_time = time.time()

    # Obtener el tamaño total del archivo para la barra de progreso
    with open(input_file, 'rb') as file:
        file.seek(0, 2)
        total_size = file.tell()
        file.seek(0)

    print(f"\n\033[1mIniciando la compresión...\033[0m\n")

    with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024,
              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
              ascii=' █', desc="Comprimiendo") as pbar:
        
        with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
            while True:
                buffer = file_in.read(chunk_size)
                if not buffer:
                    break

                # Comprimir el fragmento usando RLE
                compressed_chunk = RLE_compression(buffer)

                # Escribir el fragmento comprimido al archivo de salida
                file_out.write(compressed_chunk)

                # Actualizar la barra de progreso
                pbar.update(len(buffer))

    end_time = time.time()
    print(f"\n\033[1mCompresión completada en {end_time - start_time:.2f} segundos\033[0m")

input_file = input("Introduca el path del arhcivo a comprimir: ")
output_file = 'test.myPack'
compress_file(input_file,output_file)