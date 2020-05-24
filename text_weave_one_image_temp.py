import sys
#import colour
from PIL import Image, ImageDraw, ImageFont

# Global parameters
filename = "texts/raven.txt"

# use 7x18 (72ppi) or 15x32 (144-150ppi) or 65x135(300ppi)
pixel_width = 65
pixel_height = 135

# 15 inch wide at 300 ppi = 4500
print_width = 4500
default_colour = (255, 255, 255, 255)
allowable_chars = "abcdefghijklmnopqrstuvwxyz 1234567890,./?;:!@#$%&()[]{}-+=\'"

text_font = ImageFont.truetype('fonts/times.ttf', 80)

class pixel_square(object):
    """ This is a class for each "pixel" element in the final image."""

    tag = 0  # used to store a tag for every instance in the class

    def __init__(self, letter=" ", width=pixel_width, height=pixel_height, temp_colour=default_colour):
        # Note: for some reason the entire list is being passed into letter - using letter[1] is a crude workaround.
        self.letter = letter
        self.width = width
        self.height = height
        self.pixel_colour = temp_colour

        # increments tag for the next instance created so each instance has a unique tag
        self.id = pixel_square.tag
        pixel_square.tag += 1

    def __str__(self):
        return ("letter: " + str(self.letter) + " width: " + str(self.width) + " height: " +
                str(self.height) + " colour: " + str(self.pixel_colour) + " tag: " + str(self.id))

    def set_letter(self, new_letter=""):
        self.letter = new_letter

    def set_width(self, new_width=""):
        self.letter = new_width

    def set_height(self, new_height=""):
        self.letter = new_height

    def set_colour(self, new_colour=""):
        self.letter = new_colour


def char_switcher(char):
    '''
    Case-like structure to convert characters to the paramters needed for each pixel_square object
    '''
    switcher = {
        "a": ["1", pixel_width, pixel_height, (252, 255, 54, 255)],
        "b": ["2", pixel_width, pixel_height, (0, 255, 54, 255)],
        "c": ["3", pixel_width, pixel_height, (34, 255, 255, 255)],
        "d": ["4", pixel_width, pixel_height, (255, 0, 251, 255)],
        "e": ["5", pixel_width, pixel_height, (43, 0, 251, 255)],
        "f": ["6", pixel_width, pixel_height, (253, 0, 0, 255)],
        "g": ["7", pixel_width, pixel_height, (18, 0, 137, 255)],
        "h": ["8", pixel_width, pixel_height, (13, 140, 139, 255)],
        "i": ["9", pixel_width, pixel_height, (0, 101, 15, 255)],
        "j": ["10", pixel_width * 2, pixel_height, (128, 0, 126, 255)],
        "k": ["11", pixel_width * 2, pixel_height, (138, 0, 0, 255)],
        "l": ["12", pixel_width * 2, pixel_height, (127, 128, 22, 255)],
        "m": ["13", pixel_width * 2, pixel_height, (169, 169, 169, 255)],
        "n": ["14", pixel_width * 2, pixel_height, (211, 211, 211, 255)],
        "o": ["15", pixel_width * 2, pixel_height, (0, 0, 0, 255)],
        "p": ["16", pixel_width * 2, pixel_height, (252, 255, 54, 255)],
        "q": ["17", pixel_width * 2, pixel_height, (0, 255, 54, 255)],
        "r": ["18", pixel_width * 2, pixel_height, (34, 255, 255, 255)],
        "s": ["19", pixel_width * 2, pixel_height, (255, 0, 251, 255)],
        "t": ["20", pixel_width * 2, pixel_height, (43, 0, 251, 255)],
        "u": ["21", pixel_width * 2, pixel_height, (253, 0, 0, 255)],
        "v": ["22", pixel_width * 2, pixel_height, (18, 0, 137, 255)],
        "w": ["23", pixel_width * 2, pixel_height, (13, 140, 139, 255)],
        "x": ["24", pixel_width * 2, pixel_height, (0, 101, 15, 255)],
        "y": ["25", pixel_width * 2, pixel_height, (128, 0, 126, 255)],
        "z": ["26", pixel_width * 2, pixel_height, (138, 0, 0, 255)],
        "0": ["000", pixel_width * 3, pixel_height, (253, 0, 0, 255)],
        "1": ["111", pixel_width * 3, pixel_height, (127, 128, 22, 255)],
        "2": ["222", pixel_width * 3, pixel_height, (169, 169, 169, 255)],
        "3": ["333", pixel_width * 3, pixel_height, (211, 211, 211, 255)],
        "4": ["444", pixel_width * 3, pixel_height, (0, 0, 0, 255)],
        "5": ["555", pixel_width * 3, pixel_height, (252, 255, 54, 255)],
        "6": ["666", pixel_width * 3, pixel_height, (0, 255, 54, 255)],
        "7": ["777", pixel_width * 3, pixel_height, (34, 255, 255, 255)],
        "8": ["888", pixel_width * 3, pixel_height, (255, 0, 251, 255)],
        "9": ["999", pixel_width * 3, pixel_height, (43, 0, 251, 255)],
    }
    # Return switched char - if char is not in the list above return a white space
    return switcher.get(char, [" ", pixel_width, pixel_height, (255, 255, 255, 255)])


