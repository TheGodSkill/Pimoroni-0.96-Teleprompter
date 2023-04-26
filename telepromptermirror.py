import ST7735
from PIL import Image, ImageDraw, ImageOps
import time


time.sleep(120)

# Initialize the display
display = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=90,
    spi_speed_hz=4000000
)

# Define the font size and text color
font_size = 5
text_color = (255, 255, 255)

# Define the dimensions of the display
display_width = 160
display_height = 80

# Define the maximum number of words per line and per page
words_per_line = 3
words_per_page = 20

# Define the position of the first line of text
x0 = 0
y0 = 0

# Load the text from the script.txt file
with open("/home/brokeskill/RPiFiles/Script.txt", "r") as f:
    text = f.read().split()

# Calculate the number of pages needed to display the entire text
num_pages = (len(text) + words_per_page - 1) // words_per_page

# Loop through the pages
for page_num in range(num_pages):
    # Calculate the start and end indices for the words on this page
    start_index = page_num * words_per_page
    end_index = min(start_index + words_per_page, len(text))

    # Create a list of the words on this page
    words = text[start_index:end_index]

    # Calculate the number of lines needed to display the words on this page
    num_lines = (len(words) + words_per_line - 1) // words_per_line

    # Clear the entire screen
    image = Image.new("RGB", (display_width, display_height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, display_width, display_height), fill=(0, 0, 0))

    # Loop through the lines
    for line_num in range(num_lines):
        # Calculate the start and end indices for the words on this line
        start_index = line_num * words_per_line
        end_index = min(start_index + words_per_line, len(words))

        # Create a string of the words on this line
        line_text = " ".join(words[start_index:end_index])

        # Calculate the position of the line on the display
        x = x0
        y = y0 + line_num * font_size * 2

        # Draw the text on the image
        draw.text((x, y), line_text, font_size=font_size, fill=text_color)

    # Flip the image horizontally
    image = ImageOps.mirror(image)

    # Display the image on the ST7735 display
    display.display(image)

    # Wait for 10 seconds before displaying the next page
    time.sleep(10)
