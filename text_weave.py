#import sys
from PIL import Image, ImageDraw, ImageFont

# Global parameters
filename = "texts/Raven.txt"
savename = "Raven"
imagetype = ".png"

# use 7x18 (72ppi) or 15x32 (144-150ppi) or 65x135(300ppi)
pixel_width = 65
pixel_height = 135

# 15 inch wide at 300 ppi = 4500
# 44 inches wide at 300 ppi = 13200
# 40" * 40" print = 12000 * 12000
print_width = 12000
default_colour = (255, 255, 255)
allowable_chars = "abcdefghijklmnopqrstuvwxyz 1234567890,./?;:!@#$%&()[]{}-+=\'"

text_font = ImageFont.truetype('fonts/times.ttf', 80)

# Maximum height for outputted image in pixels
max_image_height = 12000


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
        "a": ["1", pixel_width, pixel_height, (252, 255, 54)],
        "b": ["2", pixel_width, pixel_height, (0, 255, 54)],
        "c": ["3", pixel_width, pixel_height, (34, 255, 255)],
        "d": ["4", pixel_width, pixel_height, (255, 0, 251)],
        "e": ["5", pixel_width, pixel_height, (43, 0, 251)],
        "f": ["6", pixel_width, pixel_height, (253, 0, 0)],
        "g": ["7", pixel_width, pixel_height, (18, 0, 137)],
        "h": ["8", pixel_width, pixel_height, (13, 140, 139)],
        "i": ["9", pixel_width, pixel_height, (0, 101, 15)],
        "j": ["10", pixel_width * 2, pixel_height, (128, 0, 126)],
        "k": ["11", pixel_width * 2, pixel_height, (138, 0, 0)],
        "l": ["12", pixel_width * 2, pixel_height, (127, 128, 22)],
        "m": ["13", pixel_width * 2, pixel_height, (169, 169, 169)],
        "n": ["14", pixel_width * 2, pixel_height, (211, 211, 211)],
        "o": ["15", pixel_width * 2, pixel_height, (0, 0, 0)],
        "p": ["16", pixel_width * 2, pixel_height, (252, 255, 54)],
        "q": ["17", pixel_width * 2, pixel_height, (0, 255, 54)],
        "r": ["18", pixel_width * 2, pixel_height, (34, 255, 255)],
        "s": ["19", pixel_width * 2, pixel_height, (255, 0, 251)],
        "t": ["20", pixel_width * 2, pixel_height, (43, 0, 251)],
        "u": ["21", pixel_width * 2, pixel_height, (253, 0, 0)],
        "v": ["22", pixel_width * 2, pixel_height, (18, 0, 137)],
        "w": ["23", pixel_width * 2, pixel_height, (13, 140, 139)],
        "x": ["24", pixel_width * 2, pixel_height, (0, 101, 15)],
        "y": ["25", pixel_width * 2, pixel_height, (128, 0, 126)],
        "z": ["26", pixel_width * 2, pixel_height, (138, 0, 0)],
        "0": ["000", pixel_width * 3, pixel_height, (253, 0, 0)],
        "1": ["111", pixel_width * 3, pixel_height, (127, 128, 22)],
        "2": ["222", pixel_width * 3, pixel_height, (169, 169, 169)],
        "3": ["333", pixel_width * 3, pixel_height, (211, 211, 211)],
        "4": ["444", pixel_width * 3, pixel_height, (0, 0, 0)],
        "5": ["555", pixel_width * 3, pixel_height, (252, 255, 54)],
        "6": ["666", pixel_width * 3, pixel_height, (0, 255, 54)],
        "7": ["777", pixel_width * 3, pixel_height, (34, 255, 255)],
        "8": ["888", pixel_width * 3, pixel_height, (255, 0, 251)],
        "9": ["999", pixel_width * 3, pixel_height, (43, 0, 251)],
    }
    # Return switched char - if char is not in the list above return a white space
    return switcher.get(char, [" ", pixel_width, pixel_height, (255, 255, 255)])


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
        pixel_list_length += pixel_list[i].width

    # Determines the number of pixel rows in the final image
    num_of_rows = int(pixel_list_length / print_width)
    print_height = num_of_rows * pixel_height

    num_of_columns = int(print_width / pixel_width)

    print("This will make a print " + str(num_of_rows) + " squares high by " + str(num_of_columns) + " squares wide.")
    print("The resolution of the final print will be " + str(print_height) + " pixels high by " + str(print_width) + " pixels wide.")


    # Add a mechanism to split the image into parts if required - and create starting parameters
    more_image_parts = True

    pixel_list_start_index = 0
    pixel_list_end_index = 0
    num_of_img_parts = 1
    remaining_print_height = print_height

    while more_image_parts:

        if remaining_print_height > max_image_height:
            pixel_list_end_index += max_image_height

            print("printing...")

            # Creates a smaller partial pixel list that will be used to create the partial image
            partial_pixel_list = pixel_list[pixel_list_start_index:pixel_list_end_index]

            # Creates a new image with the appropriate dimensions
            weave_img = Image.new('RGB', (print_width, max_image_height), default_colour)

            # Makes an image drawing object to elements can be added
            img_draw = ImageDraw.Draw(weave_img)

            start_point_x = 0
            start_point_y = 0

            # Draws rectangles and text on final image
            for i in range(len(partial_pixel_list)):
                end_point_x = start_point_x + partial_pixel_list[i].width
                end_point_y = start_point_y + partial_pixel_list[i].height

                img_draw.rectangle((start_point_x, start_point_y, end_point_x, end_point_y), fill=(partial_pixel_list[i].pixel_colour))

                # Calculates the start point for the text
                text_start_x = start_point_x + partial_pixel_list[i].width / 5
                text_start_y = start_point_y + partial_pixel_list[i].height / 5

                # Could add a conversion to white text if needed

                img_draw.text((text_start_x, text_start_y), partial_pixel_list[i].letter, font=text_font, fill='black')

                # Calculates start points for the next round in the for loop. Resets and incriments y at the end of a row.
                if start_point_x <= print_width:
                    start_point_x = end_point_x

                else:
                    start_point_x = 0
                    start_point_y = end_point_y

            temp_save_name = ("output_images/" + savename + "_" + str(num_of_img_parts))
            weave_img.save(temp_save_name + imagetype)

            pixel_list_start_index = pixel_list_end_index + 1
            num_of_img_parts += 1
            remaining_print_height -= max_image_height

        else:
            # This is the last partial image that will be saved,or the only if it is a small text file.
            more_image_parts = False

            pixel_list_end_index = remaining_print_height

            partial_pixel_list = pixel_list[pixel_list_start_index:pixel_list_end_index]

            # Creates a new image with the appropriate dimensions
            weave_img = Image.new('RGB', (print_width, remaining_print_height), default_colour)

            # Makes an image drawing object to elements can be added
            img_draw = ImageDraw.Draw(weave_img)

            start_point_x = 0
            start_point_y = 0

            # Draws rectangles and text on final image
            for i in range(len(partial_pixel_list)):
                end_point_x = start_point_x + partial_pixel_list[i].width
                end_point_y = start_point_y + partial_pixel_list[i].height

                img_draw.rectangle((start_point_x, start_point_y, end_point_x, end_point_y), fill=(partial_pixel_list[i].pixel_colour))

                # Calculates the start point for the text
                text_start_x = start_point_x + partial_pixel_list[i].width / 5
                text_start_y = start_point_y + partial_pixel_list[i].height / 5

                # Could add a conversion to white text if needed

                img_draw.text((text_start_x, text_start_y), pixel_list[i].letter, font=text_font, fill='black')

                # Calculates start points for the next round in the for loop. Resets and incriments y at the end of a row.
                if start_point_x <= print_width:
                    start_point_x = end_point_x

                else:
                    start_point_x = 0
                    start_point_y = end_point_y

            temp_save_name = ("output_images/" + savename + "_" + str(num_of_img_parts))
            weave_img.save(temp_save_name + imagetype)


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
