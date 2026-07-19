from PIL import Image
from tkinter import filedialog, Tk

char_ramp_styles = {
    "detailed": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "short": "@%#*+=-:. ",
    "blocks": "█▓▒░ ",
    "minimalist": "##XXxxx==::--..  ",
    "binary": "10 "
}


def image_to_ascii(image_path, input_width, ramp_style):
    image = Image.open(image_path)
    original_width, original_height = image.size
    aspect_ratio = original_height / original_width
    target_height = int((input_width * aspect_ratio) * 0.5)

    resized_image = image.resize((input_width, target_height))

    grayscaled_image = resized_image.convert("L")

    pixels = grayscaled_image.getdata()
    ascii_str = ""

    ramp_length = len(ramp_style)

    for pixel in pixels:
        index = int((pixel / 255) * (ramp_length - 1))
        ascii_str += ramp_style[index]

    ascii_art_lines = [
        ascii_str[i:i + input_width]
        for i in range(0, len(ascii_str), input_width)
    ]

    return "\n".join(ascii_art_lines)


if __name__ == "__main__":

    root = Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp"),
            ("All files", "*.*")
        ]
    )

    user_ramp = input(
        "Choose your own character ramp style or press Enter to use the default (@%#*+=-:.): "
    ).strip().lower()

    if user_ramp not in char_ramp_styles:
        if user_ramp == "":
            ramp_style = char_ramp_styles["short"]
        else:
            print("Invalid ramp style. Using default.")
            ramp_style = char_ramp_styles["short"]
    else:
        ramp_style = char_ramp_styles[user_ramp]

    width = input("Enter the desired width of the ASCII art: ")
    if width.isdigit():
        input_width = int(width)
    else:
        print("Invalid width. Using default width of 100.")
        input_width = 100

    ascii_art = image_to_ascii(image_path, input_width, ramp_style)
    print(ascii_art)