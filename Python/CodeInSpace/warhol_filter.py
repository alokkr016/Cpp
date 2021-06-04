"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import Pixel, SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here
    
    return patch

def make_patch(image):
   
    original_width = image.width
    original_height = image.height
    final = SimpleImage.blank(WIDTH, HEIGHT)
    for x in range(original_width):
        for y in range(original_height):
            pixel = image.get_pixel(x,y)
            final.set_pixel(x,y,pixel)

            final.set_pixel(x+PATCH_SIZE,y,pixel)
            final.set_pixel(x + 2*PATCH_SIZE,y,pixel)
            final.set_pixel(x,y + PATCH_SIZE,pixel)
            final.set_pixel(x+PATCH_SIZE,y + PATCH_SIZE,pixel)
            final.set_pixel(x + 2*PATCH_SIZE,y + PATCH_SIZE,pixel)
            
    return final

def red_channel(filename):
    """
    Reads image from file specified by filename.
    Changes the image as follows:
    For every pixel, set green and blue values to 0
    yielding the red channel.
    Return the changed image.
    """
    image = filename
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image

def main():
    original =SimpleImage(PATCH_NAME)
    modified_image = make_patch(original)
    modified_image.show()
    coloured_image = red_channel(modified_image)
    coloured_image.show()
    # patch = make_recolored_patch(1.5, 0, 1.5)
    # final_image.show()

if __name__ == '__main__':
    main()