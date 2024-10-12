from numpy._core.multiarray import array as array
from mandelbrot.configs import Configs, ImageConfigs
from mandelbrot.themes import get_theme
import numpy as np

def blank_image(configs: ImageConfigs) -> np.ndarray:
    return np.zeros((configs.height, configs.width, 3), np.uint8)

def apply_theme(bailout_array: np.ndarray, theme_str: str, configs: Configs) -> np.ndarray:
    image = blank_image(configs.image)
    theme = get_theme(theme_str, configs)
    for y in range(configs.image.height):
        for x in range(configs.image.width):
            color = theme.get_pixel_color(bailout_array[y, x])
            image[y, x, 0] = color[2]
            image[y, x, 1] = color[1]
            image[y, x, 2] = color[0]
    return image
