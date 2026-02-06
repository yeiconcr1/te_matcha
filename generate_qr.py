import qrcode
from PIL import Image

# Data and Paths
data = "https://te-matcha.vercel.app/"
logo_path = "public/logo-removebg-preview.png"
output_path = "public/qr-code.png"
brand_color = "#4A6741" # Matcha Green

# 1. Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=2,
)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color=brand_color, back_color="white").convert('RGBA')

# 2. Load Logo
try:
    logo = Image.open(logo_path)
    # Resize logo to match QR width (with some padding)
    target_logo_width = int(qr_img.size[0] * 0.6) # Logo 60% of QR width
    ratio = target_logo_width / logo.size[0]
    target_logo_height = int(logo.size[1] * ratio)
    logo = logo.resize((target_logo_width, target_logo_height), Image.Resampling.LANCZOS)
    
    # 3. Create Composite Image
    # Height = Logo Height + Padding + QR Height
    padding = 40
    total_height = target_logo_height + padding + qr_img.size[1]
    total_width = max(qr_img.size[0], logo.size[0] + padding) # Ensure enough width
    
    # Create white canvas
    composite = Image.new('RGBA', (total_width, total_height), 'white')
    
    # Paste Logo (Centered at top)
    logo_x = (total_width - logo.size[0]) // 2
    logo_y = 20 # Top padding
    composite.paste(logo, (logo_x, logo_y), mask=logo if logo.mode == 'RGBA' else None)
    
    # Paste QR (Centered below logo)
    qr_x = (total_width - qr_img.size[0]) // 2
    qr_y = logo_y + logo.size[1] + 20 # Padding between logo and QR
    composite.paste(qr_img, (qr_x, qr_y))
    
    # Save
    composite.save(output_path)
    print(f"QR Code with Logo header generated: {output_path}")
    
except Exception as e:
    print(f"Error adding logo: {e}")
    # Fallback to just QR
    qr_img.save(output_path)
