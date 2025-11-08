from PIL import Image, ImageDraw, ImageFont
import os

# Create a 1024x1024 icon (standard size for app icons)
size = 1024
icon = Image.new('RGB', (size, size), color='#2196F3')  # Blue background

# Draw a simple "M" for Menu
draw = ImageDraw.Draw(icon)

# Draw a simple shape - a rounded rectangle with "M"
margin = size // 8
inner_size = size - 2 * margin

# Draw white circle
circle_bbox = [margin, margin, size - margin, size - margin]
draw.ellipse(circle_bbox, fill='white')

# Try to add text
try:
    # Try to use a default font
    font_size = size // 2
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "M"
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - margin // 4
    
    draw.text((text_x, text_y), text, fill='#2196F3', font=font)
except Exception as e:
    print(f"Could not add text: {e}")
    # Draw a simple shape instead
    inner_margin = size // 3
    rect_bbox = [inner_margin, inner_margin, size - inner_margin, size - inner_margin]
    draw.rectangle(rect_bbox, fill='#2196F3')

# Save the icon
output_path = os.path.join('assets', 'icon', 'app_icon.png')
icon.save(output_path, 'PNG')
print(f"Icon created successfully at {output_path}")
