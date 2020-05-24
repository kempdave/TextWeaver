from PIL import Image

daveIm = Image.open("Davey Face.jpg")

dave2Im = daveIm

dave2Im.save('davey2.jpg')

# Create a new image with the appropriate dimensions - 13200 = 300ppi 44inch wide print
test_img = Image.new('RGBA', (13200, 25000), 'white')

test_img.save('test.tif')
