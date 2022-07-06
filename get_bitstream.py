from bitarray import bitarray
from bitarray.util import zeros

def get_bitstream(key, initial_value):
    streamA = zeros(93)
    streamB = zeros(84)
    streamC = zeros(111)
    if len(key) != 80:
        raise Exception('Key is the wrong length')
    if len(initial_value) != 80:
        raise Exception('Initial Value is the wrong length')
    
    streamA[13:93] = key
    streamB[13:93] = initial_value
    return streamA , streamB
