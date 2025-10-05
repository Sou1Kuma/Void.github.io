# local_decrypt.py
# Usage: python local_decrypt.py <cipherfile.bin> <base64url_key> [out_file]
import sys, base64
from Crypto.Cipher import AES
from pathlib import Path

if len(sys.argv) < 3:
    print('Usage: python local_decrypt.py <cipherfile.bin> <base64url_key> [out_file]')
    raise SystemExit(1)

infile = Path(sys.argv[1])
key_b64url = sys.argv[2]
outp = Path(sys.argv[3]) if len(sys.argv) > 3 else infile.with_suffix('.dec')

if not infile.exists():
    print('Input not found:', infile); raise SystemExit(1)

s = key_b64url.replace('-', '+').replace('_', '/')
s += '=' * ((4 - len(s) % 4) % 4)
key = base64.b64decode(s)
data = infile.read_bytes()
iv = data[:12]
cipher_and_tag = data[12:]
try:
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    plaintext = cipher.decrypt_and_verify(cipher_and_tag[:-16], cipher_and_tag[-16:])
except Exception as e:
    print('Decryption failed:', e)
    raise SystemExit(1)
outp.write_bytes(plaintext)
print('Wrote plaintext to', outp)
