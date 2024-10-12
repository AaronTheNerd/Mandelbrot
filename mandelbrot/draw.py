from mandelbrot.bailout import get_bailout_array
from mandelbrot.color import apply_color
from mandelbrot.configs import Configs
from mandelbrot.save import save


def draw(configs: Configs) -> None:
    bailout_array = get_bailout_array(configs)
    image = apply_color(bailout_array, configs)
    save(configs, image)
