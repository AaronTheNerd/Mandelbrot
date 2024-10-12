import math
from abc import ABC, abstractmethod

from mandelbrot.colormaps import Color
from mandelbrot.configs import Configs


class Blender(ABC):
    @abstractmethod
    def get_pixel_color(self, iterations: float) -> Color: ...


class Plain(Blender):
    def __init__(self, configs: Configs, colormap: list[Color]) -> None:
        self.max_iterations = configs.mandelbrot.max_iterations
        self.colormap = colormap

    def get_pixel_color(self, iterations: float) -> Color:
        if iterations >= self.max_iterations:
            return [0, 0, 0]
        return self.colormap[round(iterations) % len(self.colormap)]


def interpolate(a: float, b: float, t: float):
    return (1 - t) * a + t * b


class Interpolate(Blender):
    def __init__(self, configs: Configs, colormap: list[Color]) -> None:
        self.max_iterations = configs.mandelbrot.max_iterations
        self.colormap = colormap

    def get_pixel_color(self, iterations: float) -> Color:
        if iterations >= self.max_iterations:
            return [0, 0, 0]
        color1 = self.colormap[math.floor(iterations) % len(self.colormap)]
        color2 = self.colormap[(math.floor(iterations) + 1) % len(self.colormap)]
        return [
            int(interpolate(color1[i], color2[i], iterations % 1)) for i in range(3)
        ]


def get_blender(name: str, configs: Configs, colormap: list[Color]) -> Blender:
    blenders = {"plain": Plain, "inter": Interpolate}
    if name not in blenders:
        name = "plain"
    return blenders[name](configs, colormap)
