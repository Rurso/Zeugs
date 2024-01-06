from PIL import Image

def image_to_ascii(image_path, output_width, ascii_chars):
    # Open the image
    img = Image.open(image_path).convert('L')

    # Calculate aspect ratio
    aspect_ratio = img.height / img.width
    output_height = int(output_width * aspect_ratio)

    # Resize the image
    img = img.resize((output_width, output_height))

    # Convert image to a list of pixel values
    pixels = list(img.getdata())

    # Determine the scaling factor to map pixel values to ASCII characters
    scale_factor = len(ascii_chars) / 256

    # Convert pixel values to ASCII characters
    ascii_str = ''
    for pixel_value in pixels:
        ascii_index = int(pixel_value * scale_factor)
        ascii_str += ascii_chars[ascii_index]

    # Format the ASCII art into lines
    lines = [ascii_str[i:i + output_width] for i in range(0, len(ascii_str), output_width)]
    ascii_art = '\n'.join(lines)

    return ascii_art

def main():
    print("Made by einstellung, requested by akmarfu\n")
    # Get user input
    image_path = input("Enter the path to the black and white image: ")
    output_width = int(input("Enter the desired width of the ASCII art: "))
    ascii_chars = input("Enter the characters to use for ASCII art (e.g., '@%#*+=-:. '): ")

    # Generate ASCII art
    ascii_art = image_to_ascii(image_path, output_width, ascii_chars)

    # Display the result
    print('\nSuccsessfully generated ASCII art and saved it as "Bild zu Ascii Ausgabe.txt"\n')
    with open("Bild zu Ascii Ausgabe.txt", "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    main()
