# Write your script here

class ExecuteCrypto(object): 
    def generate_keys(self):
        """Generate keys"""

        # Write your script here



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
        """Generate nonces"""

        # Write your script here



        print("Nonce for AES-128-CBC") 
        print(nonce_aes_cbc) 
        print("Nonce for AES-128-CTR") 
        print(nonce_aes_ctr) 
        print("NOnce for RSA-2048") 
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

    def encrypt(self, algo, key, plaintext, nonce): 
        """Encrypt the given plaintext"""

        # Write your script here


        if algo == 'AES-128-CBC-ENC': 
            # Write your script here

        elif algo == 'AES-128-CTR-ENC': 
            # Write your script here

        elif algo == 'RSA-2048-ENC': 
            # Write your script here

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

        elif algo == 'AES-128-CTR-DEC': 
            # Write your script here

        elif algo == 'RSA-2048-DEC': 
            # Write your script here

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

    def generate_auth_tag(self, algo, key, plaintext, nonce): 
        """Generate the authenticate tag for the given plaintext"""

        # Write your script here

        if algo =='AES-128-CMAC-GEN': 
            # Write your script here

        elif algo =='SHA3-256-HMAC-GEN': 
            # Write your script here

        elif algo =='RSA-2048-SHA3-256-SIG-GEN': 
            # Write your script here

        elif algo =='ECDSA-256-SHA3-256-SIG-GEN': 
            # Write your script here

        else:
            raise Exception("Unexpected algorithm") 

        # Write your script here


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

    def verify_auth_tag(self, algo, key, plaintext, nonce, auth_tag): 
        """Verify the authenticate tag for the given plaintext"""

        # Write your script here

        if algo =='AES-128-CMAC-VRF': 
            # Write your script here

        elif algo =='SHA3-256-HMAC-VRF': 
            # Write your script here

        elif algo =='RSA-2048-SHA3-256-SIG-VRF': 
            # Write your script here

        elif algo =='ECDSA-256-SHA3-256-SIG-VRF': 
            # Write your script here

        else:
            raise Exception("Unexpected algorithm") 

        # Write your script here

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
        """Encrypt and generate the authentication tag for the given plaintext"""

        # Write your script here

        if algo == 'AES-128-GCM-GEN': 
            # Write your script here

        else:
            raise Exception("Unexpected algorithm") 

        # Write your script here

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
        """Decrypt and verify the authentication tag for the given plaintext"""

        # Write your script here

        if algo == 'AES-128-GCM-VRF': 
            # Write your script here

        else:
            raise Exception("Unexpected algorithm") 

        # Write your script here

        print("Algorithm") 
        print(algo) 
        print("Decryption Key") 
        print(key_decrypt) 
        print("Authentication Key") 
        print(key_verify_auth) 
        print("Plaintext") 
        print(plaintext) 
        print("Nonce") 
        print(nonce) 
        print("Ciphertext") 
        print(ciphertext) 
        print("Authentication Tag") 
        print(auth_tag) 
        print("Authentication Tag Valid") 
        print(auth_tag_valid) 

        return plaintext, auth_tag_valid 

if __name__ == '__main__': 
    ExecuteCrypto() 
