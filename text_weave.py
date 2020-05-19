import sys
import colour
import PIL

# Global parameters
filename = "texts/raven.txt"
pixel_width = 10
pixel_height = 20
default_colour = (255, 255, 255)
allowable_chars = "abcdefghijklmnopqrstuvwxyz 1234567890,./?;:!@#$%&()[]{}-+=\'"


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
        # Creates temporary list (params) so that the chars_witcher list can be broken down into the value required for the
        # initialization of the pixel_square object.
        # (Note: if a list is passed to the object constructor the full list goes to the first parameter of the object.
        params = char_switcher(chars[i])
        temp_pixels.append(pixel_square(params[0], params[1], params[2], params[3]))

    return temp_pixels


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

    # Test to confirm that pixel_square objects were correctly created
    for j in range(len(pixels)):
        print(pixels[j])


if __name__ == '__main__':
    main()
