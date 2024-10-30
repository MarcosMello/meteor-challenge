from PIL import Image

image = Image.open('meteor_challenge_01.png')
image = image.convert('RGB')

is_water = [0] * image.width
is_star = [0] * image.width
is_meteor = [0] * image.width

stars = 0
meteors = 0
meteors_into_water = 0

for y in range(image.height - 1, -1, -1):
    for x in range(image.width):
        R, G, B = image.getpixel((x, y))

        if R == 0 and G == 0 and B == 255:
            is_water[x] = 1
        elif R == 255 and G == 0 and B == 0:
            meteors += 1
            meteors_into_water += is_water[x]

            is_meteor[x] = 1
        elif R == 255 and G == 255 and B == 255:
            stars += 1

            is_star[x] = 1

print(f"Stars: {stars}")
print(f"Meteors: {meteors}")
print(f"Meteors falling into water: {meteors_into_water}")
print(f"Hidden Phrase: ", end="")

is_celestial_body = is_star + is_meteor

for index in range(0, len(is_celestial_body), 8):
    byte = "".join([str(i) for i in is_celestial_body[index:(index + 8)]])
    print(chr(int(byte, 2)), end="")
