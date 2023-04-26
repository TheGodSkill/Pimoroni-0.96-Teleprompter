import ST7735
from PIL import Image, ImageDraw
import time


display = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=90,
    spi_speed_hz=4000000
)


font_size = 5
text_color = (255, 255, 255)


display_width = 160
display_height = 80


words_per_line = 3
words_per_page = 25


x0 = 0
y0 = 0


with open("Script.txt", "r") as f:
    text = f.read().split()


num_pages = (len(text) + words_per_page - 1) // words_per_page


for page_num in range(num_pages):

    start_index = page_num * words_per_page
    end_index = min(start_index + words_per_page, len(text))


    words = text[start_index:end_index]


    num_lines = (len(words) + words_per_line - 1) // words_per_line


    image = Image.new("RGB", (display_width, display_height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, display_width, display_height), fill=(0, 0, 0))


    for line_num in range(num_lines):

        start_index = line_num * words_per_line
        end_index = min(start_index + words_per_line, len(words))


        line_text = " ".join(words[start_index:end_index])


        x = x0
        y = y0 + line_num * font_size * 2


        draw.text((x, y), line_text, font_size=font_size, fill=text_color)


    display.display(image)


    time.sleep(10)
