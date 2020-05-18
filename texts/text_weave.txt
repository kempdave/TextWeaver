import sys
import pygame
import colour
import PIL

# Global parameters
filename = "texts/raven.txt"
pixel_width = 10
pixel_height = 20


class pixel_square(object):
    """ This is a class for each "pixel" element in the final image."""

    tag = 1  # used to store a tag for every instance in the class

    def __init__(self, letter, width, height, colour):
        self.letter = letter
        self.width = width
        self.height = height
        self.colour = colour

        # increments tag for the next instance created so each instance has a unique tag
        self.id = pixel_square.tag
        pixel_square.tag += 1

    def __str__(self):
        return "letter: " + str(self.letter) + " width: " + str(self.width) + " height: " + str(
            self.height) + " colour: " + str(self.colour)

    def set_letter(self, new_letter=""):
        self.letter = new_letter

    def set_width(self, new_width=""):
        self.letter = new_width

    def set_height(self, new_height=""):
        self.letter = new_height

    def set_colour(self, new_colour=""):
        self.letter = new_colour


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
        if char in "abcdefghijklmnopqrstuvwxyz 1234567890":
            char_list = char_list + char

    return char_list


def main():
    print("hello world")

    '''
    #test for __str__
    ps1 = pixel_square("a", 10, 10, 10)
    print(ps1)
    '''

    chars = text_to_chars(filename)
    for i in range(len(chars)):
        print(chars[i])


if __name__ == '__main__':
    main()
