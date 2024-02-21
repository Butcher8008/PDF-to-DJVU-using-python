import os
import subprocess

def pdf_to_djvu(input_file, output_file):
    try:
        subprocess.run(["pdf2djvu", input_file, output_file], check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")

# Constructing the input and output file paths
input_file = "sample.pdf"
output_file = "output.djvu"

# Convert PDF to DjVu
pdf_to_djvu(input_file, output_file)
