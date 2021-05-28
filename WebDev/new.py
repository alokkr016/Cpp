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
    
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def put_patch(final_image, start_x, start_y, patch):
    # Loop through the patch's x and y values
    for current_x in range(patch.width):
        for current_y in range(patch.height):
            # Get the pixel from patch
            pixel = patch.get_pixel(current_x, current_y)
            # Set it into the final image with the co-ordinates shifted
            final_image.set_pixel(start_x + current_x, start_y + current_y, pixel)
def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    put_patch(final_image, 0,0, patch)
    patch = make_recolored_patch(1.0, 1, 0.2)
    put_patch(final_image, PATCH_SIZE, 0, patch)
    
    final_image.show()

if __name__ == '__main__':
    main()