from PIL import Image, ImageFont, ImageDraw
import os

font = ImageFont.truetype(os.path.dirname(__file__) + "/daxxhub.otf", 230)

def daxxhub(teks):
    # Create a temporary image and draw object to calculate text size
    temp_img = Image.new("RGB", (1, 1), color=(0, 0, 0))
    temp_draw = ImageDraw.Draw(temp_img)
    
    # Calculate text dimensions using textbbox
    bbox = temp_draw.textbbox((0, 0), teks, font=font)
    text_width = bbox[2] - bbox[0]  # right - left
    text_height = bbox[3] - bbox[1]  # bottom - top

    # Create base image with adjusted size
    img = Image.new("RGB", (text_width + 100, text_height + 100), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Calculate text position for centering
    text_x = (img.width - text_width) // 2
    text_y = (img.height - text_height) // 2
    draw.text((text_x, text_y), teks, fill=(255, 148, 224), font=font)

    # Add border and paste into a larger image
    img2 = Image.new("RGB", (img.width + 400, img.height + 400), color=(0, 0, 0))
    img2.paste(Paste(img), ((img2.width - img.width) // 2, (img2.height - img.height) // 2))

    return img2

def Paste(im):
    # Create bordered image
    new = Image.new("RGB", (im.width + 20, im.height + 20), color=(255, 148, 224))
    new.paste(im, ((new.width - im.width) // 2, (new.height - im.height) // 2))
    return new
