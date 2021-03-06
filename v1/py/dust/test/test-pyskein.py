import sys
from dust.crypto.pyskein import skein512
from dust.core.util import encode

v3=(sys.version[0]=='3')

### Print hash of MSG if called directly ###
if __name__ == "__main__":
  if v3:
    MSG = bytes("Nobody inspects the spammish repetition", 'ascii')
  else:
    MSG = "Nobody inspects the spammish repetition"

  hash = skein512(msg=MSG, digest_bits=256)
  print(encode(hash))

  hash = skein512(msg=MSG, digest_bits=512)
  print(encode(hash))
