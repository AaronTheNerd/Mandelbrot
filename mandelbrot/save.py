from mandelbrot.configs import Configs
import numpy as np
import time
import cv2
import os

def get_filename(configs: Configs) -> str:
    return f"{int(time.time())}-{configs.image.width}x{configs.image.height}-{configs.color.theme}.png"

def save(configs: Configs, image: np.ndarray) -> None:
    output_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "output", get_filename(configs))
    return cv2.imwrite(output_file_path, image)
