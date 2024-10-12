from mandelbrot.configs import Configs, ImageConfigs
import math

from functools import partial
import numpy as np

def actual_pos(x: int, y: int, configs: Configs) -> complex:
    span_x = configs.mandelbrot.span
    dist_per_pixel = span_x / configs.image.width
    span_y = configs.image.height * dist_per_pixel
    origin_x = configs.mandelbrot.origin[0]
    origin_y = configs.mandelbrot.origin[1]
    return complex(
        origin_x - 0.5 * span_x + x * dist_per_pixel,
        origin_y + 0.5 * span_y - y * dist_per_pixel
    )

def get_starting_array(configs: Configs) -> np.ndarray:
    arr = np.zeros((configs.image.height, configs.image.width), np.complex64)
    for y in range(configs.image.height):
        for x in range(configs.image.width):
            arr[y, x] = actual_pos(x, y, configs)
    return arr

def get_bailout(max_iterations: int, pos: complex) -> float:
    x0 = pos.real
    y0 = pos.imag
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    iteration = 0
    while x2 + y2 <= (1 << 16) and iteration < max_iterations:
        y = 2 * x * y + y0
        x = x2 - y2 + x0
        x2 = x * x
        y2 = y * y
        iteration += 1
    if iteration < max_iterations:
        log_zn = math.log(x2 + y2) / 2
        nu = math.log(log_zn / math.log(2)) / math.log(2)
        iteration = iteration + 1 - nu
    return iteration

def get_bailout_array(configs: Configs) -> np.ndarray:
    bailout_vector = np.vectorize(partial(get_bailout, configs.mandelbrot.max_iterations))
    return bailout_vector(get_starting_array(configs))
