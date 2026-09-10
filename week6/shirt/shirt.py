from PIL import Image, ImageOps
import sys
from os.path import splitext

SHIRT_PATH = "shirt.png"

if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments" if len(sys.argv)<3 else "Too many command-line arguments")

input_path = sys.argv[1].lower()
output_path = sys.argv[2].lower()

if splitext(input_path)[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Input file type not supported")

if splitext(output_path)[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Output file type not supported")

if splitext(input_path)[1] != splitext(output_path)[1]:
    sys.exit("Input and output file types do not match")

try:
    with Image.open(input_path) as before_file, Image.open(SHIRT_PATH) as shirt_image:
        shirt_size = shirt_image.size
        output_image = ImageOps.fit(before_file, shirt_size)
        output_image.paste(shirt_image, shirt_image)
        output_image.save(output_path)

except FileNotFoundError:
    sys.exit("File does not exist")
