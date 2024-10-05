# **✨ RLE File Compressor and Decompressor ✨**

A simple and efficient tool for compressing and decompressing files using the **Run-Length Encoding (RLE)** algorithm. This tool features a user-friendly command-line interface, progress bars for long operations, and the ability to restore original file formats upon decompression.

## **🛠 Features**
- **Compression & Decompression**: Supports RLE algorithm.
- **Original Format Recovery**: Restores the original file format and extension.
- **Progress Bars**: Displays progress during long operations.
- **Chunk Processing**: Efficient handling of large files.
- **Custom Extension**: Outputs files with the `.myPack` extension.

## **📁 Project Structure**

```
project/
│
├── compressor.py         # RLE compression/decompression logic
├── interface.py          # Command-line interface
├── main.py               # Main program entry point
└── README.md             # Project documentation (this file)
```

### **🔍 File Descriptions**
- **compressor.py**: Implements RLE compression and decompression, reading files in manageable chunks.
- **interface.py**: Provides a CLI for users to interact with the tool.

## **🔄 How It Works**

### **Compression**
- Reads the input file, compresses it with RLE, and saves it as `.myPack`.
- Stores the original file name and extension for decompression.

### **Decompression**
- Restores the original file name and extension based on metadata in the `.myPack` file.

## **📜 Usage Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aaronrojas32/PerfectPack.git
   cd PerfectPack
   ```

2. **Run the tool**:
   ```bash
   python main.py
   ```

3. **Choose an option**:
   - **Compress a file**: Enter the path to the file.
   - **Decompress a file**: Enter the path to the `.myPack` file.
   - **Exit**: Close the application.

### **📊 Example**

**Compressing a File**
```bash
$ python main.py
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

**Decompressing a File**
```bash
$ python main.py
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

## **📥 Installation & Requirements**

- **Python 3** is required.
- Install dependencies with:
  ```bash
  pip install tqdm
  ```

## **🤝 Collaboration and Contributions**

We welcome contributions! Here’s how you can help:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make and test your changes**.
4. **Commit your changes** with a clear message:
   ```bash
   git commit -m "Description of changes"
   ```
5. **Push your branch**:
   ```bash
   git push origin feature-branch
   ```
6. **Create a Pull Request** on the original repository.

## **🔮 Future Improvements**
- Support for additional compression algorithms.
- Multi-threading for faster performance.
- Enhanced testing for reliability.
- Potential GUI expansion.

## **📝 License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for contributing and using the RLE file compression tool! 🚀
