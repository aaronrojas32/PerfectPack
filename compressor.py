import os
import time
from tqdm import tqdm
import heapq
from collections import Counter
from colorama import Fore, Style

# Inicializar colorama
import colorama
colorama.init()

# Huffman Tree Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    root = heapq.heappop(priority_queue)
    huffman_code = {}
    build_codes(root, "", huffman_code)
    return root, huffman_code

def build_codes(node, current_code, huffman_code):
    if node is None:
        return
    if node.char is not None:
        huffman_code[node.char] = current_code
    build_codes(node.left, current_code + "0", huffman_code)
    build_codes(node.right, current_code + "1", huffman_code)

def huffman_compress(input_data):
    root, huffman_code = build_huffman_tree(input_data)
    encoded_data = ''.join(huffman_code[char] for char in input_data)

    # Pad the encoded data to make it a multiple of 8 bits
    extra_padding = 8 - len(encoded_data) % 8
    encoded_data += "0" * extra_padding

    # Store the padding info in the first byte
    padded_info = "{0:08b}".format(extra_padding)
    encoded_data = padded_info + encoded_data

    # Convert the encoded binary string into bytes
    compressed_data = bytearray()
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        compressed_data.append(int(byte, 2))

    return compressed_data, root

def huffman_decompress(compressed_data, root):
    if root is None:
        raise ValueError("El árbol Huffman es requerido para la descompresión")

    encoded_data = ''.join(format(byte, '08b') for byte in compressed_data)

    # Get the padding info from the first byte
    extra_padding = int(encoded_data[:8], 2)
    encoded_data = encoded_data[8:]  # Remove padding info byte
    encoded_data = encoded_data[:-extra_padding]  # Remove padding from the end

    decoded_data = []
    current_node = root
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root

    return ''.join(decoded_data)

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

def compress_file(input_file, algorithm="RLE", output_file=None, chunk_size=8*1024*1024, show_progress=True):
    start_time = time.time()
    file_size = os.path.getsize(input_file)

    file_name = os.path.basename(input_file)
    file_name_no_ext, file_ext = os.path.splitext(file_name)

    if output_file is None:
        output_file = os.path.join(os.path.dirname(input_file), file_name_no_ext + ".myPack")

    print(Fore.GREEN + f"\nStarting compression using {algorithm}...\n" + Style.RESET_ALL)

    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
                        ascii=' █', desc="Compressing") if show_progress else None

    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        file_out.write(f"{file_name}\n".encode())  # Store the original file name in the header

        if algorithm == "RLE":
            while True:
                buffer = file_in.read(chunk_size)
                if not buffer:
                    break
                compressed_chunk = RLE_compression(buffer)
                file_out.write(compressed_chunk)
                if progress_bar:
                    progress_bar.update(len(buffer))

        elif algorithm == "Huffman":
            input_data = file_in.read()
            compressed_data, _ = huffman_compress(input_data.decode('latin-1'))  # Decode using latin-1
            file_out.write(compressed_data)
            if progress_bar:
                progress_bar.update(len(input_data))

    if progress_bar:
        progress_bar.close()

    end_time = time.time()
    print(Fore.GREEN + f"\nCompression completed in {end_time - start_time:.2f} seconds" + Style.RESET_ALL)
    print(Fore.YELLOW + f"File saved as: {output_file}" + Style.RESET_ALL)

def decompress_file(compressed_file, algorithm="RLE", output_file=None, is_test=False, show_progress=True):
    start_time = time.time()

    with open(compressed_file, 'rb') as file_in:
        original_file_name = file_in.readline().decode().strip()  # The original filename
        
        if is_test:
            original_name, original_ext = os.path.splitext(original_file_name)
            output_file = f"Test/{original_name}_decompressed{original_ext}"

        if output_file is None:
            output_file = original_file_name

        file_size = os.path.getsize(compressed_file) - len(original_file_name) - 1

        print(Fore.GREEN + f"\nStarting decompression using {algorithm}...\n" + Style.RESET_ALL)

        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024,
                            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
                            ascii=' █', desc="Decompressing") if show_progress else None

        with open(output_file, 'wb') as file_out:
            if algorithm == "RLE":
                while True:
                    buffer = file_in.read(1024)
                    if not buffer:
                        break
                    decompressed_chunk = RLE_decompression(buffer)
                    file_out.write(decompressed_chunk)
                    if progress_bar:
                        progress_bar.update(len(buffer))

            elif algorithm == "Huffman":
                compressed_data = file_in.read()
                root, _ = build_huffman_tree(compressed_data.decode('latin-1'))  # Decode using latin-1
                decompressed_data = huffman_decompress(compressed_data, root)
                file_out.write(decompressed_data.encode('latin-1'))  # Ensure binary compatibility

        if progress_bar:
            progress_bar.close()

    end_time = time.time()
    print(Fore.GREEN + f"\nDecompression completed in {end_time - start_time:.2f} seconds" + Style.RESET_ALL)
    print(Fore.YELLOW + f"File decompressed as: {output_file}" + Style.RESET_ALL)
    return output_file
