import os
import time

import cv2
import numpy as np

from mandelbrot.configs import Configs


def get_filename(configs: Configs) -> str:
    return f"{int(time.time())}-s{configs.mandelbrot.span}-x{configs.mandelbrot.origin[0]}-y{configs.mandelbrot.origin[1]}.png"


def save(configs: Configs, image: np.ndarray) -> None:
    output_file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "..",
        "output",
        get_filename(configs),
    )
    return cv2.imwrite(output_file_path, image)
