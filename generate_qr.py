import qrcode
from PIL import Image

# Data and Paths
data = "https://te-matcha.vercel.app/"
logo_path = "public/logo-removebg-preview.png"
output_path = "public/qr-code.png"
brand_color = "#4A6741" # Matcha Green

# Create QR Code instance with High Error Correction (to support logo)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12, # Slightly larger for better quality
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create the QR image with brand color
img = qr.make_image(fill_color=brand_color, back_color="white").convert('RGB')

# Load and resize the logo
try:
    logo = Image.open(logo_path)
    
    # Calculate logo size (e.g., 25% of the QR code size)
    logo_size = int(img.size[0] * 0.25)
    logo = logo.resize((logo_size, int(logo_size * logo.size[1] / logo.size[0])), Image.Resampling.LANCZOS)
    
    # Calculate position to center the logo
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    
    # Paste the logo (using itself as mask if transparency exists)
    if logo.mode in ('RGBA', 'LA'):
        img.paste(logo, pos, mask=logo)
    else:
        img.paste(logo, pos)
        
    print("Logo added to QR code.")
except Exception as e:
    print(f"Warning: Could not add logo to QR code: {e}")

# Save the final image
img.save(output_path)
print(f"Corporate QR Code generated successfully: {output_path}")
