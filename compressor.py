import os
import time
from tqdm import tqdm

def RLE_compression(input_bytes):
    """
    Compresses the input bytes using the Run-Length Encoding (RLE) algorithm.
    
    Args:
        input_bytes (bytes): The data to compress.
    
    Returns:
        bytearray: The compressed data.
    """
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

    # Add the last byte
    compressed.append(input_bytes[-1])
    if count > 1:
        compressed.append(count)

    return compressed

def RLE_decompression(compressed_bytes):
    """
    Decompresses the data that was compressed using the RLE algorithm.
    
    Args:
        compressed_bytes (bytes): The compressed data.
    
    Returns:
        bytearray: The decompressed data.
    """
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
    """
    Compresses a file using RLE and stores the original filename in the compressed file.
    
    Args:
        input_file (str): Path to the input file to be compressed.
        output_file (str): Path to the output compressed file. If None, replaces the original extension with '.myPack'.
        chunk_size (int): Size of chunks to read from the input file (default: 8MB).
    """
    start_time = time.time()
    file_size = os.path.getsize(input_file)
    
    # Get original file name and extension
    file_name = os.path.basename(input_file)
    file_name_no_ext, file_ext = os.path.splitext(file_name)  # Split name and extension
    
    # If no output file is specified, create a .myPack file
    if output_file is None:
        output_file = file_name_no_ext + ".myPack"
    
    print(f"\n\033[1mStarting compression...\033[0m\n")

    with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
              ascii=' █', desc="Compressing") as pbar:
        
        with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
            # Write the header with the original file name and extension
            file_out.write(f"{file_name}\n".encode())
            
            while True:
                buffer = file_in.read(chunk_size)
                if not buffer:
                    break

                # Compress the data using RLE
                compressed_chunk = RLE_compression(buffer)

                # Write compressed chunk to the output file
                file_out.write(compressed_chunk)

                # Update progress bar
                pbar.update(len(buffer))

    end_time = time.time()
    print(f"\n\033[1mCompression completed in {end_time - start_time:.2f} seconds\033[0m")
    print(f"File saved as: {output_file}")

def decompress_file(compressed_file):
    """
    Decompresses a file that was compressed using the custom RLE format, restoring the original filename.
    
    Args:
        compressed_file (str): Path to the compressed file.
    """
    start_time = time.time()

    with open(compressed_file, 'rb') as file_in:
        # Read the header to get the original filename
        file_name = file_in.readline().decode().strip()  # The full original name with extension
        file_size = os.path.getsize(compressed_file) - len(file_name) - 1  # Estimate size excluding the header

        print(f"\n\033[1mStarting decompression...\033[0m\n")
        
        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
                  bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
                  ascii=' █', desc="Decompressing") as pbar:
            
            with open(file_name, 'wb') as file_out:
                while True:
                    buffer = file_in.read(1024)
                    if not buffer:
                        break

                    # Decompress the data using RLE
                    decompressed_chunk = RLE_decompression(buffer)

                    # Write decompressed chunk to the output file
                    file_out.write(decompressed_chunk)

                    # Update progress bar
                    pbar.update(len(buffer))

    end_time = time.time()
    print(f"\n\033[1mDecompression completed in {end_time - start_time:.2f} seconds\033[0m")
    print(f"File decompressed as: {file_name}")
