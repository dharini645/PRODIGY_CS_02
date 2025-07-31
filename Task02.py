import numpy as np
from PIL import Image

class ImageEncryptionTool:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = np.array(self.image)

    def encrypt(self, value=50):
        """Simple encryption by adding a value to each pixel and clipping the result."""
        self.pixels = np.clip(self.pixels + value, 0, 255).astype(np.uint8)

    def decrypt(self, value=50):
        """Simple decryption by subtracting the same value and clipping."""
        self.pixels = np.clip(self.pixels - value, 0, 255).astype(np.uint8)

    def save_image(self, path):
        """Save the modified image."""
        encrypted_image = Image.fromarray(self.pixels)
        encrypted_image.save(path)

# Example usage
image_path = r"F:\jobs backup 25\JOB\Internship\Skillcraft\image2.jpeg"  # Correct image path
tool = ImageEncryptionTool(image_path)

# Encrypt and save
tool.encrypt(value=50)
tool.save_image("encrypted_image.png")

# Decrypt and save
tool.decrypt(value=50)
tool.save_image("decrypted_image.png")
