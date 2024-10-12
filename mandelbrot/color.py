import numpy as np

from mandelbrot.blender import get_blender
from mandelbrot.colormaps import get_colormap
from mandelbrot.configs import Configs, ImageConfigs


def blank_image(configs: ImageConfigs) -> np.ndarray:
    return np.zeros((configs.height, configs.width, 3), np.uint8)


def apply_color(bailout_array: np.ndarray, configs: Configs) -> np.ndarray:
    image = blank_image(configs.image)
    colormap = get_colormap(configs.color.colormap)
    blender = get_blender(configs.color.blender, configs, colormap)
    for y in range(configs.image.height):
        for x in range(configs.image.width):
            color = blender.get_pixel_color(bailout_array[y, x])
            image[y, x, 0] = color[2]
            image[y, x, 1] = color[1]
            image[y, x, 2] = color[0]
    return image
