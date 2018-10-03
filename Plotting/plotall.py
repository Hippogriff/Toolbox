from matplotlib import pyplot as plt


def plotall(images: List, cmap="Greys_r"):
    """
    Awesome function to plot figures in list of list fashion.
    Every list inside the list, is assumed to be drawn in one row.
    :param images: List of list containing images
    :param cmap: color map to be used for all images
    :return: List of figures.
    """
    figures = []
    num_rows = len(images)
    for r in range(num_rows):
        cols = len(images[r])
        f, a = plt.subplots(1, cols)
        for c in range(cols):
            a[c].imshow(images[r][c], cmap=cmap)
            a[c].title.set_text("{}".format(c))
            a[c].axis("off")
            a[c].grid("off")
        figures.append(f)
    return figures
