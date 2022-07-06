from bitarray import bitarray
from bitarray.util import zeros
from get_bitstream import get_bitstream
import secrets




key = bitarray()
key.frombytes(b'ABCDEFGHJK')

initial_value = bitarray()
initial_value.frombytes(secrets.token_bytes(10))

print('The length of the key is: ', len(key))

streamA = bitarray()
streamB = bitarray()

streamA , streamB = get_bitstream(key, initial_value)

print(streamA)
print(streamB)


