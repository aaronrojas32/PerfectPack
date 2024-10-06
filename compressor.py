import os
import time
from tqdm import tqdm

def RLE_compression(input_bytes):
    compressed = bytearray()
    length = len(input_bytes)
    count = 1
    
    for i in range(1, length):
        if input_bytes[i] == input_bytes[i - 1]:
            count += 1
            if count == 255:  # Maximum value that can be stored in one byte.
                compressed.append(input_bytes[i - 1])
                compressed.append(count)
                count = 1
        else:
            compressed.append(input_bytes[i - 1])
            if count > 1:
                compressed.append(count)
            count = 1

    compressed.append(input_bytes[-1])
    if count > 1:
        compressed.append(count)

    return compressed

def RLE_decompression(compressed_bytes):
    decompressed = bytearray()
    i = 0
    length = len(compressed_bytes)

    while i < length:
        byte = compressed_bytes[i]
        i += 1

        if i < length and compressed_bytes[i] < 255:
            count = compressed_bytes[i]
            i += 1
            decompressed.extend([byte] * count)
        else:
            decompressed.append(byte)

    return decompressed

def compress_file(input_file, output_file=None, chunk_size=8*1024*1024):
    start_time = time.time()
    file_size = os.path.getsize(input_file)
    
    file_name = os.path.basename(input_file)
    file_name_no_ext, file_ext = os.path.splitext(file_name)
    
    # Guardar el archivo comprimido en la misma carpeta que el archivo original
    if output_file is None:
        output_file = os.path.join(os.path.dirname(input_file), file_name_no_ext + ".myPack")
    
    print(f"\n\033[1mStarting compression...\033[0m\n")

    with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
              ascii=' █', desc="Compressing") as pbar:
        
        with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
            file_out.write(f"{file_name}\n".encode())
            
            while True:
                buffer = file_in.read(chunk_size)
                if not buffer:
                    break

                compressed_chunk = RLE_compression(buffer)
                file_out.write(compressed_chunk)
                pbar.update(len(buffer))

    end_time = time.time()
    print(f"\n\033[1mCompression completed in {end_time - start_time:.2f} seconds\033[0m")
    print(f"File saved as: {output_file}")

def decompress_file(compressed_file):
    start_time = time.time()

    with open(compressed_file, 'rb') as file_in:
        # Leer el nombre del archivo original
        original_file_name = file_in.readline().decode().strip()
        file_size = os.path.getsize(compressed_file) - len(original_file_name) - 1
        
        # Preguntar al usuario si quiere cambiar el nombre del archivo descomprimido
        new_file_name = input(f"Enter new name for the decompressed file (leave empty to use '{original_file_name}'): ").strip()

        # Si el usuario no introduce un nombre, se usa el nombre original
        if not new_file_name:
            decompressed_file = os.path.join(os.path.dirname(compressed_file), original_file_name)
        else:
            original_name_no_ext, original_ext = os.path.splitext(original_file_name)
            new_file_name = new_file_name + original_ext
            decompressed_file = os.path.join(os.path.dirname(compressed_file), new_file_name)

        print(f"\n\033[1mStarting decompression...\033[0m\n")
        
        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
                  bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
                  ascii=' █', desc="Decompressing") as pbar:
            
            with open(decompressed_file, 'wb') as file_out:
                while True:
                    buffer = file_in.read(1024)
                    if not buffer:
                        break

                    decompressed_chunk = RLE_decompression(buffer)
                    file_out.write(decompressed_chunk)
                    pbar.update(len(buffer))

    end_time = time.time()
    print(f"\n\033[1mDecompression completed in {end_time - start_time:.2f} seconds\033[0m")
    print(f"File decompressed as: {decompressed_file}")
