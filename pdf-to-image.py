import argparse
import os

import fitz  # PyMuPDF

# use the argument parser to obtain the filename
parser = argparse.ArgumentParser(description='Convert a PDF into images')
parser.add_argument('pdf_file', help='PDF file to convert')
args = parser.parse_args()

pdf_file = args.pdf_file
if not os.path.isfile(pdf_file) or not pdf_file.lower().endswith('.pdf'):
    print("Invalid PDF file provided.")
    exit(1)

pdf_filename = os.path.splitext(os.path.basename(pdf_file))[0]
image_folder = f'{pdf_filename}_images/'

os.makedirs(image_folder, exist_ok=True)

pdf_document = fitz.open(pdf_file)

for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    
    image = page.get_pixmap()
    
    image.save(f"{image_folder}page_{page_number + 1}.png")

pdf_document.close()

print(f"PDF pages converted to images and saved in '{image_folder}'")

