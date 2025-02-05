import json
import base64
from cryptography.fernet import Fernet

def encrypt_transcripts(input_file="data/meeting_notes.json", encrypted_file="data/encrypted_transcripts.enc", key_file="config/encryption_key.key"):
    """ Encrypt and save meeting transcripts """
    with open(key_file, "rb") as key_f:
        key = key_f.read()
    cipher = Fernet(key)

    with open(input_file, "r") as file:
        data = json.load(file)
    
    encrypted_data = cipher.encrypt(json.dumps(data).encode("utf-8"))
    
    with open(encrypted_file, "wb") as enc_file:
        enc_file.write(encrypted_data)
    
    print("Meeting transcripts encrypted successfully.")

if __name__ == "__main__":
    encrypt_transcripts()
