#Caesar Cipher
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
key = 3
plaintext = "Ahmed Osman"
# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha():ciphertext += I2L[ (L2I[c] + key)%26 ]
    else: ciphertext += c
# decipher
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
    else: plaintext2 += c
print ("text :"+plaintext)
print ("ciphertext :"+ciphertext)
print( "plaintext :"+plaintext2)

input("enter to exit");
