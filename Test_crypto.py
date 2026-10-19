
import base64
import unittest

from cryptography.exceptions import InvalidTag

from main import (
    aes_encrypt,
    aes_decrypt,
    generate_rsa_keys,
    rsa_encrypt,
    rsa_decrypt,
)


class TestAES(unittest.TestCase):
    def test_round_trip(self):
        message = "Cybersecurity learning project"
        key, encrypted = aes_encrypt(message)

        self.assertEqual(aes_decrypt(key, encrypted), message)

    def test_empty_message(self):
        key, encrypted = aes_encrypt("")
        self.assertEqual(aes_decrypt(key, encrypted), "")

    def test_wrong_key_rejected(self):
        _, encrypted = aes_encrypt("Protected message")
        wrong_key, _ = aes_encrypt("Different message")

        with self.assertRaises(InvalidTag):
            aes_decrypt(wrong_key, encrypted)

    def test_modified_ciphertext_rejected(self):
        key, encrypted = aes_encrypt("Integrity matters")

        payload = bytearray(base64.b64decode(encrypted))
        payload[-1] ^= 1

        modified = base64.b64encode(payload).decode("ascii")

        with self.assertRaises(InvalidTag):
            aes_decrypt(key, modified)


class TestRSA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.public_key, cls.private_key = generate_rsa_keys()

    def test_round_trip(self):
        message = "RSA encryption demo"
        encrypted = rsa_encrypt(message, self.public_key)

        self.assertEqual(
            rsa_decrypt(encrypted, self.private_key),
            message,
        )

    def test_empty_message(self):
        encrypted = rsa_encrypt("", self.public_key)

        self.assertEqual(
            rsa_decrypt(encrypted, self.private_key),
            "",
        )

    def test_wrong_private_key_rejected(self):
        _, another_private_key = generate_rsa_keys()
        encrypted = rsa_encrypt("Private data", self.public_key)

        with self.assertRaises(ValueError):
            rsa_decrypt(encrypted, another_private_key)


if __name__ == "__main__":
    unittest.main()
