
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import base64

# My original message
message = "Hello, this is my message to the computer world!"


# ====================================
# PART 1: SYMMETRIC ENCRYPTION
# ====================================

print("\nPART 1: SYMMETRIC ENCRYPTION")
print("------------------------------------")

# Create a secret key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt the message
encrypted = cipher.encrypt(message.encode())

# Decrypt the message
decrypted = cipher.decrypt(encrypted).decode()

# Display the results
print("Original Message:", message)
print("Secret Key:", key.decode())
print("Encrypted Message:", encrypted.decode())
print("Decrypted Message:", decrypted)
print("Encryption Successful:", decrypted == message)


# ====================================
# PART 2: ASYMMETRIC ENCRYPTION
# ====================================

print("\nPART 2: ASYMMETRIC ENCRYPTION")
print("------------------------------------")

# Create public and private keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Encrypt using the public key
encrypted_message = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt using the private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
).decode()

# Display the original message
print("Original Message:", message)

# Display the public key
print("\nPublic Key:")
print(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode())

# Display the private key
print("Private Key:")
print(private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode())

# Display encrypted and decrypted messages
print("Encrypted Message:")
print(base64.b64encode(encrypted_message).decode())

print("Decrypted Message:", decrypted_message)
print("Encryption Successful:", decrypted_message == message)


# ====================================
# PROGRAM COMPLETE
# ====================================

print("\n------------------------------------")
print("ENCRYPTION PROGRAM COMPLETED!")
print("------------------------------------")
