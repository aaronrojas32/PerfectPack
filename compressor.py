import time
from tqdm import tqdm

# Compresión RLE aún más optimizada
def RLE_compression(input_bytes):
    compressed = bytearray()
    length = len(input_bytes)
    
    count = 1
    for i in range(1, length):
        if input_bytes[i] == input_bytes[i - 1]:
            count += 1
            if count == 255:  # Máximo valor que puede ser almacenado en un byte (255)
                compressed.append(input_bytes[i - 1])
                compressed.append(count)
                count = 1
        else:
            compressed.append(input_bytes[i - 1])
            if count > 1:
                compressed.append(count)
            count = 1

    # Agregar el último byte
    compressed.append(input_bytes[-1])
    if count > 1:
        compressed.append(count)

    return compressed

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

# Usar la función para comprimir un archivo
input_file = 'test.txt'  # Archivo de entrada (puede ser binario)
output_file = 'test.myPack'  # Archivo de salida (en modo binario)
compress_file(input_file, output_file)
