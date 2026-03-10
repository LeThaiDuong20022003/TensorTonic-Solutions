def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    result = []

    for row in image:
        gray_row = []
        for pixel in row:
            R, G, B = pixel
            Y = 0.299 * R + 0.587 * G + 0.114 * B
            gray_row.append(Y)
        result.append(gray_row)
    return result            