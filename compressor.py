
def RLE_compression(input_bytes):
    compressed = bytearray()
    length = len(input_bytes)
    
    count = 1
    for i in range(1, length):
        if input_bytes[i] == input_bytes[i - 1]:
            count += 1
            if count == 255:  # Máximo valor que puede ser almacenado en un byte (255)
                compressed.append(input_bytes[i - 1])
                compressed.append(count)
                count = 1
        else:
            compressed.append(input_bytes[i - 1])
            if count > 1:
                compressed.append(count)
            count = 1

    # Agregar el último byte
    compressed.append(input_bytes[-1])
    if count > 1:
        compressed.append(count)

    return compressed