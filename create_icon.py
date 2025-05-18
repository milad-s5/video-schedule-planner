from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # Create a 256x256 image with a white background
    size = 256
    image = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw a simple calendar-like icon
    # Draw a rectangle for the calendar
    draw.rectangle([(20, 20), (size-20, size-20)], outline='black', width=3)
    
    # Draw some lines to represent calendar days
    for i in range(1, 4):
        y = 20 + (size-40) * i // 4
        draw.line([(20, y), (size-20, y)], fill='black', width=2)
    
    for i in range(1, 4):
        x = 20 + (size-40) * i // 4
        draw.line([(x, 20), (x, size-20)], fill='black', width=2)
    
    # Save as both .ico and .png
    image.save('icon.ico')
    image.save('icon.png')
    print("Icons created successfully!")

if __name__ == '__main__':
    create_icon() 