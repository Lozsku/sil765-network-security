from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode, b64decode
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives.padding import PKCS7
from os import urandom
import time
import sys

def cal_packet_length( ciphertext, nonce):
    ciphertext_bytes = len(b64decode(ciphertext))
    nonce_bytes = len(nonce)
    total_length_bits = (ciphertext_bytes + nonce_bytes) * 8
    print("packet_length",total_length_bits)
    return total_length_bits
def cal_packet_len2(plaintext, auth_tag, nonce):
    packet_size = len(plaintext)
    packet_size += len(auth_tag)
    packet_size += len(nonce)
    print("packet_size",packet_size*8)

    return packet_size*8

def cal_key_length(key):
    key_bytes = key
    key_length_bytes = len(key_bytes)*8
    print("key_length",key_length_bytes)
    return key_length_bytes

def aes_128_cbc_encrypt(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Use PKCS7 directly from cryptography.hazmat.primitives.padding
    padder = PKCS7(algorithms.AES.block_size).padder()

    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return b64encode(ciphertext).decode('utf-8')

def aes_128_cbc_decrypt(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Use PKCS7 directly from cryptography.hazmat.primitives.padding
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()

    decrypted_data = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()
    plaintext = unpadder.update(decrypted_data) + unpadder.finalize()
    return plaintext.decode('utf-8')

def aes_128_ctr_encrypt(key, nonce, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    return b64encode(ciphertext).decode('utf-8')

def aes_128_ctr_decrypt(key, nonce, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()
    return decrypted_data.decode('utf-8')

def rsa_2048_encrypt(public_key, plaintext):
    key = serialization.load_pem_public_key(public_key.encode('utf-8'), backend=default_backend())
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')

    ciphertext = key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return b64encode(ciphertext).decode('utf-8')

def rsa_2048_decrypt(private_key, ciphertext):
    key = serialization.load_pem_private_key(
        private_key.encode('utf-8'),
        password=None,
        backend=default_backend()
    )
    decrypted_data = key.decrypt(
        b64decode(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data


class ExecuteCrypto(object): 
    def generate_keys(self):
        # Symmetric Key
        symmetric_key = urandom(16)

        # Sender's RSA Key Pair
        private_key_sender_rsa, public_key_sender_rsa = self.generate_rsa_key_pair()

        # Receiver's RSA Key Pair
        private_key_receiver_rsa, public_key_receiver_rsa = self.generate_rsa_key_pair()

        # Sender's ECC Key Pair
        private_key_sender_ecc, public_key_sender_ecc = self.generate_ecc_key_pair()

        print("Symmetric Key")
        print(symmetric_key)
        print("Sender's RSA Public Key")
        print(public_key_sender_rsa)
        print("Sender's RSA Private Key")
        print(private_key_sender_rsa)
        print("Receiver's RSA Public Key")
        print(public_key_receiver_rsa)
        print("Receiver's RSA Private Key")
        print(private_key_receiver_rsa)
        print("Sender's ECC Public Key")
        print(public_key_sender_ecc)
        print("Sender's ECC Private Key")
        print(private_key_sender_ecc)

        return symmetric_key, \
               public_key_sender_rsa, private_key_sender_rsa, \
               public_key_receiver_rsa, private_key_receiver_rsa, \
               public_key_sender_ecc, private_key_sender_ecc

    def generate_nonces(self):
        nonce_aes_cbc = urandom(16)
        nonce_aes_ctr = urandom(16)
        nonce_encrypt_rsa = urandom(16)
        nonce_aes_cmac = urandom(16)
        nonce_hmac = urandom(16)
        nonce_tag_rsa = urandom(16)
        nonce_ecdsa = urandom(16)
        nonce_aes_gcm = urandom(12)  # Nonce for AES-GCM should be 12 bytes

        print("Nonce for AES-128-CBC")
        print(nonce_aes_cbc)
        print("Nonce for AES-128-CTR")
        print(nonce_aes_ctr)
        print("Nonce for RSA-2048")
        print(nonce_encrypt_rsa)
        print("Nonce for AES-128-CMAC")
        print(nonce_aes_cmac)
        print("Nonce for SHA3-256-HMAC")
        print(nonce_hmac)
        print("Nonce for RSA-2048-SHA3-256")
        print(nonce_tag_rsa)
        print("Nonce for ECDSA")
        print(nonce_ecdsa)
        print("Nonce for AES-128-GCM")
        print(nonce_aes_gcm)

        return nonce_aes_cbc, nonce_aes_ctr, nonce_encrypt_rsa, nonce_aes_cmac, \
               nonce_hmac, nonce_tag_rsa, nonce_ecdsa, nonce_aes_gcm

    def generate_rsa_key_pair(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        return private_pem, public_pem

    def generate_ecc_key_pair(self):
        private_key = ec.generate_private_key(
            ec.SECP256R1(),
            default_backend()
        )
        public_key = private_key.public_key()
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        return private_pem, public_pem

    def encrypt(self, algo, key, plaintext, nonce): 
        """Encrypt the given plaintext"""

        # Write your script here


        if algo == 'AES-128-CBC-ENC': 
            # Write your script here
            start_time = time.time()
            ciphertext = aes_128_cbc_encrypt(key,nonce,plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        elif algo == 'AES-128-CTR-ENC': 
            # Write your script here
            start_time = time.time()
            ciphertext = aes_128_ctr_encrypt(key,nonce,plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        elif algo == 'RSA-2048-ENC': 
            # Write your script here
            start_time = time.time()
            ciphertext = rsa_2048_encrypt(key,plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        else: 
            raise Exception("Unexpected algorithm") 

        # Write your script here


        print("Algorithm") 
        print(algo) 
        print("Encryption Key") 
        print(key) 
        print("Plaintext") 
        print(plaintext) 
        print("Nonce") 
        print(nonce) 
        print("Ciphertext") 
        print(ciphertext) 

        return ciphertext 

    def decrypt(self, algo, key, ciphertext, nonce): 
        """Decrypt the given ciphertext"""
        # Write your script here

        if algo=='AES-128-CBC-DEC': 
            # Write your script here
            start_time=time.time()
            plaintext = aes_128_cbc_decrypt(key,nonce,ciphertext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_length(ciphertext,nonce)

        elif algo == 'AES-128-CTR-DEC': 
            # Write your script here
            start_time=time.time()
            plaintext = aes_128_ctr_decrypt(key,nonce,ciphertext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_length(ciphertext,nonce)

        elif algo == 'RSA-2048-DEC': 
            # Write your script here
            start_time=time.time()
            plaintext = rsa_2048_decrypt(key,ciphertext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_length(ciphertext,nonce)
            

        else: 
            raise Exception("Unexpected algorithm") 

        # Write your script here

        print("Algorithm") 
        print(algo) 
        print("Decryption Key") 
        print(key) 
        print("Plaintext") 
        print(plaintext) 
        print("Nonce") 
        print(nonce) 
        print("Ciphertext") 
        print(ciphertext) 
        return plaintext 
# 333333333333333333333333333333333333333
    def generate_aes_cmac(self, key, plaintext):
        mac = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        mac.update(plaintext.encode('utf-8'))
        return mac.finalize()

    def generate_sha3_hmac(self, key, plaintext):
        mac = hmac.HMAC(key, hashes.SHA3_256(), backend=default_backend())
        mac.update(plaintext.encode('utf-8'))
        return mac.finalize()

    def generate_rsa_signature(self, key, plaintext):
        private_key = serialization.load_pem_private_key(key.encode('utf-8'), password=None, backend=default_backend())
        signature = private_key.sign(
            plaintext.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA3_256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA3_256()
        )
        return b64encode(signature).decode('utf-8')

    def generate_ecdsa_signature(self, key, plaintext):
        private_key = serialization.load_pem_private_key(key.encode('utf-8'), password=None, backend=default_backend())
        hasher = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
        hasher.update(plaintext.encode('utf-8'))
        hashed_data = hasher.finalize()
        signature = private_key.sign(
            hashed_data,
            ec.ECDSA(utils.Prehashed(hashes.SHA3_256()))
        )
        return b64encode(signature).decode()
# 3333333333333333333333333333333333333333
    def generate_auth_tag(self, algo, key, plaintext, nonce):
        if algo == 'AES-128-CMAC-GEN':
            start_time=time.time()
            auth_tag = self.generate_aes_cmac(key, plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        elif algo == 'SHA3-256-HMAC-GEN':
            start_time=time.time()
            auth_tag = self.generate_sha3_hmac(key, plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        elif algo == 'RSA-2048-SHA3-256-SIG-GEN':
            start_time=time.time()
            auth_tag = self.generate_rsa_signature(key, plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        elif algo == 'ECDSA-256-SHA3-256-SIG-GEN':
            start_time=time.time()
            auth_tag = self.generate_ecdsa_signature(key, plaintext)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
        else:
            raise Exception("Unexpected algorithm")

        print("Algorithm")
        print(algo)
        print("Authentication Key")
        print(key)
        print("Plaintext")
        print(plaintext)
        print("Nonce")
        print(nonce)
        print("Authentication Tag")
        print(auth_tag)

        return auth_tag
#444444444444444444444444444444444
    def verify_aes_cmac_auth_tag(self,key, plaintext, auth_tag):
        mac = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        mac.update(plaintext.encode('utf-8'))
        try:
            mac.verify(auth_tag)
            return True
        except:
            return False

    def verify_sha3_hmac_auth_tag(self,key, plaintext, auth_tag):
        mac = hmac.HMAC(key, hashes.SHA3_256(), backend=default_backend())
        mac.update(plaintext.encode('utf-8'))
        try:
            mac.verify(auth_tag)
            return True
        except:
            return False

    def verify_rsa_signature_auth_tag(self,key, plaintext, auth_tag):
        public_key = serialization.load_pem_public_key(key.encode('utf-8'), backend=default_backend())
        signature = b64decode(auth_tag)
        try:
            public_key.verify(
                signature,
                plaintext.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA3_256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA3_256()
            )
            return True
        except:
            return False

    def verify_ecdsa_signature_auth_tag(self,key, plaintext, auth_tag):
        public_key = serialization.load_pem_public_key(key.encode('utf-8'), backend=default_backend())
        hasher = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
        hasher.update(plaintext.encode('utf-8'))
        hashed_data = hasher.finalize()
        signature = b64decode(auth_tag)
        try:
            public_key.verify(
                signature,
                hashed_data,
                ec.ECDSA(utils.Prehashed(hashes.SHA3_256()))
            )
            return True
        except:
            return False
#44444444444444444444444444444444444444444444444
    def verify_auth_tag(self, algo, key, plaintext, nonce, auth_tag):
        if algo == 'AES-128-CMAC-VRF':
            start_time=time.time()
            auth_tag_valid = self.verify_aes_cmac_auth_tag(key, plaintext, auth_tag)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_len2(plaintext,auth_tag,nonce)

        elif algo == 'SHA3-256-HMAC-VRF':
            start_time=time.time()
            auth_tag_valid = self.verify_sha3_hmac_auth_tag(key, plaintext, auth_tag)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_len2(plaintext,auth_tag,nonce)

        elif algo == 'RSA-2048-SHA3-256-SIG-VRF':
            start_time=time.time()
            auth_tag_valid=self.verify_rsa_signature_auth_tag(key, plaintext, auth_tag)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_len2(plaintext,auth_tag,nonce)

        elif algo == 'ECDSA-256-SHA3-256-SIG-VRF':
            start_time=time.time()
            auth_tag_valid=self.verify_ecdsa_signature_auth_tag(key, plaintext, auth_tag)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key)
            cal_packet_len2(plaintext,auth_tag,nonce)
        else:
            raise Exception("Unexpected algorithm")

        print("Algorithm")
        print(algo)
        print("Authentication Key")
        print(key)
        print("Plaintext")
        print(plaintext)
        print("Nonce")
        print(nonce)
        print("Authentication Tag")
        print(auth_tag)
        print("Authentication Tag Valid")
        print(auth_tag_valid)

        return auth_tag_valid

    def encrypt_generate_auth(self, algo, key_encrypt, key_generate_auth, plaintext, nonce):
        if algo == 'AES-128-GCM-GEN':
            start_time=time.time()
            cipher = Cipher(algorithms.AES(key_encrypt), modes.GCM(nonce), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
            auth_tag = encryptor.tag
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)

        else:
            raise Exception("Unexpected algorithm")

        print("Algorithm")
        print(algo)
        print("Encryption Key")
        print(key_encrypt)
        print("Authentication Key")
        print(key_generate_auth)
        print("Plaintext")
        print(plaintext)
        print("Nonce")
        print(nonce)
        print("Ciphertext")
        print(ciphertext)
        print("Authentication Tag")
        print(auth_tag)

        return ciphertext, auth_tag

    def decrypt_verify_auth(self, algo, key_decrypt, key_verify_auth, ciphertext, nonce, auth_tag):
        if algo == 'AES-128-GCM-VRF':
            start_time=time.time()
            cipher = Cipher(algorithms.AES(key_decrypt), modes.GCM(nonce, auth_tag), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
            plaintext = decrypted_data.decode('utf-8')
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(execution_time)
            cal_key_length(key_decrypt)
            ciphertext_bytes = len(ciphertext)
            ciphertext_bytes+=len(nonce)+len(auth_tag)
            print("packet_size",ciphertext_bytes)

        else:
            raise Exception("Unexpected algorithm")

        print("Algorithm")
        print(algo)
        print("Decryption Key")
        print(key_decrypt)
        print("Authentication Key")
        print(key_verify_auth)
        print("Ciphertext")
        print(ciphertext)
        print("Nonce")
        print(nonce)
        print("Authentication Tag")
        print(auth_tag)
        print("Plaintext")
        print(plaintext)

        return plaintext,auth_tag

if __name__ == '__main__': 
    ExecuteCrypto() 
