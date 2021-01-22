# import sys
from PIL import Image, ImageDraw, ImageFont

# Global parameters
text_filename = "texts/History_of_Art_Janson_SPACES_short.txt"
save_name = "Janson"
image_type = ".png"

# Shaheer's Pixel are 15 x 32 (at 72 ppi)
# use 7x18 (72ppi) or 15x32 (144-150ppi) or 65x135(300ppi)
# 80pt text works well with 65x135
# 60pt text works well with 45x80
# 50pt text works well with
pixel_width = 36
pixel_height = 72

# 12 inch wide at 300 ppi = 3600
# 15 inch wide at 300 ppi = 4500
# 44 inches wide at 300 ppi = 13200
# 40" * 40" print = 12000 * 12000
print_width = 3600

# Maximum height for outputted image in pixels
max_image_height = 3600


default_colour = (255, 255, 255)
# allowable_chars = "abcdefghijklmnopqrstuvwxyz 1234567890,./?;:!@#$%&()[]{}-+=\' \n"  #\n = escape character for newline
allowable_chars = "abcdefghijklmnopqrstuvwxyz 1234567890,./?;:!@#$%&()[]{}-+=\'"

# Outputs to 72ppi, so must scale up for 300ppi
# 19.2pt = 80pt
# 14pt = 60pt
# 12pt = 50pt
text_font = ImageFont.truetype('fonts/times.ttf', 50)

# Margins values for text within each pixel
# e.g 0.2 = 20% which means 20 percent of the over pixel_height would be left as a margin for the text
# This may need to be adjusted as different font sizes are used
# 60 pt text works well with - text_left_margin_percent = 0.18,  text_top_margin_percent = 0.10
# 50 pt text works well with - text_left_margin_percent = 0.18,  text_top_margin_percent = 0.12
text_left_margin_percent = 0.18
text_top_margin_percent = 0.12


class PixelSquare(object):
    """ This is a class for each "pixel" element in the final image."""

    tag = 0  # used to store a tag for every instance in the class

    def __init__(self, letter=" ", width=pixel_width, height=pixel_height, temp_colour=default_colour):
        # Note: for some reason the entire list is being passed into letter - using letter[1] is a crude workaround.
        self.letter = letter
        self.width = width
        self.height = height
        self.pixel_colour = temp_colour

        # increments tag for the next instance created so each instance has a unique tag
        self.id = PixelSquare.tag
        PixelSquare.tag += 1

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
    """
    Case-like structure to convert characters to the parameters needed for each PixelSquare object
    """

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
        # "\n": [" ", print_width, pixel_height, (255, 255, 255)],
        # "\n": ["*", print_width, pixel_height, (255, 255, 255)],
    }

    # Return switched char - if char is not in the list above return a white space
    return switcher.get(char, [" ", pixel_width, pixel_height, (255, 255, 255)])


def text_to_chars(filename):
    """
    Reads in a text file and return a list with each character as a separate item

    Parameters:
    filename (string)

    Returns:
    list: where each element is a char from the original text file
    """

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
    """
    Creates an PixelSquare object for each character in the original text and paces these all in a list
    called temp_pixels[]

    Parameters:
    chars (list) #the list with each char as a separate element

    Returns:
    temp_pixels(list of PixelSquare objects)

    """

    temp_pixels = []

    for i in range(len(chars)):
        # Creates temporary list (params) so that the char_switcher list can be broken down into the value required
        # for the initialization of the PixelSquare object.
        # (Note: if a list is passed to the object constructor the full list goes to the first parameter of the object.
        params = char_switcher(chars[i])

        temp_pixels.append(PixelSquare(params[0], params[1], params[2], params[3]))

    return temp_pixels


