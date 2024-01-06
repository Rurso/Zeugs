from PIL import Image

def image_to_ascii(image_path, output_width, ascii_chars):
    img = Image.open(image_path).convert('RGB')
    aspect_ratio = img.height / img.width
    output_height = int(output_width * aspect_ratio)
    img = img.resize((output_width, output_height))
    pixels = list(img.getdata())
    scale_factor = len(ascii_chars) / 256
    ascii_str = ''
    for pixel_value in pixels:
        grayscale_value = int(0.2989 * pixel_value[0] + 0.587 * pixel_value[1] + 0.114 * pixel_value[2])
        ascii_index = int(grayscale_value * scale_factor)
        ascii_str += ascii_chars[ascii_index]

    lines = [ascii_str[i:i + output_width] for i in range(0, len(ascii_str), output_width)]
    ascii_art = '\n'.join(lines)

    return ascii_art

def main():
    print("Made by einstellung, requested by akmarfu\n")

    image_path = input("Enter the path to the image: ")
    output_width = int(input("Enter the desired width of the output: "))
    ascii_chars = input("Enter the characters to use for ASCII art (e.g., '@%#*+=-:. '): ")

    ascii_art = image_to_ascii(image_path, output_width, ascii_chars)

    print('\nSuccessfully generated ASCII art and saved it as "Image_to_ASCII_Output.txt"\n')
    with open("Image_to_ASCII_Output.txt", "w", encoding="utf-8") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    main()
