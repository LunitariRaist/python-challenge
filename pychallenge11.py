from PIL import ImageShow, Image

im = Image.open("C:/Users/sdomi/Documents/Code/PythonChallenge/pychallenge11.jpg")
w = 640
h = 480
# ImageShow.show(im)

original_image_pixels = list(im.getdata())
print(len(original_image_pixels))

def get_odds(image_array):
    new_list = []
    for i in range(0, len(image_array), 2):
        new_list.append(image_array[i])
    return new_list

im2 = Image.new('RGB', [640, 480])

print(len(get_odds(original_image_pixels)))

im2.putdata(get_odds(original_image_pixels))

ImageShow.show(im2)

# answer: evil