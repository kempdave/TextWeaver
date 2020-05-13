import sys
import pygame
import colour
import PIL

#Global variables
filename = "filename.txt"
pixel_width = 10
pixel_height = 20



class pixel_square(object):
    tag = 1   #used to store a tag for every instance in the class

    def __init__(self, letter, width, height, colour):
        self.letter = letter
        self.width = width
        self.height = height
        self.colour = colour

        #increments tag for the next instance created so each instance has a unique tag
        self.id = pixel_square.tag
        pixel_square.tag +=1

    def __str__(self):
        return "letter:" + str(self.letter) + "width:" + str(self.wdith) + "height" + str(self.height) + "colour" + str(self.colour)

    def set_letter(self, new_letter=""):
        self.letter = new_letter

    def set_width(self, new_width=""):
        self.letter = new_width

    def set_height(self, new_height=""):
        self.letter = new_height

    def set_colour(self, new_colour=""):
        self.letter = new_colour





def hello_world():
    print('hello world')


def default():
    print('running normally')


def main():
    print('hello world')

    #test for __str__
    ps1 = pixel_square("a", 10, 10, 10)
    print(ps1)


if __name__ == '__main__':
    main()