def text_to_chars(filename):
    '''
    Reads in a text file and return a list with each charater as a separate item

    Parameters:
    filename (string)

    Returns:
    list: where each element is a char from the original text file
    '''

    with open(filename, "r", encoding='utf8') as f:
        text = f.read()
    text = text.lower()

    char_list = ""
    for char in text:
        # All allowable characters, anything else will be removed from the text
        if char in allowable_chars:
            char_list = char_list + char

    return char_list


def text_to_pixels(chars):
    '''
    Creates an pixel_square object for each character in the original text and paces these all in a list called temp_pixels[]

    Parameters:
    chars (list) #the list with each char as a seperate element

    Returns:
    temp_pixels(list of pixel_square objects)

    '''

    temp_pixels = []

    for i in range(len(chars)):
        # Creates temporary list (params) so that the char_switcher list can be broken down into the value required for the
        # initialization of the pixel_square object.
        # (Note: if a list is passed to the object constructor the full list goes to the first parameter of the object.
        params = char_switcher(chars[i])
        temp_pixels.append(pixel_square(params[0], params[1], params[2], params[3]))

    return temp_pixels

def make_image(pixel_list):
    '''
    Take the list of pixel objects and converts it into a prinatble tiff file.

    '''

    # Finds overall width of the linear pixel list
    pixel_list_length = 0

    for i in range(len(pixel_list)):
        pixel_list_length = pixel_list_length + pixel_list[i].width

    # Determines the number of pixel rows in the final image
    num_of_rows = int(pixel_list_length / print_width)

    print_height = num_of_rows * pixel_height

    num_of_columns = int(print_width / pixel_width)

    print("This will make a print " + str(num_of_rows) + " squares high by " + str(num_of_columns) + " squares wide.")
    print("The resolution of the final print will be " + str(print_height) + " pixels high by " + str(print_width) + " pixels wide.")

    # Create a new image with the appropriate dimensions
    weave_img = Image.new('RGBA', (print_width, print_height), default_colour)

    # Makes an image drawing object to elements can be added
    img_draw = ImageDraw.Draw(weave_img)

    start_point_x = 0
    start_point_y = 0

    # Draws rectangles and text on final image
    for i in range(len(pixel_list)):
        end_point_x = start_point_x + pixel_list[i].width
        end_point_y = start_point_y + pixel_list[i].height

        img_draw.rectangle((start_point_x, start_point_y, end_point_x, end_point_y), fill=(pixel_list[i].pixel_colour))

        # Calculates the start point for the text
        text_start_x = start_point_x + pixel_list[i].width / 5
        text_start_y = start_point_y + pixel_list[i].height / 5

        # Could add a conversion to white text if needed

        img_draw.text((text_start_x, text_start_y), pixel_list[i].letter, font=text_font, fill='black')

        # Calculates start points for the next round in the for loop. Resets and incriments y at the end of a row.
        if start_point_x <= print_width:
            start_point_x = end_point_x

        else:
            start_point_x = 0
            start_point_y = end_point_y


    weave_img.save('output_images/weave_test.png')



def main():
    # #test for __str__
    # ps1 = pixel_square("a", 10, 10, 10)
    # print(ps1)

    chars = text_to_chars(filename)
    # #test for text to char
    # for i in range(len(chars)):
    #     print(chars[i])

    # #test for char switcher
    # print(char_switcher("a"))
    # print(char_switcher(chars[3]))


    # params = char_switcher("a")
    # temp = pixel_square(params[0], params[1], params[2], params[3])
    # print("switcher: " + str(char_switcher("a")))
    # print(temp)

    pixels = []
    pixels = text_to_pixels(chars)

    make_image(pixels)

    # # Test to confirm that pixel_square objects were correctly created
    # for j in range(len(pixels)):
    #     print(pixels[j])


if __name__ == '__main__':
    main()
