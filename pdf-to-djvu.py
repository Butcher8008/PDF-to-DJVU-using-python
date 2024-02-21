import os
import subprocess

def pdf_to_djvu(input_file, output_file):
    pdf2djvu_path = r"C:\\Users\\Increase-Rev\\Desktop\\PDF to DJVU\\pdf2djvugui.exe"  # Specify the full path to pdf2djvu executable
    try:
        subprocess.run([pdf2djvu_path, input_file, "-o", output_file], check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")

# Constructing the input and output file paths
input_file = os.path.join(os.getcwd(), "input.pdf")
output_file = os.path.join(os.getcwd(), "output.djvu")

# Convert PDF to DjVu
pdf_to_djvu(input_file, output_file)
