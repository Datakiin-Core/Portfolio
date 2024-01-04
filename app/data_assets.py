""" Menu Links DataClass """

from dataclasses import dataclass

@dataclass
class ImageAsset:
    """ IMAGE DATACLASS """
    name: str
    file_path: str

@dataclass
class MenuAsset:
    """ IMAGE DATACLASS """
    name: str
    links: str

# Example Usage
image1 = ImageAsset(name="Image1", file_path="/path/to/image1.png")
image2 = ImageAsset(name="Image2", file_path="/path/to/image2.jpg")

# Accessing the file path
print(image1.file_path)  # Outputs: /path/to/image1.png
