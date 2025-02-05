import os
import json
import re
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define file paths
ENCRYPTED_FILE = "data/encrypted_transcripts.enc"
KEY_FILE = "config/encryption_key.key"

def load_encryption_key():
    """ Load encryption key from file """
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key file not found. Run secure_config.py first.")
    
    with open(KEY_FILE, "rb") as key_f:
        return key_f.read()

def decrypt_transcripts():
    """ Decrypt and load meeting transcripts """
    if not os.path.exists(ENCRYPTED_FILE):
        raise FileNotFoundError("Encrypted transcript file not found. Run data_loader.py first.")

    key = load_encryption_key()
    cipher = Fernet(key)

    with open(ENCRYPTED_FILE, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
    return json.loads(decrypted_data)

def clean_transcript_text(text):
    """ Preprocess transcript text for AI processing """
    text = text.strip()  # Remove leading/trailing spaces
    text = re.sub(r"\s+", " ", text)  # Normalize whitespace
    text = re.sub(r"([a-z])\.\s+([A-Z])", r"\1. \2", text)  # Fix punctuation spacing
    return text

def process_transcripts():
    """ Load, clean, and return transcripts """
    try:
        transcripts = decrypt_transcripts()
        processed_transcripts = []

        for transcript in transcripts:
            cleaned_text = clean_transcript_text(transcript["discussion"])
            processed_transcripts.append({
                "date": transcript["date"],
                "attendees": transcript["attendees"],
                "cleaned_text": cleaned_text
            })

        return processed_transcripts

    except Exception as e:
        print(f"Error processing transcripts: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    transcripts = process_transcripts()
    if transcripts:
        print("✅ Processed transcripts successfully.")
        print(json.dumps(transcripts[:1], indent=2))  # Display sample output
    else:
        print("❌ No transcripts processed.")
