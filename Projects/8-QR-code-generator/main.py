import os
import qrcode

def generate_qr(folder_path):
    url = input("Enter the URL here: ")
    file_name = input("Enter the file name: ")

    file_name += '.png'

    # Ensure folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Full file path
    full_path = os.path.join(folder_path, file_name)

    # Generate QR
    img = qrcode.make(url)

    # Save image
    img.save(full_path)

    print(f"QR Code saved at: {full_path}")

if __name__ == "__main__":
    target_folder = r"F:/CODE PLAYGROUND/PYTHON/Projects/8-QR-code-generator/QR-Codes/"
    generate_qr(target_folder)
