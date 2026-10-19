
import base64
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def aes_encrypt(message: str) -> tuple[str, str]:
    """Encrypt text using AES-256-GCM."""
    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)

    aes = AESGCM(key)
    ciphertext = aes.encrypt(nonce, message.encode("utf-8"), None)

    key_b64 = base64.b64encode(key).decode("ascii")
    encrypted_b64 = base64.b64encode(
        nonce + ciphertext
    ).decode("ascii")

    return key_b64, encrypted_b64


def aes_decrypt(key_b64: str, encrypted_b64: str) -> str:
    """Decrypt AES-GCM ciphertext and verify its authentication tag."""
    key = base64.b64decode(key_b64, validate=True)
    payload = base64.b64decode(encrypted_b64, validate=True)

    if len(key) != 32:
        raise ValueError("AES-256 requires a 32-byte key.")

    if len(payload) < 28:
        raise ValueError("Encrypted payload is too short.")

    nonce = payload[:12]
    ciphertext = payload[12:]

    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")


def generate_rsa_keys():
    """Generate an RSA public/private key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return private_key.public_key(), private_key


def rsa_encrypt(message: str, public_key) -> str:
    """Encrypt a short message using RSA-OAEP with SHA-256."""
    ciphertext = public_key.encrypt(
        message.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return base64.b64encode(ciphertext).decode("ascii")


def rsa_decrypt(encrypted_b64: str, private_key) -> str:
    """Decrypt RSA-OAEP ciphertext."""
    ciphertext = base64.b64decode(encrypted_b64, validate=True)

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext.decode("utf-8")


def main():
    print("=" * 48)
    print("       CRYPTOGRAPHY BASICS: AES & RSA")
    print("=" * 48)

    message = input("Enter a short message to encrypt: ")

    print("\n--- AES-256-GCM ---")
    aes_key, aes_ciphertext = aes_encrypt(message)
    print("AES key: [REDACTED]")
    print("Encrypted data: [REDACTED]")
    print("Decrypted message:", aes_decrypt(aes_key, aes_ciphertext))

    print("\n--- RSA-OAEP with SHA-256 ---")
    public_key, private_key = generate_rsa_keys()
    rsa_ciphertext = rsa_encrypt(message, public_key)
    print("Encrypted data: [REDACTED]")
    print("Decrypted message:", rsa_decrypt(rsa_ciphertext, private_key))

    print("\nAES and RSA demonstrations completed successfully.")


if __name__ == "__main__":
    main()