def make_image(pixel_list):
    """
    Take the list of pixel objects and converts it into a printable tiff file.

    """

    # Finds overall width of the linear pixel list
    pixel_list_length = 0

    for i in range(len(pixel_list)):
        pixel_list_length += pixel_list[i].width

    # Determines the number of pixel rows in the final image
    num_of_rows = int(pixel_list_length / print_width)
    print_height = num_of_rows * pixel_height

    num_of_columns = int(print_width / pixel_width)

    # Determine the absolute line length for each page on a pixel basis
    max_line_length_per_page = print_width * (max_image_height / pixel_height)


    print("This will make a print " + str(num_of_rows) + " squares high by " + str(num_of_columns) + " squares wide.")
    print("The overall number of pixel squares will be " + str(int(pixel_list_length/pixel_width)))
    print("The resolution of the final print will be " + str(print_height) + " pixels high by " + str(print_width) +
          " pixels wide.")

    # Add a mechanism to split the image into parts if required - and create starting parameters
    more_image_parts = True

    pixel_list_start_index = 0
    pixel_list_end_index = 0
    num_of_img_parts = 1
    remaining_print_height = print_height

    while more_image_parts:

        if remaining_print_height > max_image_height:

            # Here is the problem pixel_list_end_index is based on the characters - max_image_height is based in pixels
            # pixel_list_end_index += max_image_height

            # Determines the pixel_list_end_index for the partial list end index base on pixel in order to
            # accommodate characters that are longer than 1 "square"wide
            temp_line_length_per_page = 0
            temp_pixel_list_start_index = pixel_list_start_index

            while temp_line_length_per_page <= max_line_length_per_page:
                print ("templinelength = " + str(temp_line_length_per_page))
                print (pixel_list[temp_pixel_list_start_index])
                temp_line_length_per_page += pixel_list[temp_pixel_list_start_index].width
                temp_pixel_list_start_index += 1
                pixel_list_end_index += 1

            # for j in range(len(pixels)):
            #     print("templinelength = " + str(temp_line_length_per_page))
            #     print (pixel_list[temp_pixel_list_start_index])
            #     temp_line_length_per_page += pixel_list[temp_pixel_list_start_index].width
            #     temp_pixel_list_start_index += 1
            #     pixel_list_end_index += 1

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

                # Detects if the end point will run over a row in which case it will start on a new row
                if end_point_x > print_width:
                    start_point_x = 0
                    end_point_x = start_point_x + partial_pixel_list[i].width
                    start_point_y = end_point_y

                img_draw.rectangle((start_point_x, start_point_y, end_point_x, end_point_y),
                                   fill=partial_pixel_list[i].pixel_colour)

                # Calculates the start point for the text
                text_start_x = start_point_x + partial_pixel_list[i].width * text_left_margin_percent
                text_start_y = start_point_y + partial_pixel_list[i].height * text_top_margin_percent

                # Could add a conversion to white text if needed

                img_draw.text((text_start_x, text_start_y), partial_pixel_list[i].letter, font=text_font, fill='black')

                # Calculates start points for the next round in the for loop. Resets and increments y at the
                # end of a row.
                # if end_point_x <= print_width:
                #     start_point_x = end_point_x

                start_point_x = end_point_x


                # else:
                #     start_point_x = 0
                #     start_point_y = end_point_y

            temp_save_name = ("output_images/" + save_name + "_" + str(num_of_img_parts))
            weave_img.save(temp_save_name + image_type)

            pixel_list_start_index = pixel_list_end_index + 1
            num_of_img_parts += 1
            remaining_print_height -= max_image_height

        else:
            # This is the last partial image that will be saved,or the only if it is a small text file.
            more_image_parts = False

            # Take the remaining pixel square entries in the list - [x:y] between x and and y -- [x:] x until end
            partial_pixel_list = pixel_list[pixel_list_start_index:-1]

            for j in range(len(partial_pixel_list)):
                print(partial_pixel_list[j])


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

                # Detects if the end point will run over a row in which case it will start on a new row
                if end_point_x > print_width:
                    start_point_x = 0
                    end_point_x = start_point_x + partial_pixel_list[i].width
                    start_point_y = end_point_y

                img_draw.rectangle((start_point_x, start_point_y, end_point_x, end_point_y),
                                   fill=partial_pixel_list[i].pixel_colour)

                # Calculates the start point for the text
                text_start_x = start_point_x + partial_pixel_list[i].width * text_left_margin_percent
                text_start_y = start_point_y + partial_pixel_list[i].height * text_top_margin_percent

                # Could add a conversion to white text if needed

                img_draw.text((text_start_x, text_start_y), partial_pixel_list[i].letter, font=text_font, fill='black')

                # Calculates start points for the next round in the for loop. Resets and increments y at the
                # end of a row.
                # if end_point_x <= print_width:
                #     start_point_x = end_point_x

                start_point_x = end_point_x

            temp_save_name = ("output_images/" + save_name + "_" + str(num_of_img_parts))
            weave_img.save(temp_save_name + image_type)


def main():
    # #test for __str__
    # ps1 = PixelSquare("a", 10, 10, 10)
    # print(ps1)

    chars = text_to_chars(text_filename)
    # #test for text to char
    # for i in range(len(chars)):
    #     print(chars[i])

    # #test for char switcher
    # print(char_switcher("a"))
    # print(char_switcher(chars[3]))

    # params = char_switcher("a")
    # temp = PixelSquare(params[0], params[1], params[2], params[3])
    # print("switcher: " + str(char_switcher("a")))
    # print(temp)

    pixels = []
    pixels = text_to_pixels(chars)

    make_image(pixels)

    # Test to confirm that PixelSquare objects were correctly created
    # for j in range(len(pixels)):
    #    print(pixels[j])


if __name__ == '__main__':
    main()
