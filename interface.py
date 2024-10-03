option = -1

while option != 3:
    print("1. Compress file")
    print("2. Decompress file")
    print("3. Exit")

    option = int(input("Enter an option: "))

    if option == 1:
        print("compressing...")
    
    elif option == 2:
        print("Decompressing...")
    
    else:
        print("Exit...")
