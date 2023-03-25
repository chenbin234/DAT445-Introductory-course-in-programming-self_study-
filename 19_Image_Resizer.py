from PIL import Image

image = Image.open('test.jpg')

print(f'Current size:{image.size}')

resized_image = image.resize((250,300))
resized_image.save('resized_test.jpg')