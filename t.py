# encrypt_file.py
# pip install pycryptodome
import os, sys, hashlib, base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

if len(sys.argv) < 2:
    print("Usage: python encrypt_file.py input_file")
    sys.exit(1)

inp = sys.argv[1]
data = open(inp, "rb").read()

key = get_random_bytes(32)           # 256-bit key
iv  = get_random_bytes(12)           # 96-bit nonce for GCM
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
ct, tag = cipher.encrypt_and_digest(data)

blob = iv + ct + tag                 # store like this
sha = hashlib.sha256(blob).hexdigest()  # object id (you can use this as filename)
outname = f"{sha}.bin"
open(outname, "wb").write(blob)

# base64url encode key (no padding) for putting into URL fragment
key_b64 = base64.urlsafe_b64encode(key).rstrip(b"=").decode()

print("Wrote ciphertext ->", outname)
print("Object id (sha256):", sha)
print("Key (base64url, use as fragment):", key_b64)
print("\nExample capability URL (recommended uses fragment):")
print(f"https://yourhost.example.com/files/{sha}/{os.path.basename(inp)}#{key_b64}")
