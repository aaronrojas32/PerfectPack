import compressor
import filecmp
import os

input_file = "Test/test_300ch.txt"
compressed_file = "Test/test_300ch.myPack"
decompressed_file = "Test/test_300ch_c.txt"

def test_compression_decompression(input_file, compressed_file, decompressed_file):
    """
    Tests the compression and decompression process, comparing the original and decompressed files.
    """
    print("\n\033[1mStarting the compression and decompression test...\033[0m")

    # Compress the file
    print(f"\nCompressing the file: {input_file}")
    compressor.compress_file(input_file, compressed_file)

    # Check if the compressed file exists
    if not os.path.exists(compressed_file):
        print(f"\033[91mError: The compressed file {compressed_file} was not created correctly.\033[0m")
        return False

    # Decompress the file
    print(f"\nDecompressing the compressed file: {compressed_file}")
    compressor.decompress_file(compressed_file)

    # Check if the decompressed file exists
    if not os.path.exists(decompressed_file):
        print(f"\033[91mError: The decompressed file {decompressed_file} was not created correctly.\033[0m")
        return False

    # Compare the original file with the decompressed one
    files_are_equal = filecmp.cmp(input_file, decompressed_file, shallow=False)
    if files_are_equal:
        print(f"\033[92mSuccess: The decompressed file {decompressed_file} is identical to the original file.\033[0m")
    else:
        print(f"\033[91mFailure: The decompressed file {decompressed_file} is different from the original file.\033[0m")
    
    return files_are_equal


def run_tests():
    """
    Executes all defined tests.
    """
    print("\n\033[1m=== RUNNING TESTS ===\033[0m")

    # Test 1: Test with a 300-character file
    result = test_compression_decompression(input_file, compressed_file, decompressed_file)
    if result:
        print("\033[92mTest 1 completed successfully.\033[0m")
    else:
        print("\033[91mTest 1 failed.\033[0m")


# Run the tests
if __name__ == "__main__":
    run_tests()
