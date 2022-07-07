from bitarray import bitarray
from bitarray.util import zeros
from get_bitstream import get_bitstream
from algor import encrypt_file
from algor import decrypt_file
import secrets




key = bitarray()
key.frombytes(b'ABCDEFGHJK')


filename = 'secretMessage.txt'

encrypt_file(filename,'mySecret.enc',key)
             
decrypt_file('encrypted\mySecret.enc',key)
