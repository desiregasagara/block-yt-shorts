from PIL import Image

# Load the original image
original_image_path = "images/icon.png"
original_image = Image.open(original_image_path)

# Define the sizes needed
sizes = [16, 32, 48, 128]
resized_images = {}

# Resize and save each image
for size in sizes:
    resized_image = original_image.resize((size, size), Image.LANCZOS)
    resized_path = f"images/icon-{size}.png"
    resized_image.save(resized_path)
    resized_images[f"{size}x{size}"] = resized_path

resized_images
