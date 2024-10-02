def RLE_compression(input):
    if not input:  # Si la cadena está vacía
        return ""

    compressed = ""
    count = 1

    # Recorremos la cadena por índice
    for i in range(1, len(input)):
        if input[i] == input[i - 1]:
            count += 1
        else:
            compressed += input[i - 1] + (str(count) if count > 1 else "")
            count = 1

    # Agregar el último grupo
    compressed += input[-1] + (str(count) if count > 1 else "")

    return compressed


def compress_file(input_file, output_file):
    # Leer el archivo de entrada
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Comprimir el contenido usando RLE
    compressed_content = RLE_compression(content)

    # Escribir el contenido comprimido en el archivo de salida
    with open(output_file, 'w') as file:
        file.write(compressed_content)


# Usar la función para comprimir un archivo
input_file = 'test.txt'  # Archivo de entrada
output_file = 'compressed.myPack'  # Archivo de salida
compress_file(input_file, output_file)
