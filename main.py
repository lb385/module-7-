import qrcode
import argparse
import os

if not os.path.exists('qr_codes'):
    os.makedirs('qr_codes')

parser = argparse.ArgumentParser(description='Generate QR code for a URL')
parser.add_argument('--url', required=True, help='The URL to encode in the QR code')
args = parser.parse_args()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(args.url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qr_codes/qr_code.png')

print(f"QR code generated for {args.url} and saved to qr_codes/qr_code.png")