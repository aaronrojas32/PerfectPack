from compressor import compress_file, decompress_file

def user_interface():
    """
    Provides a simple command-line interface for compressing and decompressing files.
    The user can choose between compressing a file, decompressing a file, or exiting the program.
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
            try:
                compress_file(input_file)
            except Exception as e:
                print(f"An error occurred during compression: {e}")
        
        elif option == 2:
            compressed_file = input("Enter the path to the compressed file: ")
            try:
                decompress_file(compressed_file)
            except Exception as e:
                print(f"An error occurred during decompression: {e}")
        
        elif option == 3:
            print("Exiting the program...")
        
        else:
            print("Invalid option. Please choose a valid option.")
