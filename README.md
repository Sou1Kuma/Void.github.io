Capability-file hosting package
-------------------------------
Files included:
- decrypt.html         : browser-based client-side AES-GCM decrypt page (expects ciphertext at same path)
- local_decrypt.py     : decrypt locally with PyCryptodome (usage below)
- README.md (this file)

Steps to use:
1) You already have a ciphertext file produced (name: 6c64150e05d7c95d71b73051e3a1618eadb9570fbbbc70ad68d35f7d44e366ca.bin)
   Upload that file to your web host at the path you want, for example:
     https://yourhost.example.com/files/6c64150e05d7c95d71b73051e3a1618eadb9570fbbbc70ad68d35f7d44e366ca/6c64150e05d7c95d71b73051e3a1618eadb9570fbbbc70ad68d35f7d44e366ca.bin
   OR upload it as 'blob' next to decrypt.html:
     https://yourhost.example.com/files/6c64150e05d7c95d71b73051e3a1618eadb9570fbbbc70ad68d35f7d44e366ca/blob

2) Place decrypt.html in the same folder on your host (or point users to the page you host).
   Example capability URL (use fragment for key):
     https://yourhost.example.com/files/6c64150e05d7c95d71b73051e3a1618eadb9570fbbbc70ad68d35f7d44e366ca/decrypt.html#PqvOulgq9c3tSHE5fW4X_9X2f1_BDBs5PI_CIMdlkPs

   Note: the portion after '#' is never sent to the server (fragment) so the server logs won't contain the key.

3) Alternatively, you can distribute the file and key separately (key via chat/email, file via hosting).

Local decryption example:
  pip install pycryptodome
  python local_decrypt.py 6c64150e05d7c95d71b73051e3a1618eadb9570fbbbc70ad68d35f7d44e366ca.bin PqvOulgq9c3tSHE5fW4X_9X2f1_BDBs5PI_CIMdlkPs out.zip

Security notes:
- Keep the key out of logs: put it in the fragment (after '#') or transmit separately.
- Use HTTPS on your host to prevent MITM attacks and to protect the fragment when the page is fetched.
- Anyone with the capability URL (including fragment/key) can decrypt the file; treat the URL as a secret capability.
- Consider using short expiry or deleting the ciphertext after some time if you want limited lifetime access.
