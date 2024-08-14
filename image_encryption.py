from Cryptodome.Cipher import ChaCha20
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad
from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Read the image
    image = Image.open(input_path)
    image_data = image.tobytes()

    # Initialize the ChaCha cipher
    cipher = ChaCha20.new(key=key, nonce=get_random_bytes(8))

    # Encrypt the image data
    encrypted_data = cipher.encrypt(pad(image_data, cipher.block_size))

    # Save the encrypted data to a new image file
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
    encrypted_image.save(output_path)

# Example usage:
key = get_random_bytes(32)  # 256-bit key

# Replace "input_image.jpg" with the path to your input image file
encrypt_image("C:\\Users\\avani\\OneDrive\\Desktop\\InfoSec Project\\react-face-auth\\public\\temp-accounts\\374ed1e4-481b-4074-a26e-6137657c6e35\\Avani.jpg", "C:\\Users\\avani\\OneDrive\\Desktop\\InfoSec Project\\react-face-auth\\public\\temp-accounts\\374ed1e4-481b-4074-a26e-6137657c6e35\\Encrypted_Image.jpg", key)