import rsa
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    (publicserverKey, privateserverKey) = rsa.newkeys(1024)
    
    with open('publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
        
    with open('privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))
    
    with open('publicserverKey.pem', 'wb') as p:
        p.write(publicserverKey.save_pkcs1('PEM'))
        
    with open('privateserverKey.pem', 'wb') as p:
        p.write(privateserverKey.save_pkcs1('PEM'))

def loadKeys():
    with open('publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return publicKey,privateKey

def loadserverKeys():
    with open('publicKey.pem', 'rb') as p:
        publicserverKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('privateKey.pem', 'rb') as p:
        privateserverKey = rsa.PrivateKey.load_pkcs1(p.read())
    return publicserverKey,privateserverKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)
def decrypt(ciphertext, key):
    return rsa.decrypt(ciphertext, key).decode('ascii')
    
    
