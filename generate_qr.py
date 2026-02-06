import qrcode
from PIL import Image, ImageDraw

# Data and Paths
data = "https://te-matcha.vercel.app/"
logo_path = "public/logo-removebg-preview.png"
output_path = "public/qr-code.png"
brand_color = "#4A6741" # Matcha Green

# 1. Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High EC to support covering data
    box_size=12,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color=brand_color, back_color="white").convert('RGBA')

# 2. Load and Prepare Logo
try:
    logo = Image.open(logo_path)
    
    # Calculate logo size (Increased to ~40% for better visibility)
    target_logo_width = int(img.size[0] * 0.40) 
    
    ratio = target_logo_width / logo.size[0]
    target_logo_height = int(logo.size[1] * ratio)
    logo = logo.resize((target_logo_width, target_logo_height), Image.Resampling.LANCZOS)
    
    # 3. Paste Logo in Center
    pos_x = (img.size[0] - logo.size[0]) // 2
    pos_y = (img.size[1] - logo.size[1]) // 2
    
    # Create a white background for the logo ("sin qr encima")
    # This prevents QR dots from showing through transparent parts of the logo
    bg_w, bg_h = logo.size
    # Add a small padding for the white box
    padding = 6
    white_bg = Image.new('RGBA', (bg_w + padding*2, bg_h + padding*2), 'white')
    
    # Paste white box first (centered)
    bg_pos_x = pos_x - padding
    bg_pos_y = pos_y - padding
    img.paste(white_bg, (bg_pos_x, bg_pos_y))
    
    # Paste logo on top of white box
    img.paste(logo, (pos_x, pos_y), mask=logo if logo.mode == 'RGBA' else None)
    
    # Save
    img.save(output_path)
    print(f"Centered Corporate QR Code generated: {output_path}")
    
except Exception as e:
    print(f"Error adding logo: {e}")
    # Fallback to just QR
    img.save(output_path)
