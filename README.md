# **🚀 Advanced File Compression Tool (RLE & Huffman) 🚀**

A modern and efficient tool for compressing and decompressing files using the **Run-Length Encoding (RLE)** and **Huffman Encoding** algorithms. This tool features a sleek, professional GUI, progress bars for long operations, and restores the original file formats upon decompression.

## **🛠 Features**
- **Multiple Compression Algorithms**: Supports both **RLE** and **Huffman** encoding.
- **GUI Interface**: A user-friendly graphical interface with an intuitive design.
- **Original Format Recovery**: Automatically restores the original file name and extension after decompression.
- **Progress Tracking**: Displays a dynamic progress bar during compression and decompression operations.
- **Large File Handling**: Efficient processing of large files with chunk-based operations.
- **Customizable Output**: Allows users to specify custom output filenames.

## **📁 Project Structure**

```
project/
│
├── compressor.py         # Core compression/decompression logic for RLE and Huffman
├── interface.py          # Graphical User Interface (GUI) using CustomTkinter
├── main.py               # Main program entry point
└── README.md             # Project documentation (this file)
```

### **🔍 File Descriptions**
- **compressor.py**: Contains the implementation for both **RLE** and **Huffman** compression algorithms, managing files efficiently by processing them in chunks.
- **interface.py**: Provides the graphical interface for user interaction with the tool, enabling file selection, compression algorithm choice, and progress visualization.

## **🔄 How It Works**

### **Compression**
- Select the input file and preferred compression algorithm (RLE or Huffman).
- The tool compresses the file and saves it with the `.myPack` extension by default.
- The original file name and extension are preserved for use during decompression.

### **Decompression**
- Choose a `.myPack` file, and the tool will automatically restore the original file name and format based on the metadata stored in the compressed file.

## **📜 Usage Instructions**

### **Running the GUI Tool**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aaronrojas32/PerfectPack.git
   cd PerfectPack
   ```

2. **Install the required dependencies**:
   ```bash
   pip install tqdm customtkinter
   ```

3. **Run the tool**:
   ```bash
   python main.py
   ```

4. **Interact with the GUI**:
   - **Compress a file**: Select the file, choose an algorithm (RLE or Huffman), and click "Compress".
   - **Decompress a file**: Select a `.myPack` file and click "Decompress".
   - **Progress**: A real-time progress bar will display the compression or decompression status.

### **📊 Example**

**Compressing a File via the GUI**
- After selecting the file, choose the desired compression algorithm:
  - RLE for run-length encoding.
  - Huffman for Huffman encoding.
  
- Then, click **"Compress"** to start the process.

```plaintext
[Progress bar updating]
Compression completed in 5.43 seconds.
File saved as: example.myPack
```

**Decompressing a File via the GUI**
- Select the `.myPack` file, and click **"Decompress"** to restore the original file.

```plaintext
[Progress bar updating]
Decompression completed in 4.12 seconds.
File decompressed as: example.txt
```

## **📥 Installation & Requirements**

- **Python 3** is required.
- Install dependencies using the following command:
  ```bash
  pip install -r requirements.txt
  ```

## **👨‍💻 Development & Contribution**

We welcome contributions from the community! Follow the steps below to contribute:

1. **Fork the repository** to your GitHub account.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes**, and thoroughly test them.
4. **Commit your changes** with a descriptive commit message:
   ```bash
   git commit -m "Add new feature: Improved compression"
   ```
5. **Push your changes** to your fork:
   ```bash
   git push origin feature-branch
   ```
6. **Open a Pull Request** on the main repository to propose your changes.

## **🔮 Future Enhancements**
- **Support for additional algorithms**: Expand the tool to include more compression techniques.
- **Parallel Processing**: Implement multi-threading to enhance speed and performance for large files.
- **Extended Platform Support**: Ensure compatibility across a wider range of operating systems.
- **Testing and Automation**: Increase unit tests and improve code reliability with CI/CD pipelines.

## **📄 License**
This project is licensed under the MIT License. You can view the license details in the [LICENSE](LICENSE) file.

---

Thank you for using and contributing to the Advanced File Compression Tool! 🙌
