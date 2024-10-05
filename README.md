# **RLE File Compressor and Decompressor**

This project implements a **Run-Length Encoding (RLE)** file compression and decompression tool. The tool compresses files using the RLE algorithm, which is efficient for files with repeated sequences of bytes. It includes a command-line interface for easy interaction, a progress bar during compression/decompression, and restores the original file format when decompressing.

## **Features**
- Compress files using the **RLE** algorithm.
- Decompress files and recover the original file format and extension.
- Displays a progress bar during both compression and decompression for large files.
- Handles large files efficiently by processing them in chunks.
- Automatically outputs compressed files with the `.myPack` extension.
- Easy to use via a simple command-line interface.

## **Project Structure**

```
project/
│
├── compressor.py         # Implements RLE compression and decompression algorithms
├── interface.py          # Provides the command-line interface for interacting with the tool
├── main.py               # Contains the principal class of the program
└── README.md             # Project documentation (this file)
```

### **Files Explanation:**
- **compressor.py**: Contains the core logic for compression and decompression using the RLE algorithm. It reads files in chunks to ensure memory efficiency when processing large files.
- **interface.py**: This script provides the command-line interface where users can select options to compress or decompress files.

## **How It Works**

### **Compression**
The tool reads an input file, compresses it using the **RLE algorithm**, and outputs the compressed file with a `.myPack` extension. The original file name and extension are stored within the compressed file, allowing the decompressor to recreate the original file when decompressed.

### **Decompression**
When decompressing a `.myPack` file, the tool restores the original file name and extension based on the metadata saved during compression. It decompresses the file in chunks and outputs the original file with its proper format.

## **Usage**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aaronrojas32/PerfectPack.git
   cd PerfectPack
   ```

2. **Run the tool**:
   ```bash
   python main.py
   ```

3. **Options**:
   - **Compress a file**: Enter the path to the file you want to compress.
   - **Decompress a file**: Enter the path to the `.myPack` file.
   - **Exit**: Closes the application.

### **Example**

```bash
$ python main.py

File Compression/Decompression Tool
1. Compress file
2. Decompress file
3. Exit
Enter an option: 1
Enter the path to the file to compress: example.txt

Compressing...
[Progress bar showing]

Compression completed in 5.43 seconds.
File saved as: example.myPack
```

```bash
$ python main.py

File Compression/Decompression Tool
1. Compress file
2. Decompress file
3. Exit
Enter an option: 2
Enter the path to the compressed file: example.myPack

Decompressing...
[Progress bar showing]

Decompression completed in 4.12 seconds.
File decompressed as: example.txt
```

## **Installation and Requirements**

This project uses Python and the `tqdm` package for displaying progress bars. Install the necessary dependencies:

```bash
pip install tqdm
```

Make sure you have Python 3 installed. The code should work across different operating systems (Windows, Linux, macOS).

## **Collaboration and Contributions**

We welcome contributions to improve this project. Below are ways you can contribute:

### **1. Fork the repository**
Go to the [repository page](https://github.com/aaronrojas32/PerfectPack), click the "Fork" button in the top right, and create your own copy of the project.

### **2. Create a new branch**
Create a new branch for your feature or bugfix:

```bash
git checkout -b feature-branch
```

### **3. Make your changes**
Implement your improvements or bug fixes in your local environment.

### **4. Test your changes**
Make sure that your changes work as expected by testing them. You can add new tests or manually run the compression/decompression routines.

### **5. Commit your changes**
Commit your changes with a clear message describing the purpose:

```bash
git commit -m "Added a new feature to improve RLE compression efficiency"
```

### **6. Push the branch**
Push the branch to your forked repository:

```bash
git push origin feature-branch
```

### **7. Create a Pull Request**
Go to the original repository, click on the "Pull Requests" tab, and create a new pull request from your branch. Provide a description of the changes made and the improvements.

## **Suggestions for Future Improvements**
- Support for other compression algorithms.
- Additional features like multi-threading for faster compression/decompression.
- Adding tests to improve code reliability.
- Expanding the tool with a graphical user interface (GUI).

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for contributing and using the RLE file compression tool!
