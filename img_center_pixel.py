from skimage.io import imread, imsave


def paint_central_pixel(in_file, out_file, color):
    """
    The function changes the color of the central pixel and writes it to a new file.
    The dimensions of the input image must be odd. Input format: 
    in_file, out_file - string (image file names), color - list (color in rgb format)
    """
    img = imread(in_file)
    x, y, _ = (i//2 for i in img.shape)
    img[x, y] = color
    imsave(out_file, img)
    
if __name__ == "__main__":
    color = [102, 204, 102]
    in_file, out_file = "img.png", "out_img.png"
    paint_central_pixel(in_file, out_file, colo