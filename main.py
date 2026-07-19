from PIL import Image
from tkinter import filedialog, Tk

charRampStyles = {
    "detailed": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "short": "@%#*+=-:. ",
    "blocks": "█▓▒░ ",
    "minimalist": "##XXxxx==::--..  ",
    "binary": "10 "
}

def imageToASCII(imagePath, inputWidth, rampStyle):
    image = Image.open(imagePath)
    originalWidth, originalHeight = image.size
    aspectRatio = originalHeight / originalWidth
    targetHeight = int((inputWidth * aspectRatio)*0.5)

    resizedImage = image.resize((inputWidth, targetHeight))

    grayscaledImage = resizedImage.convert("L")

    pixels = grayscaledImage.getdata()
    asciiStr = ""

    rampLength = len(rampStyle)

    for pixel in pixels:
        index = int((pixel/255)*(rampLength-1))
        asciiStr += rampStyle[index]
    
    asciiArtLines = [asciiStr[i:i+inputWidth] for i in range(0, len(asciiStr), inputWidth)]
    
    return "\n".join(asciiArtLines)

if __name__ == "__main__":
    
    root = Tk()
    root.withdraw()

    imagePath = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp"),
            ("All files", "*.*")
        ]
    )

    userRamp = input("Choose your own character ramp style or press Enter to use the default (@%#*+=-:.): ").strip().lower()
    
    if userRamp not in charRampStyles:
        if(userRamp == ""):
            rampStyle = charRampStyles["short"]
        else:
            print("Invalid ramp style. Using default.")
            rampStyle = charRampStyles["short"]
    else:
        rampStyle = charRampStyles[userRamp]

    width = (input("Enter the desired width of the ASCII art: "))
    if width.isdigit():
        inputWidth = int(width)
    else:
        print("Invalid width. Using default width of 100.")
        inputWidth = 100

    asciiArt = imageToASCII(imagePath, inputWidth, rampStyle)
    print(asciiArt)