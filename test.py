import compressor
import filecmp
import os

# Define the input files for the tests
input_file_300 = "Test/test_300ch.txt"
compressed_file_300 = "Test/test_300ch.myPack"

input_file_1000 = "Test/test_1000ch.txt"
compressed_file_1000 = "Test/test_1000ch.myPack"

input_file_10000 = "Test/test_10000ch.txt"
compressed_file_10000 = "Test/test_10000ch.myPack"


def test_compression_decompression(input_file, compressed_file):
    """
    Tests the compression and decompression process, comparing the original and decompressed files.
    Automatically generates decompressed file names during testing and cleans up the temporary files after.
    """
    print(f"\n\033[1mStarting the compression and decompression test for {input_file}...\033[0m")

    try:
        # Compress the file
        print(f"\nCompressing the file: {input_file}")
        compressor.compress_file(input_file, compressed_file)

        # Check if the compressed file exists
        if not os.path.exists(compressed_file):
            print(f"\033[91mError: The compressed file {compressed_file} was not created correctly.\033[0m")
            return False

        # Decompress the file and automatically generate decompressed file name
        print(f"\nDecompressing the compressed file: {compressed_file}")
        decompressed_file = compressor.decompress_file(compressed_file, is_test=True)

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

    finally:
        # Cleanup: Remove the compressed and decompressed files after the test
        if os.path.exists(compressed_file):
            os.remove(compressed_file)
            print(f"\033[93mDeleted: {compressed_file}\033[0m")

        if os.path.exists(decompressed_file):
            os.remove(decompressed_file)
            print(f"\033[93mDeleted: {decompressed_file}\033[0m")


def run_tests():
    """
    Executes all defined tests automatically, handling file names internally, and cleaning up generated files.
    """
    print("\n\033[1m=== RUNNING TESTS ===\033[0m")

    # Test 1: Test with a 300-character file
    print("\n\033[1m--- Test 1: 300-character file ---\033[0m")
    result_300 = test_compression_decompression(input_file_300, compressed_file_300)
    if result_300:
        print("\033[92mTest 1 completed successfully.\033[0m")
    else:
        print("\033[91mTest 1 failed.\033[0m")

    # Test 2: Test with a 1000-character file
    print("\n\033[1m--- Test 2: 1000-character file ---\033[0m")
    result_1000 = test_compression_decompression(input_file_1000, compressed_file_1000)
    if result_1000:
        print("\033[92mTest 2 completed successfully.\033[0m")
    else:
        print("\033[91mTest 2 failed.\033[0m")

    # Test 3: Test with a 10000-character file
    print("\n\033[1m--- Test 3: 10000-character file ---\033[0m")
    result_10000 = test_compression_decompression(input_file_10000, compressed_file_10000)
    if result_10000:
        print("\033[92mTest 3 completed successfully.\033[0m")
    else:
        print("\033[91mTest 3 failed.\033[0m")


# Run the tests
if __name__ == "__main__":
    run_tests()
