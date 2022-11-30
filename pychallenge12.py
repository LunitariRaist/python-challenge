from PIL import ImageShow, Image

img = Image.open("C:/Users/sdomi/Documents/Code/PythonChallenge/pychallenge12.jpg")

original_image_pixels = list(img.getdata())
print(len(original_image_pixels))

def get_odds(image_array):
    new_list = []
    for i in range(0, len(image_array), 5):
        # manipulate the RGB of the original image
        # if image_array[i][0] == 5 or image_array[i][1] == 5 or image_array[i][2] == 5:
        new_list.append(image_array[i])
        # else:
            # new_list.append((255, 255, 255))
    return new_list

img_data = get_odds(original_image_pixels)

print(len(img_data))

# for i in range(0, 100):
#     print(img_data[i])

img2 = Image.new('RGB', [640, 480])

img2.putdata(img_data)

ImageShow.show(img2)

# answer: 