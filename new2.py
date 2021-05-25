"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # Loop through the new image canvas
    for i in range(N_COLS):
        for j in range(N_ROWS):
            # Create a random patch based on random module
            patch = make_recolored_patch(random.uniform(0, 1.5), random.uniform(0, 1.5), random.uniform(0, 1.5))
            # Add color to the new image based on current position in canvas
            put_patch(final_image, i * PATCH_SIZE, j * PATCH_SIZE, patch)
    final_image.show()

def put_patch(final_image, start_x, start_y, patch):
    # Loop through the patch's x and y values
    for current_x in range(patch.width):
        for current_y in range(patch.height):
            # Get the pixel from patch
            pixel = patch.get_pixel(current_x, current_y)
            # Set it into the final image with the co-ordinates shifted
            final_image.set_pixel(start_x + current_x, start_y + current_y, pixel)
    
    return final_image

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
    # Multiple each channel with the given scale in the function
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch


if __name__ == '__main__':
    main()