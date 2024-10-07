import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from compressor import compress_file, decompress_file

# Configuración inicial para CustomTkinter
ctk.set_appearance_mode("dark")  # Tema oscuro
ctk.set_default_color_theme("blue")  # Color principal azul

class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PerfectPack")
        
        # Ajustamos el tamaño de la ventana para que todo se vea bien
        self.root.geometry("500x500")  # Aumentamos la altura a 500px para que quepan todos los elementos.
        self.root.resizable(False, False)

        # Header
        self.title_label = ctk.CTkLabel(root, text="File Compression Tool", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=20)

        # File selection
        self.file_frame = ctk.CTkFrame(root)
        self.file_frame.pack(pady=10, padx=10, fill="x")

        self.file_path_var = ctk.StringVar()
        self.file_path_entry = ctk.CTkEntry(self.file_frame, textvariable=self.file_path_var, width=300, placeholder_text="Select a file...")
        self.file_path_entry.grid(row=0, column=0, padx=10, pady=10)

        self.browse_button = ctk.CTkButton(self.file_frame, text="Browse", command=self.browse_file, width=100)
        self.browse_button.grid(row=0, column=1, padx=10, pady=10)

        # Algorithm selection
        self.algorithm_label = ctk.CTkLabel(root, text="Select Compression Algorithm:", font=ctk.CTkFont(size=14))
        self.algorithm_label.pack(pady=10)

        self.algorithm_var = ctk.StringVar(value="RLE")
        self.rle_radio = ctk.CTkRadioButton(root, text="RLE (Run-Length Encoding)", variable=self.algorithm_var, value="RLE")
        self.huffman_radio = ctk.CTkRadioButton(root, text="Huffman Encoding", variable=self.algorithm_var, value="Huffman")
        self.rle_radio.pack(pady=5)
        self.huffman_radio.pack(pady=5)

        # Custom file name input
        self.custom_name_label = ctk.CTkLabel(root, text="Custom Output Name (Optional):", font=ctk.CTkFont(size=14))
        self.custom_name_label.pack(pady=5)

        self.custom_name_var = ctk.StringVar()
        self.custom_name_entry = ctk.CTkEntry(root, textvariable=self.custom_name_var, width=350, placeholder_text="Leave blank for original name...")
        self.custom_name_entry.pack(pady=5)

        # Progress bar
        self.progress = ctk.CTkProgressBar(root, width=400)
        self.progress.pack(pady=10)

        # Compress/Decompress Buttons (Ajustamos el espaciado para que todo quepa)
        self.button_frame = ctk.CTkFrame(root)
        self.button_frame.pack(pady=40)  # Aumentamos el espacio aquí para no cortar

        self.compress_button = ctk.CTkButton(self.button_frame, text="Compress", command=self.compress_file, width=150)
        self.compress_button.grid(row=0, column=0, padx=20)  # Ajustamos el espacio horizontal

        self.decompress_button = ctk.CTkButton(self.button_frame, text="Decompress", command=self.decompress_file, width=150)
        self.decompress_button.grid(row=0, column=1, padx=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_var.set(file_path)

    def compress_file(self):
        file_path = self.file_path_var.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file to compress.")
            return

        custom_name = self.custom_name_var.get()
        algorithm = self.algorithm_var.get()

        output_file = custom_name if custom_name else None

        try:
            # Simulate compression progress
            self.progress.set(0)
            self.root.update_idletasks()

            if algorithm == "RLE":
                compress_file(file_path, output_file, algorithm="RLE", progress_callback=self.update_progress)
            else:
                compress_file(file_path, output_file, algorithm="Huffman", progress_callback=self.update_progress)

            messagebox.showinfo("Success", "File successfully compressed!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during compression: {e}")

    def decompress_file(self):
        file_path = self.file_path_var.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file to decompress.")
            return

        try:
            self.progress.set(0)
            self.root.update_idletasks()

            # Decompress the selected file
            decompress_file(file_path, progress_callback=self.update_progress)

            messagebox.showinfo("Success", "File successfully decompressed!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decompression: {e}")

    def update_progress(self, value):
        self.progress.set(value / 100)
        self.root.update_idletasks()


# Run the application
if __name__ == "__main__":
    root = ctk.CTk()
    app = CompressionApp(root)
    root.mainloop()
