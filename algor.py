from bitarray import bitarray
from bitarray import bits2bytes
from bitarray.util import zeros
from get_bitstream import get_bitstream
import secrets

def encrypt_file(filename,encrypted_filename,key):
    
    initial_value = bitarray()
    message = bitarray()
    name_bytes = bitarray()
    
    initial_value.frombytes(secrets.token_bytes(10))
    
    ciphertext = bitarray(initial_value)
    
    name_bytes.frombytes(filename.encode('utf-8'))
    filename_length = bits2bytes(len(name_bytes))
    
    message.frombytes(filename_length.to_bytes(1,'little'))
    message = message + name_bytes

    with open(filename, mode='rb') as file:
        message.fromfile(file)

    bitstream = get_bitstream(key, initial_value,len(message))

    ciphertext += bitstream ^ message

    with open('encrypted\\'+encrypted_filename, mode='wb') as file:
        ciphertext.tofile(file)

def decrypt_file(filename,key):
    filedata = bitarray()
    initial_value = bitarray()
    message = bitarray()
    name_bytes = bitarray()
    plaintext = bitarray()
    file_out = bitarray()
    

    with open(filename, mode='rb') as file:
        filedata.fromfile(file)

    initial_value = filedata[0:80]
    message = filedata[80:]

    bitstream = get_bitstream(key, initial_value,len(message))

    plaintext = bitstream ^ message

    filename_length = int.from_bytes(plaintext[0:8].tobytes(),'little')  
    name_bytes = plaintext[8:8*(filename_length+1)]
    filename = name_bytes.tobytes().decode('utf-8')
    print(filename)

    file_out = plaintext[8*(filename_length+1):]
    print('The first 8 bytes are:\n')
    print(file_out[0:64].tobytes())
    with open('decrypted\\'+filename, mode='wb') as file:
        file_out.tofile(file)
    
