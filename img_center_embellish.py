from skimage.io import imread, imsave, imshow


def paint_central_rectangle(in_file, out_file, color, size):
    """
    The function draws a rectangle in the center of the image and writes a new image to a file.
    The dimensions of the input image and the rectangle must be odd.
    Input format: size - list (the size of the rectangle),
    in_file, out_file - string (image file names), color - list (color in rgb format)
    """
    img = imread(in_file).copy()
    x, y, _ = (i//2 for i in img.shape)
    x_delta, y_delta = (i//2 for i in size)
    img[x - x_delta:x + x_delta +1, y - y_delta:y + y_delta +1] = color
    imsave(out_file, img)
    
if __name__ == "__main__":
    color, size = [255, 192, 203], [7, 15]
    in_file, out_file = "img.png", "out_img.png"