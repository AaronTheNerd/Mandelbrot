from mandelbrot.configs import Configs
from abc import ABC, abstractmethod
import math


class Theme(ABC):
    @abstractmethod
    def get_pixel_color(self, iterations: int) -> list[int]: ...


class Default(Theme):
    def __init__(self, configs: Configs) -> None:
        self.max_iterations = configs.mandelbrot.max_iterations

    def get_pixel_color(self, iteration: float) -> list[int]:
        return [0, 0, 0] if round(iteration) >= self.max_iterations else [255, 255, 255]


class List(Theme):
    def __init__(self, configs: Configs, colors: list[list[int]]) -> None:
        self.max_iterations = configs.mandelbrot.max_iterations
        self.colors = colors

    def get_pixel_color(self, iterations: float) -> list[int]:
        if iterations >= self.max_iterations:
            return [0, 0, 0]
        return self.colors[round(iterations) % len(self.colors)]


def interpolate(a: float, b: float, t: float):
    return (1 - t) * a + t * b


class Interpolate(Theme):
    def __init__(self, configs: Configs, colors: list[list[int]]) -> None:
        self.max_iterations = configs.mandelbrot.max_iterations
        self.colors = colors

    def get_pixel_color(self, iterations: int) -> list[int]:
        if iterations >= self.max_iterations:
            return [0, 0, 0]
        color1 = self.colors[math.floor(iterations) % len(self.colors)]
        color2 = self.colors[(math.floor(iterations) + 1) % len(self.colors)]
        return [
            int(interpolate(color1[i], color2[i], iterations % 1)) for i in range(3)
        ]


def get_theme(theme: str, configs: Configs) -> Theme:
    themes = {
        "default": Default(configs),
        "candy": List(configs, [[255, 0, 0], [255, 255, 255]]),
        "candy_inter": Interpolate(configs, [[255, 0, 0], [255, 255, 255]]),
        "wiki": Interpolate(
            configs,
            [[0, 7, 100], [32, 107, 203], [237, 255, 255], [255, 170, 0], [0, 2, 0]],
        ),
    }
    return themes[theme] if theme in themes else themes["default"]
