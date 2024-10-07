import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import compressor  # Assuming RLE functions are inside compressor.py

class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compression Tool")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Style for ttk widgets
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 10))
        style.configure("TCheckbutton", font=("Arial", 10))
        style.configure("TCombobox", font=("Arial", 10))

        # Compression Section
        self.label_compress = ttk.Label(root, text="Compress a File:")
        self.label_compress.pack(pady=10)

        self.button_compress = ttk.Button(root, text="Select File to Compress", command=self.select_file_to_compress)
        self.button_compress.pack(pady=5)

        # Compression Algorithm Selector
        self.label_algorithm = ttk.Label(root, text="Select Compression Algorithm:")
        self.label_algorithm.pack(pady=5)

        self.algorithms = ["RLE", "Huffman"]
        self.combo_algorithm = ttk.Combobox(root, values=self.algorithms, state="readonly")
        self.combo_algorithm.current(0)  # Default to RLE
        self.combo_algorithm.pack(pady=5)

        # Custom filename checkbox and entry field
        self.custom_name_var = tk.IntVar()
        self.check_custom_name = ttk.Checkbutton(root, text="Custom Filename", variable=self.custom_name_var, command=self.toggle_custom_name)
        self.check_custom_name.pack(pady=5)

        self.entry_custom_name = ttk.Entry(root, state='disabled', width=40)
        self.entry_custom_name.pack(pady=5)

        # Decompression Section
        self.label_decompress = ttk.Label(root, text="Decompress a File:")
        self.label_decompress.pack(pady=10)

        self.button_decompress = ttk.Button(root, text="Select File to Decompress", command=self.select_file_to_decompress)
        self.button_decompress.pack(pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=20)

        # Close button
        self.button_close = ttk.Button(root, text="Close", command=root.quit)
        self.button_close.pack(pady=20)

    def toggle_custom_name(self):
        """
        Enable or disable the custom name entry based on the checkbox.
        """
        if self.custom_name_var.get():
            self.entry_custom_name.config(state='normal')
        else:
            self.entry_custom_name.delete(0, 'end')
            self.entry_custom_name.config(state='disabled')

    def select_file_to_compress(self):
        """
        Opens a file dialog to choose a file to compress.
        """
        file_path = filedialog.askopenfilename(title="Select a File to Compress")
        if file_path:
            self.compress_file(file_path)

    def compress_file(self, file_path):
        """
        Compress the selected file and display progress.
        """
        try:
            algorithm = self.combo_algorithm.get()  # Get selected algorithm
            file_name, file_extension = os.path.splitext(file_path)
            if self.custom_name_var.get():  # If custom name is enabled
                custom_name = self.entry_custom_name.get()
                output_file = os.path.join(os.path.dirname(file_path), custom_name + ".myPack")
            else:
                output_file = file_name + ".myPack"

            self.progress['value'] = 0  # Reset progress bar
            self.update_progress(10)  # Simulate progress (you should update based on actual compression)

            if algorithm == "RLE":
                compressor.compress_file(file_path, output_file)
            elif algorithm == "Huffman":
                with open(file_path, 'r') as f:
                    input_data = f.read()
                compressed_data, root = compressor.huffman_compress(input_data)
                with open(output_file, 'wb') as f:
                    f.write(compressed_data)

            self.update_progress(100)  # Full progress once done
            messagebox.showinfo("Success", f"File compressed successfully as {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to compress file: {e}")

    def select_file_to_decompress(self):
        """
        Opens a file dialog to choose a compressed file to decompress.
        """
        compressed_file_path = filedialog.askopenfilename(title="Select a Compressed File", 
                                                          filetypes=[("Compressed Files", "*.myPack")])
        if compressed_file_path:
            self.decompress_file(compressed_file_path)

    def decompress_file(self, compressed_file_path):
        """
        Decompress the selected file and display progress.
        """
        try:
            algorithm = self.combo_algorithm.get()  # Get selected algorithm
            output_file = os.path.splitext(compressed_file_path)[0]  # Strip the .myPack extension

            self.progress['value'] = 0  # Reset progress bar
            self.update_progress(10)  # Simulate progress (you should update based on actual decompression)

            if algorithm == "RLE":
                compressor.decompress_file(compressed_file_path, output_file)
            elif algorithm == "Huffman":
                with open(compressed_file_path, 'rb') as f:
                    compressed_data = f.read()
                with open(output_file, 'w') as f:
                    f.write(compressor.huffman_decompress(compressed_data))

            self.update_progress(100)  # Full progress once done
            messagebox.showinfo("Success", f"File decompressed successfully as {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decompress file: {e}")

    def update_progress(self, value):
        """
        Update the progress bar.
        """
        self.progress['value'] = value
        self.root.update_idletasks()  # This is important to make sure the GUI updates the progress bar


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionApp(root)
    root.mainloop()
