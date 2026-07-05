from PIL import Image, ImageDraw

width, height = 900, 600
img = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(img)

# German flag stripes: black, red, gold
draw.rectangle([0, 0, width, height // 3], fill=(0, 0, 0))
draw.rectangle([0, height // 3, width, (2 * height) // 3], fill=(221, 0, 0))
draw.rectangle([0, (2 * height) // 3, width, height], fill=(255, 206, 0))

img.save("static/Germany.png")
print("Created static/Germany.png")