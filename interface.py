from compressor import compress_file, decompress_file, huffman_compress, huffman_decompress

def user_interface():
    """
    Provides a simple command-line interface for compressing and decompressing files.
    The user can choose between compressing a file, decompressing a file, and selecting the compression algorithm.
    """
    option = -1

    while option != 3:
        print("\n\033[1mFile Compression/Decompression Tool\033[0m")
        print("1. Compress file")
        print("2. Decompress file")
        print("3. Exit")

        try:
            option = int(input("Enter an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            input_file = input("Enter the path to the file to compress: ")
            print("\nSelect compression algorithm:")
            print("1. RLE (Run-Length Encoding)")
            print("2. Huffman Encoding")

            try:
                algorithm_option = int(input("Enter an option (1 or 2): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if algorithm_option == 1:
                # Use RLE for compression
                try:
                    compress_file(input_file)  # Assuming RLE is the default in compress_file
                    print(f"File '{input_file}' successfully compressed using RLE.")
                except Exception as e:
                    print(f"An error occurred during RLE compression: {e}")

            elif algorithm_option == 2:
                # Use Huffman for compression (handle binary files)
                try:
                    with open(input_file, 'rb') as f:  # Read file as binary
                        input_data = f.read()
                    compressed_data, root = huffman_compress(input_data)  # Compress the binary data
                    output_file = input_file + ".myPack"
                    with open(output_file, 'wb') as f:  # Save as binary
                        f.write(compressed_data)
                    print(f"File '{input_file}' successfully compressed using Huffman as '{output_file}'.")
                except Exception as e:
                    print(f"An error occurred during Huffman compression: {e}")
            else:
                print("Invalid option for compression algorithm.")
        
        elif option == 2:
            compressed_file = input("Enter the path to the compressed file: ")
            print("\nSelect decompression algorithm:")
            print("1. RLE (Run-Length Encoding)")
            print("2. Huffman Encoding")

            try:
                algorithm_option = int(input("Enter an option (1 or 2): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if algorithm_option == 1:
                # Use RLE for decompression
                try:
                    decompress_file(compressed_file)  # Assuming RLE is the default in decompress_file
                    print(f"File '{compressed_file}' successfully decompressed using RLE.")
                except Exception as e:
                    print(f"An error occurred during RLE decompression: {e}")

            elif algorithm_option == 2:
                # Use Huffman for decompression (handle binary files)
                try:
                    with open(compressed_file, 'rb') as f:  # Read compressed file as binary
                        compressed_data = f.read()
                    output_file = compressed_file.replace('.myPack', '_decompressed')  # Decompressed file
                    decompressed_data = huffman_decompress(compressed_data, root=None)  # Assuming root can be recovered
                    with open(output_file, 'wb') as f:  # Save decompressed data as binary
                        f.write(decompressed_data)
                    print(f"File '{compressed_file}' successfully decompressed using Huffman as '{output_file}'.")
                except Exception as e:
                    print(f"An error occurred during Huffman decompression: {e}")
            else:
                print("Invalid option for decompression algorithm.")

        elif option == 3:
            print("Exiting the program...")
        
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    user_interface()
