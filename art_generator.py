from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import random

def pixelate(image, pixel_size=10):
    """Pixelates the image by resizing it to a smaller size and back."""
    small = image.resize(
        (image.width // pixel_size, image.height // pixel_size), Image.NEAREST
    )
    return small.resize(image.size, Image.NEAREST)

def color_quantization(image, num_colors=8):
    """Reduces the number of colors in the image for an abstract effect."""
    image = image.convert("P", palette=Image.ADAPTIVE, colors=num_colors)
    return image.convert("RGB")

def extract_palette(image, num_colors=8):
    """Extracts a palette of colors from the input image."""
    image = image.convert("P", palette=Image.ADAPTIVE, colors=num_colors)
    palette = image.getpalette()[:num_colors * 3]  # Extract RGB values
    colors = [tuple(palette[i:i+3]) for i in range(0, len(palette), 3)]
    return colors

def add_random_shapes(image, palette, num_shapes=30):
    """Adds random shapes to the image using colors from the palette."""
    draw = ImageDraw.Draw(image)
    for _ in range(num_shapes):
        # Random shape type: circle or rectangle
        shape_type = random.choice(["circle", "rectangle"])

        # Generate random coordinates
        x1, y1 = random.randint(0, image.width), random.randint(0, image.height)
        x2, y2 = random.randint(0, image.width), random.randint(0, image.height)

        # Ensure coordinates are in the correct order
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        # Pick a random color from the palette
        color = random.choice(palette)

        if shape_type == "circle":
            draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
        else:
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
    return image

def generate_abstract_art(input_path, output_path):
    """Creates an abstract art image from an input image."""
    image = Image.open(input_path)
    image = image.resize((300, 300))  # Resize for consistent processing

    # Extract the color palette from the input image
    palette = extract_palette(image, num_colors=8)

    # Apply filters
    image = pixelate(image, pixel_size=15)  # Add pixelation
    image = color_quantization(image, num_colors=6)  # Reduce colors
    image = add_random_shapes(image, palette, num_shapes=50)  # Add random shapes

    # Save and display
    image.save(output_path)
    print(f"Abstract art generated and saved as {output_path}")

# Provide input and output paths
input_image_path = r"C:\Users\irene\Desktop\example4.jpg"  # Replace with your image path
output_image_path = r"C:\Users\irene\Desktop\abstract_art4.png"  # Replace with desired output path

generate_abstract_art(input_image_path, output_image_path)






