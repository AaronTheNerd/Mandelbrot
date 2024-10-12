import json
import os
from dataclasses import dataclass,  fields, is_dataclass
from typing import Any, TypeVar


@dataclass
class ImageConfigs:
    width: int
    height: int


@dataclass
class ColorConfigs:
    colormap: str
    blender: str


@dataclass
class MandelbrotConfigs:
    origin: list[float]
    span: float
    max_iterations: int


@dataclass
class Configs:
    image: ImageConfigs
    color: ColorConfigs
    mandelbrot: MandelbrotConfigs


T = TypeVar("T")


def _replaceWithDataclass(raw_configs: dict[str, Any], cls: type[T]) -> T:
    for field in fields(cls):
        if is_dataclass(field.type):
            raw_configs[field.name] = _replaceWithDataclass(
                raw_configs[field.name], field.type
            )
    return cls(**raw_configs)


def load_configs() -> Configs:
    abs_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "..", "configs.json"
    )
    raw_json = {}
    with open(abs_path) as configs:
        raw_json = json.load(configs)
    return _replaceWithDataclass(raw_json, Configs)
