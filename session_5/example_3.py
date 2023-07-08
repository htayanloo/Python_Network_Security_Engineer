#!/usr/bin/python

def lock_file(file_name):
    buffer_size = 100

    source_file = open(file_name,"rb")
    destination_file = open(f"{file_name}__lock","ab")
    key_file = open(f"{file_name}__key","ab")

    chunk = source_file.read(buffer_size)
    chunk_key_number = [1,3,6]
    chunk_key_number_count = 0
    while chunk:
        if chunk_key_number_count in chunk_key_number:
            key_file.write(chunk)
        else:
            destination_file.write(chunk)
        chunk_key_number_count += 1
        chunk = source_file.read(buffer_size)
    source_file.close()
    destination_file.close()
    key_file.close()

lock_file("a.jpg")



