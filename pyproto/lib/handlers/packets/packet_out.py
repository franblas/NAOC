import struct

def write_byte(code):
  return struct.pack('B', code).encode('hex')

def write_short(code, endian='big'):
  if endian == 'big':
    return struct.pack('>H', code).encode('hex')
  elif endian == 'little':
    return struct.pack('<H', code).encode('hex')
  else:
    return struct.pack('H', code).encode('hex')

def write_int(code, endian='big'):
  if endian == 'big':
    return struct.pack('>I', code).encode('hex')
  elif endian == 'little':
    return struct.pack('<I', code).encode('hex')
  else:
    return struct.pack('I', code).encode('hex')

def write_long(code, endian='big'):
  if endian == 'big':
    return struct.pack('>L', code).encode('hex')
  elif endian == 'little':
    return struct.pack('<L', code).encode('hex')
  else:
    return struct.pack('L', code).encode('hex')

def packet_length(pak):
  return len(pak.decode('hex'))

def write_string(s):
  if not s or len(s) <= 0: return write_byte(0x00)
  return s.encode('hex')

def write_pascal_string(s):
  if not s or len(s) <= 0: return write_byte(0x00)
  str_to_hex = s.encode('hex')
  pak_len = write_byte(packet_length(str_to_hex))
  return pak_len + str_to_hex

def fill_pak(code, nb):
  return ''.join([write_byte(code) for i in range(nb)])

def fill_string_pak(s, nb):
  encoded_s = write_string(s)
  len_s = packet_length(encoded_s)
  if nb <= len_s:
    return encoded_s
  else:
    return encoded_s + ''.join([write_byte(0x00) for i in range(nb - len_s)])
