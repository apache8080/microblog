from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64

def pad(s):
    bs = 32
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

option = int(input('Cipher or Decipher'))

if (option == 0) :
    text = str(input('What do you want to Cipher'))
    input_key = '12351235123412351234451235123456789101112123'
    key = hashlib.sha256(input_key.encode()).digest()
    print 'Here is your key: '+input_key
    # Encryption
    iv = Random.new().read( AES.block_size )
    encryption_suite = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = base64.b64encode(iv+encryption_suite.encrypt(pad(text)))

    print cipher_text
elif (option == 1):
    # Decryption
    encrypted_text = raw_input('what do you want to decrypt')
    user_key = str(input('enter your key'))
    enc = base64.b64decode(encrypted_text)
    iv = enc[:16]
    key = hashlib.sha256(user_key.encode()).digest()
    decryption_suite = AES.new(key, AES.MODE_CBC, iv)
    plain_text = decryption_suite.decrypt(enc)
    print plain_text
else:
    print 'HUH?!?!?!?!'
