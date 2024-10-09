import os
import filecmp
from colorama import Fore, Style
from compressor import compress_file, decompress_file

# Archivos de entrada
input_file_300 = "Test/test_300ch.txt"
input_file_1000 = "Test/test_1000ch.txt"
input_file_10000 = "Test/test_10000ch.txt"

# Archivos comprimidos y descomprimidos
compressed_file_300 = "Test/test_300ch.myPack"
compressed_file_1000 = "Test/test_1000ch.myPack"
compressed_file_10000 = "Test/test_10000ch.myPack"

def test_compression_decompression(input_file, compressed_file, algorithm="RLE"):
    """
    Test the compression and decompression process.
    """
    try:
        print(Fore.CYAN + f"=== Test for {input_file} using {algorithm} ===" + Style.RESET_ALL)
        
        # Compress the file
        compress_file(input_file, algorithm=algorithm, output_file=compressed_file)

        # Decompress the file
        decompressed_file = decompress_file(compressed_file, algorithm=algorithm, is_test=True)

        # Check if the decompressed file was created
        if not os.path.exists(decompressed_file):
            print(Fore.RED + f"Error: The decompressed file {decompressed_file} was not created." + Style.RESET_ALL)
            return False

        # Compare the original file with the decompressed one
        files_are_equal = filecmp.cmp(input_file, decompressed_file, shallow=False)
        if files_are_equal:
            print(Fore.GREEN + f"Success: The decompressed file is identical to the original." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Failure: The decompressed file differs from the original." + Style.RESET_ALL)

        return files_are_equal

    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}" + Style.RESET_ALL)
        return False

    finally:
        # Cleanup: Remove the compressed and decompressed files
        if os.path.exists(compressed_file):
            os.remove(compressed_file)

        if decompressed_file and os.path.exists(decompressed_file):
            os.remove(decompressed_file)


def run_tests():
    """
    Executes all defined tests automatically.
    """
    print(Fore.MAGENTA + "\n=== RUNNING TESTS ===" + Style.RESET_ALL)

    algorithms = ["RLE", "Huffman"]

    for algorithm in algorithms:
        # Test 1: Test with a 300-character file
        print(Fore.YELLOW + f"\n--- Test 1 ({algorithm}): 300-character file ---" + Style.RESET_ALL)
        result_300 = test_compression_decompression(input_file_300, compressed_file_300, algorithm=algorithm)
        if result_300:
            print(Fore.GREEN + f"Test 1 ({algorithm}) completed successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test 1 ({algorithm}) failed." + Style.RESET_ALL)

        # Test 2: Test with a 1000-character file
        print(Fore.YELLOW + f"\n--- Test 2 ({algorithm}): 1000-character file ---" + Style.RESET_ALL)
        result_1000 = test_compression_decompression(input_file_1000, compressed_file_1000, algorithm=algorithm)
        if result_1000:
            print(Fore.GREEN + f"Test 2 ({algorithm}) completed successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test 2 ({algorithm}) failed." + Style.RESET_ALL)

        # Test 3: Test with a 10000-character file
        print(Fore.YELLOW + f"\n--- Test 3 ({algorithm}): 10000-character file ---" + Style.RESET_ALL)
        result_10000 = test_compression_decompression(input_file_10000, compressed_file_10000, algorithm=algorithm)
        if result_10000:
            print(Fore.GREEN + f"Test 3 ({algorithm}) completed successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test 3 ({algorithm}) failed." + Style.RESET_ALL)


# Run the tests
if __name__ == "__main__":
    run_tests()
