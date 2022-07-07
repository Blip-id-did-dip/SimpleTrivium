from bitarray import bitarray
from bitarray.util import zeros

def get_bitstream(key, initial_value, numbits):
    streamA = zeros(93)
    streamB = zeros(84)
    streamC = zeros(111)
    
    if len(key) != 80:
        raise Exception('Key is the wrong length')
    if len(initial_value) != 80:
        raise Exception('Initial Value is the wrong length')
    
    streamA[13:93] = key
    streamB[13:93] = initial_value

    bitA = bitarray(1)
    bitB = bitarray(1)
    bitC = bitarray(1)

    bitstream = bitarray(numbits)
    
    for iter in range(0,1152):
        bitA = streamC[45]^streamC[0]^(streamC[1]&streamC[2])^streamA[24]
        bitB = streamA[27]^streamA[0]^(streamA[1]&streamA[2])^streamB[6]
        bitC = streamB[15]^streamB[0]^(streamB[1]&streamB[2])^streamC[24]

        streamA <<= 1
        streamB <<= 1
        streamC <<= 1

        streamA[-1] = bitA
        streamB[-1] = bitB
        streamC[-1] = bitC

    for iter in range(0,len(bitstream)):
        bitA = streamC[45]^streamC[0]^(streamC[1]&streamC[2])^streamA[24]
        bitB = streamA[27]^streamA[0]^(streamA[1]&streamA[2])^streamB[6]
        bitC = streamB[15]^streamB[0]^(streamB[1]&streamB[2])^streamC[24]

        streamA <<= 1
        streamB <<= 1
        streamC <<= 1

        streamA[-1] = bitA
        streamB[-1] = bitB
        streamC[-1] = bitC

        bitstream[iter] = streamC[45]^streamC[0]^streamA[27]^streamA[0]^streamB[15]^streamB[0]
    
    
    return bitstream
    
