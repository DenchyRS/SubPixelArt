from PIL import Image

input_path = r""
output_path = r""

def convert_image(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert("RGBA") # Convert image to supported format. Might add an option to select a colour to ignore or perceive as transparency so images that don't have transparency can be used

    input_width, input_height = image.size # Get image dimensions

    new_width = (input_width + 2) // 3 # Since we are using sub pixels. The input width will be divided by 3 and rounded up to the nearest whole to ensure that images that aren't perfectly divisible by 3 still work
    
    new_pixels = []

    for y in range(input_height):
        for x in range(0, input_width, 3): # Process the clusters

            rgb = [0, 0, 0] 

            for row in range(3):
                if x + row < input_width: # Don't go out of bounds
                    r, g, b, a = image.getpixel((x + row, y)) # Get pixel rgba values
                    if a != 0: # If pixel is NOT transparent assign it a value of 255
                        rgb[row] = 255

            new_pixels.append(tuple(rgb)) # Append the RGB value to this clusters row

    output = Image.new("RGB", (new_width, input_height))

    for y in range(input_height):
         for x in range(new_width): # Create the new sub pixel image
            index = x + y * new_width # Get the RGB value for current cluster row
            rgb = new_pixels[index]

            output.putpixel((x, y), rgb) # Actually set the pixels

    output.save(output_path)
    print (f"Image conversion complete. Save as: {output_path}")

convert_image(input_path, output_path)
