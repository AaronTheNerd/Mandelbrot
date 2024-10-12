from mandelbrot.configs import Configs, ImageConfigs
from mandelbrot.bailout import get_bailout_array
from mandelbrot.theme import apply_theme
from mandelbrot.save import save
import numpy as np


def draw(configs: Configs) -> None:
    bailout_array = get_bailout_array(configs)
    image = apply_theme(bailout_array, configs.color.theme, configs)
    save(configs, image)
