from PIL import Image

img = Image.open('pychallenge7.png')

img_width = 629
img_height = 95

output = ''
for i in range(43, 51):
    for j in range(0, 608, 7):
        output += chr(img.getpixel((j, i))[0])

# print(output)

answer_nums = [105, 110, 116, 101, 103, 114, 105, 116, 121]

answer = ''
for i in answer_nums:
    answer += (chr(i))

print(answer)