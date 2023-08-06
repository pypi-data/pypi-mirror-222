import base64, hashlib, Cryptodome, Crypto

async def genkey():
    generated_key = Crypto.Random.new().read(Cryptodome.Cipher.AES.block_size)
    key = hashlib.sha256(generated_key).digest()
    with open("aeseasyencryption.key", "wb") as key_file:
        key_file.write(key)
    return key

async def callkey():
  try:
    key = open("aeseasyencryption.key", "rb").read()
    if str(key) == "b''":
      await genkey()
      key = open("aeseasyencryption.key", "rb").read()
    return key
  except:
    await genkey()
    key = open("aeseasyencryption.key", "rb").read()
    return key


async def aesencrypt(slogan:str):
    key = await callkey()
    BS = Cryptodome.Cipher.AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    slogan = base64.b64encode(pad(slogan).encode('utf8'))
    iv = Crypto.Random.get_random_bytes(Cryptodome.Cipher.AES.block_size)
    cipher = Cryptodome.Cipher.AES.new(key=key, mode= Cryptodome.Cipher.AES.MODE_CFB,iv= iv)
    return base64.b64encode(iv + cipher.encrypt(slogan))

async def aesdecrypt(coded_slogan:bytes):
    key = await callkey()
    unpad = lambda s: s[:-ord(s[-1:])]

    coded_slogan = base64.b64decode(coded_slogan)
    iv = coded_slogan[:Cryptodome.Cipher.AES.block_size]
    cipher = Cryptodome.Cipher.AES.new(key, Cryptodome.Cipher.AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(coded_slogan[Cryptodome.Cipher.AES.block_size:])).decode('utf8'))