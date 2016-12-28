import struct

def read_data(raw_data):
    data = raw_data.encode('hex')
    return [bytes(eval('0x' + a + b)) for a, b in zip(data[0::2], data[1::2])]

def decode_bytes(seq):
    return eval('0x' + ''.join([struct.pack('B', int(s)).encode('hex') for s in seq]))

def read_string(sequence, size, cursor):
    seq = sequence[cursor:cursor + size]
    return ''.join([chr(int(s)) for s in seq]), cursor + len(seq)

def read_byte(sequence, cursor):
    return decode_bytes([sequence[cursor]]), cursor + 1

def read_int(sequence, cursor, endian='big'):
    seq = sequence[cursor:cursor + 4]
    if endian == 'big':
        return decode_bytes(seq), cursor + len(seq)
    elif endian == 'little':
        return decode_bytes(seq[::-1]), cursor + len(seq) # reverse sequence
    else:
        return int(''.join(seq)), cursor + len(seq)

def read_short(sequence, cursor, endian='big'):
    seq = sequence[cursor:cursor + 2]
    if endian == 'big':
        return decode_bytes(seq), cursor + len(seq)
    elif endian == 'little':
        return decode_bytes(seq[::-1]), cursor + len(seq) # reverse sequence
    else:
        return int(''.join(seq)), cursor + len(seq)

def skip(pos, new_pos):
    return pos + new_pos
